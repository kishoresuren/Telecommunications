# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:16:47 2020

@author: Kishore
"""
#This code displays the plots of the time series traffic intensities over the first 14 day period
import pandas as pd
import matplotlib.pyplot as plt

#Plot a bar graph displaying the time series
def plotPDF(area):
    plt.rcParams.update({'font.size': 22})
    plt.figure(figsize=(20,20))
    plt.title('2 week traffic for area '+str(area))
    plt.xlabel('Day')
    plt.ylabel('Traffic Intensity')
    plt.bar([i for i in range(1,15)] , areaTrafficDailyDic[area],width=0.5,align='center')
    plt.savefig(str(area)+'_2 week traffic.png')

#Consider the 3 areas mentioned in the question
areaTrafficDailyDic={5161:[],4159:[],4556:[]}
for file in range(1,15):
    df = pd.read_pickle(str(file)+'.pkl')
    #Assign dummy names to columns
    df.columns=['a','b','c','d','e','f','g','h']    
    df['h']=[0 if str(i)=='nan' else i for i in df['h']]
    trafficValues=list(df.groupby(['a']).sum().reset_index()['h'])
    #Append the values over the 2 week period to the corresponding dictionary key 
    areaTrafficDailyDic[5161].append(trafficValues[5160])
    areaTrafficDailyDic[4159].append(trafficValues[4158])
    areaTrafficDailyDic[4556].append(trafficValues[4555])


plotPDF(5161)
plotPDF(4159)
plotPDF(4556)