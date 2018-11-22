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


resistance_names = ["R1","R2","R3","R4","R5"]
resistances_types = ["conv","cond","cond","cond","conv"]
resistances_h = [10,None,None,None,25]
resistances_k=  [None,0.8,1.5,0.05,None]
resistances_L= [None,0.5,0.3,0.6,None]
resistances_RValues=[0,0,0,0,0]

resistances_ListOfLists  = [resistances_types,resistances_h,resistances_k,resistances_L,resistances_RValues]

resistances_DataFrame = pd.DataFrame(resistances_ListOfLists,index=["type","h","k","L","Rvalues"], columns=resistance_names)

#Second Way:
#resistances_DataFrame2=pd.DataFrame({"types":resistances_types,"h":resistances_h})
print resistances_DataFrame.iloc[0]
print resistances_DataFrame.loc['type',"R1"]
print resistances_DataFrame['R1']
print resistances_DataFrame.iloc[1, 3]

resistances_DataFrame.loc["Rvalues"][resistances_DataFrame.loc["type"]=="conv"]=1.0/resistances_DataFrame.loc["h"][resistances_DataFrame.loc["type"]=="conv"]
resistances_DataFrame.loc["Rvalues"][resistances_DataFrame.loc["type"]=="cond"]=resistances_DataFrame.loc["L"][resistances_DataFrame.loc["type"]=="cond"]/resistances_DataFrame.loc["k"][resistances_DataFrame.loc["type"]=="cond"]

    

