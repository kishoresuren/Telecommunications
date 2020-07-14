# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 22:57:18 2020

@author: Kishore
"""
#This code compiles and trains a neural network
from keras.layers import LSTM,Dense
from keras.models import Sequential
import numpy as np
import time

#Define a common neural network for all 3 areas
def createLSTMModel():
    model = Sequential()
    model.add(LSTM(100,input_shape=(wl,1)))
    model.add(Dense(units=40,activation='relu'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

#Train this neural network for 50 epochs and monitor the falling MSE
def fitModel(file,modelname):
    start_time = time.time()
    X= list(np.load(file))
    X_train = np.array([X[i:i+wl] for i in range(len(X)-(wl))])
    y_train = X[wl:]
    X_train = X_train.reshape(X_train.shape[0],X_train.shape[1],1)
    model = createLSTMModel()
    model.fit(X_train,y_train,epochs=50)
    print(file+"takes  %s seconds to train" % (time.time() - start_time))
    model.save(modelname)

#Set window length = 4
wl = 4
#Train and save 3 separate models
fitModel('list5161.npy','trafficmodel_5161.h5')
fitModel('list4159.npy','trafficmodel_4159.h5')
fitModel('list4556.npy','trafficmodel_4556.h5')
#Create and save a dictionary of area vs model
areaModelDic={5161:'trafficmodel_5161.h5',
              4159:'trafficmodel_4159.h5',
              4556:'trafficmodel_4556.h5'}    
np.save('areaModelDic.npy',areaModelDic)