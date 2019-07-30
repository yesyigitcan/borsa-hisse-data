# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 11:08:48 2019

@author: st900373
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#////////////////// Data Set First Combine with Dollar ///////////////////#

dataset = pd.read_excel('D:\\Users\\st900373\\Desktop\\doviz.xls')
vkf = dataset[dataset["name"] == "VAKBN"]
dollars = dataset[dataset["name"] == "SUSD"]

dollars = dollars[["date","open","close","high","low"]]
dollars.columns = ["date","dollar_open","dollar_close","dollar_high","dollar_low"]
dataset = pd.merge(vkf,dollars,on="date",how="right")
dataset = dataset.drop("isCurrency",axis=1)
dataset = dataset.dropna()

dataset.head()


#//////////// Data Set Last n Value Average and Increase Average /////////////////#

vkf_array = dataset.values.tolist()
vkf_len = len(vkf_array)
n = 7

dataset.columns
dataset.head()

selected_col = [2,3,4,5,6,7,8,9,10]

for col in selected_col:
    for i in range(vkf_len - n):
        temp_ort = 0.0
        temp_art_ort = 0.0
        for j in range(i,i+n):
            temp_ort = temp_ort + vkf_array[j][col]
        for j in range(i,i+n-1):
            temp_art_ort += ( (vkf_array[j+1][col] - vkf_array[j][col] ) / vkf_array[j][col] ) * 100.0
        temp_ort = temp_ort / n
        temp_art_ort = temp_art_ort / n
        vkf_array[i+n].append(temp_ort)
        vkf_array[i+n].append(temp_art_ort)

    #print(temp)
vkf_array[10]



cols = list(dataset.columns)
temp_col = cols[2:11]
for i in temp_col:
    cols.append(i + "_last_five")
    cols.append(i + "_increase_last_five")
cols


dataset = pd.DataFrame(vkf_array,columns=cols)
dataset = dataset.dropna()
dataset.columns


#//////////// Writing Data Set into Excel /////////////////#
dataset.to_excel("D:\\Users\\st900373\\Desktop\\doviz_featured2.xls")