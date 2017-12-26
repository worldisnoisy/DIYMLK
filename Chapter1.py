# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 12:40:29 2017

@author: hubert
"""
import pandas as pd

train_data = pd.read_csv('./Datasets/breast-cancer-train.csv')
print(train_data.describe())
train_negative = train_data.loc[train_data['Type'] == 0][['Clump Thickness','Cell Size']]
train_postive = train_data.loc[train_data['Type'] == 1][['Clump Thickness','Cell Size']]

import matplotlib.pyplot as plt
plt.scatter(train_negative['Clump Thickness'],train_negative['Cell Size'],s=200,c='red',marker='o')
plt.scatter(train_postive['Clump Thickness'],train_postive['Cell Size'],s=150,c='black',marker='x')
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
plt.show()