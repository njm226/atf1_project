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
from AtoU_model import simple as ss
import multiprocessing
import time
import pickle
# from scipy.optimize import curve_fit
# import uncertainties as unc
# import uncertainties.unumpy as unp
pool = multiprocessing.Pool(multiprocessing.cpu_count())


#parameters = [[190,40,1],[40,180,1],[50,130,1],[60,80,1],[20,90,1],[40,150,2],[50,100,2],[70,40,2],[10,100,2],[30,200,3],[30,190,3],[40,130,3],[50,80,3],[30,170,4],[40,110,4],[50,50,4],[30,150,5],[40,100,5],[50,70,5],[100,10,5]]
#parameters = [[30,200,3],[30,190,3],[40,130,3],[50,80,3],[30,170,4],[40,110,4],[50,50,4],[30,150,5],[50,70,5]]
parameters = [[30,160,5]]
#parameters = [[20,90,0.5],[40,20,0.5],[20,70,1],[40,15,1],[15,95,1.5],[35,20,1.5]]
reps=10000
duration=201
t1 = time.time()
for p in parameters:

            
            
            

        
        
        
        
        #all 27.5 kb region!!
        
        X_Y_atf1_on=[[153,p[0],p[1],p[2],4]] #X_Y_atf1_on=[[182,49,130,0]]

        
        
        repeat_atf1_on=reps*X_Y_atf1_on

        
        
        if __name__ == '__main__':
            status_atf1_on = pool.map(ss, repeat_atf1_on) 

        

        
        
        cenH_list_atf1_on = np.zeros([reps,duration])
        EcoRV_list_atf1_on = np.zeros([reps,duration])
        
        
        

        
        
        
        for elt in range(reps):
            
            cenH_atf1_on = np.array(status_atf1_on[elt][0])
            EcoRV_atf1_on = np.array(status_atf1_on[elt][1])
         
            #switch the values of the list (1 stands now for timepoint when reporter is on)
            cenH_atf1_on=1-cenH_atf1_on
            EcoRV_atf1_on=1-EcoRV_atf1_on
            
            cenH_list_atf1_on[elt]=cenH_atf1_on
            EcoRV_list_atf1_on[elt]=EcoRV_atf1_on
            
        

        
        #output
        cenH_total_atf1_on = (sum(cenH_list_atf1_on))/reps
        #
        EcoRV_total_atf1_on = (sum(EcoRV_list_atf1_on))/reps
        
        
        
        
        
        cenH_total = [cenH_total_atf1_on]
        EcoRV_total = [EcoRV_total_atf1_on]
    
        
        
        # save state_list
        with open('gAtoU_dcr_del_cenH_Atf1_65_S250_UtoS%5.1f_AtoU%5.1f_direct%5.1f_reactivation_cenH_on.txt' %tuple(p), 'wb') as F:
            pickle.dump(cenH_total, F)
            
        
        # save state_list
        with open('gAtoU_dcr_del_EcoRV_Atf1_65_S250_UtoS%5.1f_AtoU%5.1f_direct%5.1f_reactivation_cenH_on.txt' %tuple(p), 'wb') as F:
            pickle.dump(EcoRV_total, F)


        print(p)
        print(time.time()-t1)












