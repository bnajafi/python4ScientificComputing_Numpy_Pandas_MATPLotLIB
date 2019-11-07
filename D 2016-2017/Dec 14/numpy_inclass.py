# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 15:52:24 2016

@author: behzad
"""

import numpy as np

A1 = np.array([1,2,3,4])
A2 = np.array([1.1,1,2.3,4.5])
A3 = np.array(["paolo","sara", "matteo"])
A4 = np.array([True,False,False,True,True])

L = [2,3,4,5]
A5 = np.array(L)
L2 = ["pablo","juan", "alejandro"]
A6 = np.array(L2)

print A1.dtype
print A2.dtype
print A3.dtype
print A4.dtype

L3 = [12,35.5,"paolo",True]
A7 = np.array(L3)

# all of the elements of an array will have the same type
# if they are not already, they are converted

# another similarity, how to extract elements
print A1[2]
print A3[0]

#extracting a range of elements
print A2[1:]
print A2[1:3] #until a number! 

# similarity: loops!
for name in A3:
    print "Hi "+name + "!!"

L4 = [1,2,3]
L5 =[3,4,5]
L6 =L4+L5

A8 = np.array(L4)
A9 = np.array(L5)
A10 = A8+A9

C= 10
L7 = L4*C

A11 = A8*C

A12 = A8*A9
A13 = np.array([150.2,250.1,140.2])

A14 =A13/A12


# How to apply it to the RLF method
Opaque_items_list = ["wall","ceiling","door"]
Opaque_U_Heating_list = [0.438,0.25,1.694]
Opaque_netArea_list = [105.8, 200, 2.2]

Opaque_items_array = np.array(Opaque_items_list)
Opaque_U_heating_array= np.array(Opaque_U_Heating_list)
Opaque_netArea_array= np.array(Opaque_netArea_list)

T_inside_heating = 20
T_design_winter = -4.8

deltaT_heating = T_inside_heating-T_design_winter

Opqaue_HF_array = Opaque_U_heating_array*deltaT_heating
Opqaue_QHeating_array = Opqaue_HF_array*Opaque_netArea_array
Qheating_of_walls = Opqaue_QHeating_array[Opaque_items_array =="wall"]
Opaque_QHeating_tot = Opqaue_QHeating_array.sum()
# you should also try min, max, mean,...
#U_myWindow = U_array[windowName_array == window_name_iput]
 
# another useful feature!! Index Arrays!!!!
A15 =  A12 > 7
A12 == 3

# let's see index arrays!! 

Abool1  = np.array([True,False,True]) 
A16 = A12[Abool1]


age  = np.array([26,14,23,18,29,35])
income_k = np.array([22,0,18,0,30,44])

income_average = income_k[age > 20 ].mean()

# how can this be usefull !!

resistance_names = np.array(["R1","R2","R3","R4","R5"])
resistances_types = np.array(["conv","cond","cond","cond","conv"])
resistances_h = np.array([10,None,None,None,25])
resistances_k=  np.array([None,0.8,1.5,0.05,None])
resistances_L= np.array([None,0.5,0.3,0.6,None])
Resistances_RValues= np.array(np.zeros(5))
Resistances_RValues[resistances_types=="cond"]=resistances_L[resistances_types=="cond"]/resistances_k[resistances_types=="cond"]
Resistances_RValues[resistances_types=="conv"]=1.0/resistances_h[resistances_types=="conv"]
Resistances_Rvalues_tot = Resistances_RValues.sum()

A17 = np.array([2,3,5,10,12,13,4])
AL1 = A17 >5

A17[A17>5].mean()

AL2 = A17 < 12

AL3 = AL1 & AL2

A17[AL1 & AL2]

myListOfList = [[1,2,3],[4,5,6],[7,8,9]]
my2DArray = np.array(myListOfList)
myArray2D_2 = np.array([[5,15,12],[17,18,19],[51,45,61]])

myArray2D_2.sum()
print myArray2D_2.sum(axis = 1)

Resistance_parameter_matrix = np.array([resistances_h,resistances_k,resistances_L])

#what if we want to include the names:
resistance_names = np.array(["R1","R2","R3","R4","R5"])
resistances_types = np.array(["conv","cond","cond","cond","conv"])
resistances_h = np.array([10,None,None,None,25])
resistances_k=  np.array([None,0.8,1.5,0.05,None])
resistances_L= np.array([None,0.5,0.3,0.6,None])
Resistances_RValues= np.array(np.zeros(5))
Resistance_matrix = np.array([resistance_names,resistances_types,resistances_h,resistances_k,resistances_L,Resistances_RValues])


