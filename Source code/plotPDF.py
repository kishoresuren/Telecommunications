# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 18:54:09 2020

@author: Kishore
"""
#This code plots the PDF of traffic intensities over the 2 month period
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

#Load the previously created dictionary of area vs traffic
areaTrafficDic = np.load('areaTrafficDic.npy').item()
trafficIntensities = list(areaTrafficDic.values())
sample_mean = np.mean(trafficIntensities)
sample_std = np.std(trafficIntensities)
# Define the distribution
dist = norm(sample_mean, sample_std)
values = [value for value in range(int(min(trafficIntensities)), int(max(trafficIntensities)+1), 100)]
probabilities = [dist.pdf(value) for value in values]
#Plot the PDF
plt.figure(figsize=(20,20))
plt.xlabel('Traffic Distribution')
plt.ylabel('PDF')
plt.plot(values, probabilities)
plt.savefig('PDF.png')
