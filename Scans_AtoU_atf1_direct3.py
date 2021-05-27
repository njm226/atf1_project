#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:16:19 2019
Parameter scans
@author: fabio
"""

import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
from smaller_model_function_AtoU import simple_small as ss
from AtoU_model import simple
import multiprocessing
import time
import pickle
from scipy.optimize import curve_fit
#import uncertainties as unc

# mp
time_start = time.time()
#pool = multiprocessing.Pool(multiprocessing.cpu_count(), maxtasksperchild=None)
pool = multiprocessing.Pool(multiprocessing.cpu_count())

size = 182
direct = 1.5


# Generate determin parameter x and y values
#X = [1,2,3,4,5] # list of all global rate S(A->U) values
#
#X = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
X = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200] # list of all global rate S(A->U) values
Y = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200] #and all local rate S(U->S) values

#Y = [70,85,100,115,130] #and all local rate S(U->S) values

# X = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40] # list of all global rate S(A->U) values
# Y = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]

X = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100] # list of all global rate S(A->U) values
Y = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]


y = Y*len(X) # at the x-axis, the S value range is repeated 10 times
x = [] # and for the y-axis, each value is repeated 28 times
for i in range(len(X)):
    for j in range(len(Y)):
        x.append(X[i])

x = np.array(x)
y = np.array(y)

#generate list with all value pairs of all system sizes
data_pairs_small = []
for i in X:
    for j in Y:
        data_pairs_small.append([i,j,direct])


data_pairs = []
for i in X:
    for j in Y:
        data_pairs.append([size,i,j,direct,0])

data_pairs_sm = []
for i in X:
    for j in Y:
        data_pairs_sm.append([size,i,j,direct,1])

data_pairs_sl = []
for i in X:
    for j in Y:
        data_pairs_sl.append([size,i,j,direct,2])

# data_pairs_l = []
# for i in X:
#     for j in Y:
#         data_pairs_l.append([size,i,j,3])


state_list = pool.map(ss, data_pairs_small)



with open('state_ss_atf1_AtoU_direct3_factor2_reduced.txt', 'wb') as F:
      pickle.dump(state_list, F)




b_value_list = []

cenH_silenced = 0
EcoRV_silenced = 0

cenH_silenced_sm = 0
EcoRV_silenced_sm = 0

cenH_silenced_sl = 0
EcoRV_silenced_sl = 0

duration=201#15

# this for loop goes through all data_pairs (list of 400) and repeats simulation reps times
for i in range(len(data_pairs)):


    #determine how often the simulation for each system and specific parameter pair should be repeated
    reps=1000

    repeat = [data_pairs[i]]*reps
    repeat_sm = [data_pairs_sm[i]]*reps
    repeat_sl = [data_pairs_sl[i]]*reps


    # store the simulation results (status list of cenH and EcoRV) of each simulation
    if __name__ == '__main__':
        #
        status_small = pool.map(simple, repeat)
        status_m = pool.map(simple, repeat_sm)
        status_large = pool.map(simple, repeat_sl)


    # two dimensional arrays with dimensions len(repeat) and duration (pre allocation)
    cenH_list_small = np.zeros([len(repeat),duration])
    EcoRV_list_small = np.zeros([len(repeat),duration])


    cenH_list_m = np.zeros([len(repeat),duration])
    EcoRV_list_m = np.zeros([len(repeat),duration])


    cenH_list_large = np.zeros([len(repeat),duration])
    EcoRV_list_large = np.zeros([len(repeat),duration])


    cenH_list_max = np.zeros([len(repeat),duration])
    EcoRV_list_max = np.zeros([len(repeat),duration])




    # fill the columns with information on the status of different cells in parallel
    # at a certain (fixed) timepoint
    for elt in range(len(repeat)):

        cenH_small = np.array(status_small[elt][0])
        EcoRV_small = np.array(status_small[elt][1])

        #switch the values of the list (1 stands now for timepoint when reporter is on)
        cenH_small=1-cenH_small
        EcoRV_small=1-EcoRV_small

        # stores the cenH part in a seperate two dimensional array (reps X duration)
        cenH_list_small[elt]=cenH_small
        EcoRV_list_small[elt]=EcoRV_small






        cenH_m = np.array(status_m[elt][0])
        EcoRV_m = np.array(status_m[elt][1])

        #switch the values of the list (1 stands now for timepoint when reporter is on)
        cenH_m=1-cenH_m
        EcoRV_m=1-EcoRV_m

        # stores the cenH part in a seperate two dimensional array (reps X duration)
        cenH_list_m[elt]=cenH_m
        EcoRV_list_m[elt]=EcoRV_m






        cenH_large = np.array(status_large[elt][0])
        EcoRV_large = np.array(status_large[elt][1])

        #switch the values of the list (1 stands now for timepoint when reporter is on)
        cenH_large=1-cenH_large
        EcoRV_large=1-EcoRV_large

        # stores the cenH part in a seperate two dimensional array (reps X duration)
        cenH_list_large[elt]=cenH_large
        EcoRV_list_large[elt]=EcoRV_large




        # print(cenH_small)
        # print(cenH_m)
        # print(cenH_large)
        # print(cenH_max)




    #output (Histograms!)
    cenH_total_small = (sum(cenH_list_small))/reps
    #
    ys = (sum(EcoRV_list_small))/reps




    cenH_total_m = (sum(cenH_list_m))/reps
    #
    ym = (sum(EcoRV_list_m))/reps




    cenH_total_large = (sum(cenH_list_large))/reps
    #
    yl = (sum(EcoRV_list_large))/reps





    ys = ys[3:]
    ym = ym[3:]
    yl = yl[3:]
    x = np.array(range(duration-3))

    # fitting function
    def model(x,a,b):
        return a*np.exp(-x/b)

    #Perform the curve fit
    popt_s, pcov_s = curve_fit(model, x, ys, p0=[1,1], maxfev=5000)
    #print(popt_s)

    b_s = popt_s[1]

    #a_s, b_s = unc.correlated_values(popt_s, pcov_s)



     #Perform the curve fit
    popt_m, pcov_m = curve_fit(model, x, ym, p0=[1,1], maxfev=5000)
    #print(popt_s)

    b_m = popt_m[1]

    #a_m, b_m = unc.correlated_values(popt_m, pcov_m)



     #Perform the curve fit
    popt_l, pcov_l = curve_fit(model, x, yl, p0=[1,1], maxfev=5000)
    #print(popt_s)

    b_l = popt_l[1]

    #a_l, b_l = unc.correlated_values(popt_l, pcov_l)



    b = [b_s, b_m, b_l]
    print(b)

    b_value_list.append(b)


# save Timing list
with open('b_list_S100_atf1_AtoU_direct3_factor2_reduced.txt', 'wb') as F:
    pickle.dump(b_value_list, F)
