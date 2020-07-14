# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 08:40:09 2020

@author: Kishore
"""
#This code generates a dictionary of area vs total traffic over 2 months
import pandas as pd
import numpy as np

areaTrafficDic={i:0 for i in range(1,10000)}
hList = [0 for i in range(1,10000)]
for file in range(1,60):
    #Load each pickle file
    df = pd.read_pickle(str(file)+'.pkl')
    #Assign dummy names to columns
    df.columns=['a','b','c','d','e','f','g','h']
    #Column 'h' contains traffic information. Replace nan by 0
    df['h']=[0 if str(i)=='nan' else i for i in df['h']]
    #Sum the traffic values of each area within a day, and consequently over 2 months
    hList = [i+j for i,j in zip(hList,list(df.groupby(['a']).sum().reset_index()['h']))]
    areaTrafficDic={i:j for i,j in zip([k for k in range(1,10000)],hList)}


np.save('areaTrafficDic.npy',areaTrafficDic)

