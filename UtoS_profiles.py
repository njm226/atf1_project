#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:16:19 2019
histogramm and timecourse data
@author: fabio
"""


import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#from smaller_model_function_AtoU import simple_small as ss
from UtoS_model import simple as ss
import multiprocessing
#import time
import pickle
# from scipy.optimize import curve_fit
# import uncertainties as unc
# import uncertainties.unumpy as unp
pool = multiprocessing.Pool(multiprocessing.cpu_count())


parameters = [[50,190,5],[60,150,5]]
reps=10000
duration=201

for p in parameters:
    
        #all wt!!
        
        wt_X_Y_atf1_on=[[153,p[0],p[1],p[2],0]] #X_Y_atf1_on=[[182,49,130,0]]
        wt_X_Y_atf1_off=[[153,p[0],p[1],p[2],1]] #X_Y_atf1_off=[[182,49,130,1]]
        wt_X_Y_atf1_BS1_on=[[153,p[0],p[1],p[2],2]] #X_Y_atf1_off=[[182,49,130,1]]
        wt_X_Y_atf1_BS2_on=[[153,p[0],p[1],p[2],3]] #X_Y_atf1_off=[[182,49,130,1]]
        
        
        
        wt_repeat_atf1_on=reps*wt_X_Y_atf1_on
        wt_repeat_atf1_off=reps*wt_X_Y_atf1_off
        wt_repeat_atf1_BS1_on=reps*wt_X_Y_atf1_BS1_on
        wt_repeat_atf1_BS2_on=reps*wt_X_Y_atf1_BS2_on
        
        
        if __name__ == '__main__':
            wt_status_atf1_on = pool.map(ss, wt_repeat_atf1_on) 
            wt_status_atf1_off = pool.map(ss, wt_repeat_atf1_off) 
            wt_status_atf1_BS1_on = pool.map(ss, wt_repeat_atf1_BS1_on) 
            wt_status_atf1_BS2_on = pool.map(ss, wt_repeat_atf1_BS2_on) 
        

        
        
        cenH_list_atf1_on = np.zeros([reps,duration])
        EcoRV_list_atf1_on = np.zeros([reps,duration])
        
        
        

        
        
        cenH_list_atf1_off = np.zeros([reps,duration])
        EcoRV_list_atf1_off = np.zeros([reps,duration])
        
        

        
        
        cenH_list_atf1_BS1_on = np.zeros([reps,duration])
        EcoRV_list_atf1_BS1_on = np.zeros([reps,duration])
        
        

        
        cenH_list_atf1_BS2_on = np.zeros([reps,duration])
        EcoRV_list_atf1_BS2_on = np.zeros([reps,duration])
        
        
        
        
        for elt in range(reps):
            
            cenH_atf1_on = np.array(wt_status_atf1_on[elt][0])
            EcoRV_atf1_on = np.array(wt_status_atf1_on[elt][1])
         
            #switch the values of the list (1 stands now for timepoint when reporter is on)
            cenH_atf1_on=1-cenH_atf1_on
            EcoRV_atf1_on=1-EcoRV_atf1_on
            
            cenH_list_atf1_on[elt]=cenH_atf1_on
            EcoRV_list_atf1_on[elt]=EcoRV_atf1_on
            
        
            
            
            cenH_atf1_off = np.array(wt_status_atf1_off[elt][0])
            EcoRV_atf1_off = np.array(wt_status_atf1_off[elt][1])

            #switch the values of the list (1 stands now for timepoint when reporter is on)
            cenH_atf1_off=1-cenH_atf1_off
            EcoRV_atf1_off=1-EcoRV_atf1_off
            
            cenH_list_atf1_off[elt]=cenH_atf1_off
            EcoRV_list_atf1_off[elt]=EcoRV_atf1_off
            
            
            
            
            cenH_atf1_BS1_on = np.array(wt_status_atf1_BS1_on[elt][0])
            EcoRV_atf1_BS1_on = np.array(wt_status_atf1_BS1_on[elt][1])
            
            #switch the values of the list (1 stands now for timepoint when reporter is on)
            cenH_atf1_BS1_on=1-cenH_atf1_BS1_on
            EcoRV_atf1_BS1_on=1-EcoRV_atf1_BS1_on
            
            cenH_list_atf1_BS1_on[elt]=cenH_atf1_BS1_on
            EcoRV_list_atf1_BS1_on[elt]=EcoRV_atf1_BS1_on
            
            
            
            
            cenH_atf1_BS2_on = np.array(wt_status_atf1_BS2_on[elt][0])
            EcoRV_atf1_BS2_on = np.array(wt_status_atf1_BS2_on[elt][1])
           
            
            #switch the values of the list (1 stands now for timepoint when reporter is on)
            cenH_atf1_BS2_on=1-cenH_atf1_BS2_on
            EcoRV_atf1_BS2_on=1-EcoRV_atf1_BS2_on
            
            cenH_list_atf1_BS2_on[elt]=cenH_atf1_BS2_on
            EcoRV_list_atf1_BS2_on[elt]=EcoRV_atf1_BS2_on
            
            
            print(cenH_atf1_on)
            print(cenH_atf1_off)
            print(cenH_atf1_BS1_on)
            print(cenH_atf1_BS2_on)

        
        #output
        wt_cenH_total_atf1_on = (sum(cenH_list_atf1_on))/reps
        #
        wt_EcoRV_total_atf1_on = (sum(EcoRV_list_atf1_on))/reps
        
        
        
        
        wt_cenH_total_atf1_off = (sum(cenH_list_atf1_off))/reps
        #
        wt_EcoRV_total_atf1_off = (sum(EcoRV_list_atf1_off))/reps
        
        
        wt_cenH_total_atf1_BS1_on = (sum(cenH_list_atf1_BS1_on))/reps
        #
        wt_EcoRV_total_atf1_BS1_on = (sum(EcoRV_list_atf1_BS1_on))/reps
        
        
        wt_cenH_total_atf1_BS2_on = (sum(cenH_list_atf1_BS2_on))/reps
        #
        wt_EcoRV_total_atf1_BS2_on = (sum(EcoRV_list_atf1_BS2_on))/reps
        
        
        
        
        cenH_total_wt = [wt_cenH_total_atf1_on,wt_cenH_total_atf1_off,wt_cenH_total_atf1_BS1_on,wt_cenH_total_atf1_BS2_on]
        EcoRV_total_wt = [wt_EcoRV_total_atf1_on,wt_EcoRV_total_atf1_off,wt_EcoRV_total_atf1_BS1_on,wt_EcoRV_total_atf1_BS2_on]
        
        wt_cenH_all_data_points = wt_cenH_total_atf1_on + wt_cenH_total_atf1_off + wt_cenH_total_atf1_BS1_on + wt_cenH_total_atf1_BS2_on 
        
        
        # save state_list
        with open('wt_cenH_Atf1_S40_UtoS%5.1f_AtoU%5.1f_direct%5.1f.txt' %tuple(p), 'wb') as F:
            pickle.dump(cenH_total_wt, F)
            
        
        # save state_list
        with open('wt_EcoRV_Atf1_S40_UtoS%5.1f_AtoU%5.1f_direct%5.1f.txt' %tuple(p), 'wb') as F:
            pickle.dump(EcoRV_total_wt, F)
            
            
            
        # # fitting function
        # def model(x,a,b):
        #     return a*np.exp(-x/b)
        
        # time = np.array(range(duration))
        
        
            
        # #Perform the curve fit
        # popt1, pcov1 = curve_fit(model, time[3:], wt_EcoRV_total_atf1_on[3:])
        
        # a1, b1 = unc.correlated_values(popt1, pcov1)
        
        # # Plot data and best fit curve.
        # plt.scatter(time, wt_EcoRV_total_atf1_on, s=3, linewidth=0, alpha=0.3)
        
        # px1 = np.linspace(1, 200, 200)
        # # use unumpy.exp
        # py1 = a1 * unp.exp(-px1/b1)
        
        # nom1 = unp.nominal_values(py1)
        # std1 = unp.std_devs(py1)
        
        
        # #fx values for the fitted function
        # xFit1 = np.arange(0.0, 200, 0.001)
        
        
        
        
        
        # #Perform the curve fit
        # popt2, pcov2 = curve_fit(model, time[3:], wt_EcoRV_total_atf1_off[3:])
        # print(popt2)
        
        # a2, b2 = unc.correlated_values(popt2, pcov2)
        
        # # Plot data and best fit curve.
        # plt.scatter(time, wt_EcoRV_total_atf1_off, s=3, linewidth=0, alpha=0.3)
        
        # px2 = np.linspace(1, 200, 200)
        # # use unumpy.exp
        # py2 = a2 * unp.exp(-px2/b2)
        
        # nom2 = unp.nominal_values(py2)
        # std2 = unp.std_devs(py2)
        
        # # plot the nominal value
        # plt.plot(px2, nom2, c='r')
        
        # #fx values for the fitted function
        # xFit2 = np.arange(0.0, 200, 0.001)
        
        
        
        
        # #Perform the curve fit
        # popt3, pcov3 = curve_fit(model, time[3:], wt_EcoRV_total_atf1_BS1_on[3:])
        # print(popt3)
        
        # a3, b3 = unc.correlated_values(popt3, pcov3)
        
        # # Plot data and best fit curve.
        # plt.scatter(time, wt_EcoRV_total_atf1_BS1_on, s=3, linewidth=0, alpha=0.3)
        
        # px3 = np.linspace(1, 200, 200)
        # # use unumpy.exp
        # py3 = a3 * unp.exp(-px3/b3)
        
        # nom3 = unp.nominal_values(py3)
        # std3 = unp.std_devs(py3)
        
        # # plot the nominal value
        # plt.plot(px3, nom3, c='r')
        
        # #fx values for the fitted function
        # xFit3 = np.arange(0.0, 200, 0.001)
        
        
        
        
        # #Perform the curve fit
        # popt4, pcov4 = curve_fit(model, time[3:], wt_EcoRV_total_atf1_BS2_on[3:])
        # print(popt4)
        
        # a4, b4 = unc.correlated_values(popt4, pcov4)
        
        # # Plot data and best fit curve.
        # plt.scatter(time, wt_EcoRV_total_atf1_BS1_on, s=3, linewidth=0, alpha=0.3)
        
        # px4 = np.linspace(1, 200, 200)
        # # use unumpy.exp
        # py4 = a4 * unp.exp(-px4/b4)
        
        # nom4 = unp.nominal_values(py4)
        # std4 = unp.std_devs(py4)
        
        # # plot the nominal value
        # plt.plot(px4, nom4, c='r')
        
        # #fx values for the fitted function
        # xFit4 = np.arange(0.0, 200, 0.001)
        
        
        
        
        # #Perform the curve fit
        # popt5, pcov5 = curve_fit(model, time[3:], wt_cenH_all_data_points[3:])
        # print(popt5)
        
        # a5, b5 = unc.correlated_values(popt5, pcov5)
        
        # # Plot data and best fit curve.
        # plt.scatter(time, wt_cenH_all_data_points, s=3, linewidth=0, alpha=0.3)
        
        # px5 = np.linspace(1, 200, 200)
        # # use unumpy.exp
        # py5 = a5 * unp.exp(-px5/b5)
        
        # nom5 = unp.nominal_values(py5)
        # std5 = unp.std_devs(py5)
        
        # # plot the nominal value
        # plt.plot(px5, nom5, c='r')
        
        # #fx values for the fitted function
        # xFit5 = np.arange(0.0, 200, 0.001)
        

        
        # #plot the fitted function
        # plt.figure(figsize=[15,10])
        # #plt.plot(xFit1, model(xFit1, *popt1), label='fit params: a=%5.1f, b=%5.1f' % tuple(popt1), lw=3.)
        # plt.plot(time, wt_EcoRV_total_atf1_on, 'b', label='model data (atf1 on) with a=%5.1f, b=%5.1f' % tuple(popt1), lw=3.)
        
        
        # #plt.plot(xFit2, model(xFit2, *popt2), 'r', label='fit params: a=%5.1f, b=%5.1f' % tuple(popt2), lw=3.)
        # plt.plot(time, wt_EcoRV_total_atf1_off, 'r', label='model data (atf1 off) with a=%5.1f, b=%5.1f' % tuple(popt2), lw=3.)
        # # 
        
        
        # #plt.plot(xFit3, model(xFit3, *popt3), 'g', label='fit params: a=%5.1f, b=%5.1f' % tuple(popt3), lw=3.)
        # plt.plot(time, wt_EcoRV_total_atf1_BS1_on, 'g', label='model data (only BS1 on) witha=%5.1f, b=%5.1f' % tuple(popt3), lw=3.)
        
        
        # #plt.plot(xFit3, model(xFit3, *popt3), 'g', label='fit params: a=%5.1f, b=%5.1f' % tuple(popt3), lw=3.)
        # plt.plot(time, wt_EcoRV_total_atf1_BS1_on, 'salmon', label='model data (only BS2 on) with a=%5.1f, b=%5.1f' % tuple(popt4), lw=3.)
        
        # #plt.plot(xFit3, model(xFit3, *popt3), 'g', label='fit params: a=%5.1f, b=%5.1f' % tuple(popt3), lw=3.)
        # plt.plot(time, wt_cenH_all_data_points, 'yellow', label='model data (cenH all systems) ', lw=2.)
        # #plt.plot(time, cenH2, 'salmon', label='model data (cenH: atf1 off) with a=%5.1f, b=%5.1f' % tuple(popt5), lw=3.)
        # #plt.plot(time, cenH3, 'lightgreen', label='model data (cenH: ME20)', lw=2.)
        
        # plt.ylim([0.001,1])
        # plt.yticks(fontsize=40)
        # plt.xticks(fontsize=30)
        # plt.xlim([0,200])
        # plt.yscale('log')
        # plt.xticks([25, 50, 75, 100, 125, 150, 175, 200])
        # plt.yticks([1,0.1,0.01],[1, 0.1, 0.01])
        # #plt.ylabel('fraction of "ON" cells', fontsize=30)
        # #plt.xlabel('time (generations)', fontsize=30)
        # plt.legend(fontsize=18,loc="upper right")
        # plt.tick_params(width=4,length=4)
        
        # plt.savefig('wt_UtoS_model_atf1_UtoS_%_AtoU_%_direct_%.txt' %tuple(p), format='pdf')
        
    

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

















