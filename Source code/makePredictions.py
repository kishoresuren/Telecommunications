# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 22:01:06 2020

@author: Kishore
"""
#This code performs predictions on the pre-built model and displays the predicted plots
import pandas as pd
import numpy as np
from keras.models import load_model
from sklearn.metrics import mean_absolute_error as MAE
import matplotlib.pyplot as plt
import time
import sys

#Consider only dates between December 16th to December 22nd
testDays=[i for i in range(46,53)]
def appendEntries(l,area):
    print(str(area))
    for file in testDays:
        df = pd.read_pickle(str(file)+'.pkl')
        df.columns=['a','b','c','d','e','f','g','h']    
        df['h']=[0 if str(i)=='nan' else i for i in df['h']]
        l+=[df['h'][k] for k in [i for i,j in enumerate(df['a']) if j==area]] 
    return l

def createPlot(type,area,y):
    plt.rcParams.update({'font.size': 22})
    plt.figure(figsize=(20,15))
    plt.title(type+' traffic intensities between December 16th and 22nd in area '+str(area))
    plt.ylabel('Traffic')
    plt.xlabel('Day')
    plt.plot([i for i in range(len(y))] , y)
    plt.savefig(type+'_'+str(area)+'.png')

def makePrediction(X,area):
    start_time = time.time()
    model = load_model(areaModelDic[area])
    X_test = np.array([X[i:i+wl] for i in range(len(X)-(wl))])
    y_test = X[wl:]
    X_test = X_test.reshape(X_test.shape[0],X_test.shape[1],1)
    y_pred = model.predict(X_test)
    print(str(area)+" takes  %s seconds to predict" % (time.time() - start_time))
    print('MAE is: {:.3f}'.format(MAE(y_pred,y_test)))
    #0.1 is added to each element of y_test to avoid division by zero
    print('MAPE is: {:.3f}'.format(np.mean(np.abs((y_test - y_pred) / ([i+0.1 for i in y_test]))) * 100))
    createPlot('Original',area,y_test)
    createPlot('Predicted',area,y_pred)
    

wl=4
areaModelDic = np.load('areaModelDic.npy').item()
areaCode = int(sys.argv[1])

#Below code is for running in Linux
if areaCode ==5161:
    list5161 = list(np.load('list5161_test.npy'))
    print('5161')
    makePrediction(list5161,5161)
elif areaCode ==4159:
    print('4159')
    list4159 = list(np.load('list4159_test.npy'))
    makePrediction(list4159,4159)
elif areaCode ==4556:
    print('4556')
    list4556=list(np.load('list4556_test.npy'))
    makePrediction(list4556,4556)
else:
    print('Invalid Area code: Please enter any of the following: 5161,4159,4556')


#Uncomment if the .pkl files are present  
# =============================================================================
# areaModelDic=np.load('areaModelDic.npy').item()
# list5161=[]
# list4159=[]
# list4556=[]
# list5161=appendEntries(list5161,5161)
# list4159=appendEntries(list4159,4159)
# list4556=appendEntries(list4556,4556)
# 
# makePrediction(list5161,5161)
# makePrediction(list4159,4159)
# makePrediction(list4556,4556)
# =============================================================================

