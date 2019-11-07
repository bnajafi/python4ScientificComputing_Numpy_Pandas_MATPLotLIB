# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 10:01:37 2016

@author: behzad
"""
import pandas as pd 
S1 = pd.Series([1,2,3,4])
S2 = pd.Series([7,8,9,10])

S3 = S1+S2

S3[1]
S4 = pd.Series([7,8,9,10,12])
S5 = S4[2:4]

S6 = pd.Series([0.25,0.76,1.5,1.4],index = ["R1","R2","R3","R4"])
S6["R1"]

S7 = pd.Series([12,13,4],index=["a","b","c"])
S8 = pd.Series([5,6,7],index=["b","c","a"])
S9 = S7+S8

Qheating = pd.Series([1240,1500,200],index = ["wall","ceiling","door"])
Qheating.argmax()

# DataFrame
ListOFLists = [[1,2,3],[4,5,6],[7,8,9]]
DF1 = pd.DataFrame(ListOFLists,index=["index1","index2","index3"],columns =["column 1","column 2","column 3"])
print DF1.iloc[0]
print DF1.loc['type',"R1"]
print DF1['R1']
print DF1.iloc[1, 3]
