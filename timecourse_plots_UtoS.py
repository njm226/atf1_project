#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:16:19 2019
histogramm and timecourse data
@author: fabio
"""


import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
#from smaller_model_function_AtoU import simple_small as ss
from UtoS_model import simple as ss
import multiprocessing
#import time
import pickle
pool = multiprocessing.Pool(multiprocessing.cpu_count())



X_Y_atf1_on=[[182,100,100,0]] #X_Y_atf1_on=[[182,49,130,0]]
X_Y_atf1_off=[[182,100,100,1]] #X_Y_atf1_off=[[182,49,130,1]]
X_Y_atf1_BS1_on=[[182,100,100,2]] #X_Y_atf1_off=[[182,49,130,1]]
X_Y_atf1_on_AE28=[[182,100,100,3]] #X_Y_atf1_off=[[182,49,130,1]]


reps=10000

repeat=reps*X_Y_atf1_on
repeat_sm=reps*X_Y_atf1_off
repeat_l=reps*X_Y_atf1_BS1_on
repeat_max=reps*X_Y_atf1_on_AE28

duration=201

if __name__ == '__main__':
    status_small = pool.map(ss, repeat) 
    status_m = pool.map(ss, repeat_sm) 
    status_l = pool.map(ss, repeat_l) 
    status_max = pool.map(ss, repeat_max) 

#small system
reporters_diff_small = np.zeros([len(repeat),duration])
reporters_off_small = np.zeros([len(repeat),duration])
reporters_on_small = np.zeros([len(repeat),duration])


cenH_list_small = np.zeros([len(repeat),duration])
EcoRV_list_small = np.zeros([len(repeat),duration])



#medium system
reporters_diff_m = np.zeros([len(repeat),duration])
reporters_off_m = np.zeros([len(repeat),duration])
reporters_on_m = np.zeros([len(repeat),duration])


cenH_list_m = np.zeros([len(repeat),duration])
EcoRV_list_m = np.zeros([len(repeat),duration])


#large system
reporters_diff_l = np.zeros([len(repeat),duration])
reporters_off_l = np.zeros([len(repeat),duration])
reporters_on_l = np.zeros([len(repeat),duration])


cenH_list_l = np.zeros([len(repeat),duration])
EcoRV_list_l = np.zeros([len(repeat),duration])


#large system
reporters_diff_max = np.zeros([len(repeat),duration])
reporters_off_max = np.zeros([len(repeat),duration])
reporters_on_max= np.zeros([len(repeat),duration])


cenH_list_max = np.zeros([len(repeat),duration])
EcoRV_list_max = np.zeros([len(repeat),duration])




for elt in range(len(repeat)):
    
    cenH_small = np.array(status_small[elt][0])
    EcoRV_small = np.array(status_small[elt][1])
    
    
    
    # generate list with cenH and EcoRV states being both at different states (1)
    reporter_diff_small = cenH_small != EcoRV_small
    #transform that vector into a int vector
    reporter_diff_small = reporter_diff_small.astype(int)
    # copy this vector into reporter_states vector
    reporters_diff_small[elt]=reporter_diff_small
    
    
    
    # generate list with cenH and EcoRV states being both switched off
    reporter_off_small = np.zeros(len(cenH_small),'int')
    for index in range(len(cenH_small)):
        if cenH_small[index]==1 and EcoRV_small[index]==1:
            reporter_off_small[index]=1
        else:
            reporter_off_small[index]=0
            
    reporters_off_small[elt]=reporter_off_small
    
    
    
    # generate list with cenH and EcoRV states being both switched on
    reporter_on_small = np.zeros(len(cenH_small),'int')
    for Index in range(len(cenH_small)):
        if cenH_small[Index]==0 and EcoRV_small[Index]==0:
            reporter_on_small[Index]=1
        else:
            reporter_on_small[Index]=0
            
    reporters_on_small[elt]=reporter_on_small
    
    
    #switch the values of the list (1 stands now for timepoint when reporter is on)
    cenH_small=1-cenH_small
    EcoRV_small=1-EcoRV_small
    
    cenH_list_small[elt]=cenH_small
    EcoRV_list_small[elt]=EcoRV_small
    
    
    
    
    
    
    
    
    cenH_m = np.array(status_m[elt][0])
    EcoRV_m = np.array(status_m[elt][1])
    
    
    
    # generate list with cenH and EcoRV states being both at different states (1)
    reporter_diff_m = cenH_m != EcoRV_m
    #transform that vector into a int vector
    reporter_diff_m = reporter_diff_m.astype(int)
    # copy this vector into reporter_states vector
    reporters_diff_m[elt]=reporter_diff_m
    
    
    # generate list with cenH and EcoRV states being both switched off
    reporter_off_m = np.zeros(len(cenH_m),'int')
    for index in range(len(cenH_m)):
        if cenH_m[index]==1 and EcoRV_m[index]==1:
            reporter_off_m[index]=1
        else:
            reporter_off_m[index]=0
            
    reporters_off_m[elt]=reporter_off_m
    
    
    # generate list with cenH and EcoRV states being both switched on
    reporter_on_m = np.zeros(len(cenH_m),'int')
    for Index in range(len(cenH_m)):
        if cenH_m[Index]==0 and EcoRV_m[Index]==0:
            reporter_on_m[Index]=1
        else:
            reporter_on_m[Index]=0
            
    reporters_on_m[elt]=reporter_on_m
    
    #switch the values of the list (1 stands now for timepoint when reporter is on)
    cenH_m=1-cenH_m
    EcoRV_m=1-EcoRV_m
    
    cenH_list_m[elt]=cenH_m
    EcoRV_list_m[elt]=EcoRV_m
    
    
    
    
    cenH_l = np.array(status_l[elt][0])
    EcoRV_l = np.array(status_l[elt][1])
    
    
    
    # generate list with cenH and EcoRV states being both at different states (1)
    reporter_diff_l = cenH_l != EcoRV_l
    #transform that vector into a int vector
    reporter_diff_l = reporter_diff_l.astype(int)
    # copy this vector into reporter_states vector
    reporters_diff_l[elt]=reporter_diff_l
    
    
    # generate list with cenH and EcoRV states being both switched off
    reporter_off_l = np.zeros(len(cenH_l),'int')
    for index in range(len(cenH_l)):
        if cenH_l[index]==1 and EcoRV_l[index]==1:
            reporter_off_l[index]=1
        else:
            reporter_off_l[index]=0
            
    reporters_off_l[elt]=reporter_off_l
    
    
    # generate list with cenH and EcoRV states being both switched on
    reporter_on_l = np.zeros(len(cenH_l),'int')
    for Index in range(len(cenH_l)):
        if cenH_l[Index]==0 and EcoRV_l[Index]==0:
            reporter_on_l[Index]=1
        else:
            reporter_on_l[Index]=0
            
    reporters_on_l[elt]=reporter_on_l
    
    #switch the values of the list (1 stands now for timepoint when reporter is on)
    cenH_l=1-cenH_l
    EcoRV_l=1-EcoRV_l
    
    cenH_list_l[elt]=cenH_l
    EcoRV_list_l[elt]=EcoRV_l
    
    
    
    
    cenH_max = np.array(status_max[elt][0])
    EcoRV_max = np.array(status_max[elt][1])
    
    
    
    # generate list with cenH and EcoRV states being both at different states (1)
    reporter_diff_max = cenH_max != EcoRV_max
    #transform that vector into a int vector
    reporter_diff_max = reporter_diff_max.astype(int)
    # copy this vector into reporter_states vector
    reporters_diff_max[elt]=reporter_diff_max
    
    
    # generate list with cenH and EcoRV states being both switched off
    reporter_off_max = np.zeros(len(cenH_max),'int')
    for index in range(len(cenH_max)):
        if cenH_max[index]==1 and EcoRV_max[index]==1:
            reporter_off_max[index]=1
        else:
            reporter_off_max[index]=0
            
    reporters_off_max[elt]=reporter_off_max
    
    
    # generate list with cenH and EcoRV states being both switched on
    reporter_on_max = np.zeros(len(cenH_max),'int')
    for Index in range(len(cenH_max)):
        if cenH_max[Index]==0 and EcoRV_max[Index]==0:
            reporter_on_max[Index]=1
        else:
            reporter_on_max[Index]=0
            
    reporters_on_max[elt]=reporter_on_max
    
    #switch the values of the list (1 stands now for timepoint when reporter is on)
    cenH_max=1-cenH_max
    EcoRV_max=1-EcoRV_max
    
    cenH_list_max[elt]=cenH_max
    EcoRV_list_max[elt]=EcoRV_max
    
    
    print(cenH_small)
    print(cenH_m)
    print(cenH_l)
    print(cenH_max)
    
    

diff_small = (sum(reporters_diff_small))/reps
off_small = (sum(reporters_off_small))/reps
on_small = (sum(reporters_on_small))/reps




diff_m = (sum(reporters_diff_m))/reps
off_m = (sum(reporters_off_m))/reps
on_m = (sum(reporters_on_m))/reps




diff_l = (sum(reporters_diff_l))/reps
off_l = (sum(reporters_off_l))/reps
on_l = (sum(reporters_on_l))/reps


diff_max = (sum(reporters_diff_max))/reps
off_max = (sum(reporters_off_max))/reps
on_max = (sum(reporters_on_max))/reps



#output
cenH_total_small = (sum(cenH_list_small))/reps
#
EcoRV_total_small = (sum(EcoRV_list_small))/reps




cenH_total_m = (sum(cenH_list_m))/reps
#
EcoRV_total_m = (sum(EcoRV_list_m))/reps


cenH_total_l = (sum(cenH_list_l))/reps
#
EcoRV_total_l = (sum(EcoRV_list_l))/reps


cenH_total_max = (sum(cenH_list_max))/reps
#
EcoRV_total_max = (sum(EcoRV_list_max))/reps



# # save state_list
# with open('UtoS_Atf1_on_S300_AtoU_100_UtoM_100_both_(pos122_pos132).txt', 'wb') as F:
#     pickle.dump(EcoRV_total_small, F)
    
# # save state_list
# with open('UtoS_Atf1_on_S300_AtoU_100_UtoM_100_both_deleted.txt', 'wb') as F:
#     pickle.dump(EcoRV_total_m, F)
    
# # save state_list
# with open('UtoS_Atf1_on_S300_AtoU_100_UtoM_100_one_deleted(at_pos122).txt', 'wb') as F:
#     pickle.dump(EcoRV_total_l, F)
    
# # save state_list
# with open('UtoS_Atf1_on_S300_AtoU_100_UtoM_100_both_present_(pos93_pos132).txt', 'wb') as F:
#     pickle.dump(EcoRV_total_max, F)
    

# # save state_list
# with open('cenH_UtoS_Atf1_on_S300_AtoU_100_UtoM_100_both_present_(pos122_pos132).txt', 'wb') as F:
#     pickle.dump(cenH_total_small, F)
    
# # save state_list
# with open('cenH_UtoS_Atf1_on_S300_AtoU_100_UtoM_100_both_deleted.txt', 'wb') as F:
#     pickle.dump(cenH_total_m, F)
    
# # save state_list
# with open('cenH_UtoS_Atf1_on_S300_AtoU_100_UtoM_100_one_deleted(at_pos_122).txt', 'wb') as F:
#     pickle.dump(cenH_total_l, F)
    
# # save state_list
# with open('cenH_UtoS_Atf1_on_S300_AtoU_100_UtoM_100_both_present_(pos_93_pos132).txt', 'wb') as F:
#     pickle.dump(cenH_total_max, F)
    
    
    

time = np.array(range(duration))

y_axis = np.array([cenH_total_small, EcoRV_total_small,  cenH_total_m, EcoRV_total_m])
        
#fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=((36, 12)))
fig, (ax1) = plt.subplots(nrows=1, ncols=1, figsize=((15, 10)))
#default line colors and styles
ax1.plot(time,EcoRV_total_small, color='yellowgreen', label='mCherry: both atf1-sites present (pos 122 and pos 132)')
ax1.plot(time,cenH_total_small, color='cyan', label='cenH: both atf1-sites present ')
ax1.plot(time,EcoRV_total_m, color='black', label='mCherr: both atf1-sites deleted')
ax1.plot(time,EcoRV_total_l, color='grey', label='mCherry: one atf1-site deleted (at pos 122)')
ax1.plot(time,EcoRV_total_max, color='red', label='mCherry ME2: both atf1-sites present (pos 110 and pos 132)')
#ax1.plot(time,cenH_total_m,'ro', label='cenH 24 kb region')
ax1.legend(loc='upper left')
#ax1.set_ylabel("fraction of 'ON' cells", fontsize = 35)  
#ax1.set_xlabel('t (generations)', fontsize = 35)  
ax1.set_yscale('log')    
ax1.tick_params(labelsize='30')
ax1.set_ylim([0.001,1])
ax1.set_xlim([1,200])
ax1.legend(fontsize='25')

plt.savefig("UtoS_S300_all_100_atf1_pos92_pos132.pdf")
    

# #fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=((36, 12)))
# fig, (ax1) = plt.subplots(nrows=1, ncols=1, figsize=((12, 10)))
# #default line colors and styles
# ax1.plot(time,EcoRV_total_small, color='yellowgreen', label='EcoRV 20 kb region')
# ax1.plot(time,cenH_total_small, color='cyan', label='cenH 20 kb region')
# ax1.plot(time,EcoRV_total_m, color='red', label='EcoRV 24 kb region')
# #ax1.plot(time,cenH_total_m,'ro', label='cenH 24 kb region')
# ax1.plot(time,EcoRV_total_large, color='black', label='EcoRV 26 kb region')
# #ax1.plot(time,cenH_total_large, color='blue', label='cenH 26 kb region')
# ax1.plot(time,EcoRV_total_max, color='gold', label='EcoRV 28 kb region')
# #ax1.plot(time,cenH_total_max, color='purple', label='cenH 28 kb region')
# #ax1.set_title('Combined debt growth over time')
# #ax1.legend(loc='upper left')
# ax1.set_ylabel('fraction of ''ON'' cells', fontsize = 25)  
# ax1.set_xlabel('t (generations)', fontsize = 25)  
# ax1.set_yscale('log')    
# ax1.tick_params(labelsize='18')
# ax1.set_ylim([0.01,1])
# ax1.set_xlim([1,46])
# ax1.legend(fontsize='20')

#plt.savefig("timecourse_small_SUS350")

# ax2.plot(time, off_small, color='k')
# ax2.plot(time, on_small, color='b')
# ax2.plot(time, diff_small, color='r')
# #ax1.set_title('Combined debt growth over time')
# #ax1.legend(loc='upper left')
# ax2.set_ylabel('fraction of cells (small system)', fontsize = 26)  
# ax2.set_xlabel('t (generations)', fontsize = 25)   
# ax2.tick_params(labelsize='18') 
# ax2.set_ylim([0,1])
# ax2.set_xlim([1,100])

# ax3.plot(time, off_large, color='k')
# ax3.plot(time, on_large, color='b')
# ax3.plot(time, diff_large, color='r')
# #ax1.set_title('Combined debt growth over time')
# #ax1.legend(loc='upper left')
# ax3.set_ylabel('fraction of cells (large system)', fontsize = 25)  
# ax3.set_xlabel('t (generations)', fontsize = 25)   
# ax3.tick_params(labelsize='18') 
# ax3.set_ylim([0,1])
# ax3.set_xlim([1,100])

















