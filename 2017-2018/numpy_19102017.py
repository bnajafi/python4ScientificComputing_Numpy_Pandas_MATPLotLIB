# Let's start with Numpy !!!!!


import numpy as np

L1 = [1,4,5] # Just a very normal list !!!
L2 = [5,6,8]  #another normal list !!!

L3 = L1+L2

A1 = np.array(L1)
A2 = np.array([1.0,5,6])

#Adding 
A3 = A1 + A2
#subtracting 
A4 = A1-A2
A5 = A1*A2
A6 = A1/A2
C = 25
A7 = A1*C

# what if I add two different types in an array 
someList = [1,5,"luca",3.6,True]
someList2 = [1,5,6.0,8]

A9 = np.array([someList])

A10 = np.array([someList2])





deltaT_heating = 24.8
opaque_list=["wall","roof","door"]
# how to name parameters: 
#opaque_item_list or opaqueItemList

opaque_items = np.array(opaque_list)
opaque_areas = np.array([144.0,200.0,2.2])
opaque_U = np.array([0.438,0.25,0.6])

opaque_HF = opaque_U*deltaT_heating
opaque_Q = opaque_HF*opaque_areas

A11 = np.array([8,15,25,9])

opaque_items == "door"

opaque_Q[False,False,True]