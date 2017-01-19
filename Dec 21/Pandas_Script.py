# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:29:24 2016

@author: behzad
"""

import pandas as pd
import numpy as np

S1= pd.Series([1,3,6,9])
S2=pd.Series([4,5,6,8])

S3=S1+S2
S4=S1-S2
S5 = S1 >3


# index arrays also work here!

print S2[S1>5]


# How to access elements in a panda series!:
    
# it can be similar to a list or an array: !
print S1[0]
print S1[1:3]

# Series functions:
S1.mean()
S2.median()
S1.sum()
S1.std()

# so each item has got an index or name!

# what if we do not define these indexes:

S6= pd.Series([1,3,6,9],["a","b","c","d"])
S6["c"]

# vector Operation

S7 = pd.Series([4,5,7,9],["d","b","a","c"])
S8= S6+S7



# useful functions 
# argmax and argmin
Q_Heating = pd.Series([1150,1240,124],index = ["Wall","ceiling","door"])
print Q_Heating.argmax()

# We could also define them using our previous numpy arrays
Opaque_items_list = ["wall","ceiling","door"]
Opaque_U_Heating_list = [0.438,0.25,2.273]
Opaque_netArea_list = [105.8, 200, 2.2]

Opaque_items_array = np.array(Opaque_items_list)
Opaque_U_heating_array= np.array(Opaque_U_Heating_list)
Opaque_netArea_array= np.array(Opaque_netArea_list)

T_inside_heating = 20
T_design_winter = -4.8

deltaT_heating = T_inside_heating-T_design_winter

Opaque_HF_array = Opaque_U_heating_array*deltaT_heating

Opaque_QHeating_array = Opaque_HF_array*Opaque_netArea_array

Q_Heating = pd.Series(Opaque_QHeating_array,index = Opaque_items_array)


# pandas apply function !!!
def tokW(inputValue):
    outputValue=inputValue/1000
    return outputValue
    
Q_Heating_kW = Q_Heating.apply(tokW)

# pandas DataFrames

OurDataFrame = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index=["index1","index2","index3"])
OurDataFrame2 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index=["index1","index2","index3"],columns=["column 1","column2","column3"])
R1=["conv",10,None,None,0]
R2=["cond",None,0.8,0.5,0]
R3=["cond",None,1.5,0.3,0]
R4=["cond",None,0.05,0.6,0]
R5=["conv",25,None,None,0]

resistances_ListOfLists = [R1,R2,R3,R4,R5]

resistances_DataFrame = pd.DataFrame(resistances_ListOfLists,index=["R1","R2","R3","R4","R5"], columns=["type","hconv","kcond","L","RValue"])

#Second Way:
#resistances_DataFrame2=pd.DataFrame({"types":resistances_types,"h":resistances_h})
print resistances_DataFrame.iloc[0]
print resistances_DataFrame.loc['R1',"hconv"]
print resistances_DataFrame['type']
print resistances_DataFrame.iloc[1, 3]

resistances_DataFrame["RValue"][resistances_DataFrame["type"]=="conv"]=1.0/resistances_DataFrame["hconv"][resistances_DataFrame["type"]=="conv"]
resistances_DataFrame["RValue"][resistances_DataFrame["type"]=="cond"]=resistances_DataFrame["L"][resistances_DataFrame["type"]=="cond"]/resistances_DataFrame["kcond"][resistances_DataFrame["type"]=="cond"]

# The first way of defininig a DataFrame 
DF2 = pd.DataFrame({"Resistance_name":["R1","R2","R3"],"Resistance_Type":["conv","cond","conv"],"resistance_value":[0.95,1.23,1.45]})

print(DF2.head(2))
print(DF2.tail(2))
DF3 = DF2.set_index("Resistance_name")
DF2.set_index("Resistance_name",inplace=True)


DF2["Resistance_Type"]

# what if we want two or more of them
DF2[["Resistance_Type","resistance_value"]] # so we should include two parantheses

L3 = DF2["Resistance_Type"].tolist()
