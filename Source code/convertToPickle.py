# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:16:12 2020

@author: Kishore
"""
#This code is to convert each text file into a dataframe and save it as a pickle file
import pandas as pd
import glob

dfList = [pd.read_csv(filename,sep='\t',header=None) for filename in glob.glob("/dataverse_files/*.txt") if 'MANIFEST' not in filename]

for i in range(1,(len(dfList)+1)):
    dfList[i-1].to_pickle(str(i)+'.pkl')

    