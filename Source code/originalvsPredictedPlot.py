# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 21:51:23 2020

@author: Kishore
"""
#This code prepares the training set for the 3 areas
import pandas as pd
import numpy as np

#Consider all dates except December 16th to December 22nd
trainDays=[i for i in range(1,46)]+[k for k in range(53,60)]
def appendEntries(l,area):
    print(str(area))
    for file in trainDays:
        df = pd.read_pickle(str(file)+'.pkl')
        df.columns=['a','b','c','d','e','f','g','h']    
        df['h']=[0 if str(i)=='nan' else i for i in df['h']]
        #Append all traffic intensities for the corresponding area per day
        l+=[df['h'][k] for k in [i for i,j in enumerate(df['a']) if j==area]] 
    return l

list5161=[]
list4159=[]
list4556=[]
list5161=appendEntries(list5161,5161)
list4159=appendEntries(list4159,4159)
list4556=appendEntries(list4556,4556)

#Save the lists as numpy arrays for the model training
np.save('list5161_train.npy',list5161)
np.save('list4159_train.npy',list4159)
np.save('list4556_train.npy',list4556)

    