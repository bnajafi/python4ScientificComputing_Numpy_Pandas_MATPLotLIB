#!/usr/bin/env python
# coding: utf-8

# # Numpy
# Numy, apart from all other features, provides us with the possibility of running our procedures using vectorized operations
# First let's import numpy

# In[1]:


import numpy as np 


# ## Numpy arrays

# In[2]:


A1 = np.array([1,4,5,11])  #you should provide a list as the input argument


# In[3]:


A1


# How to check the data type of an array
# 

# In[6]:


A1.dtype


# In[4]:


A2 = np.array([1.0,4.2,5.0,11.1])


# In[5]:


A2


# In[7]:


A2.dtype


# In[8]:


listOfNames = ["benjamin", "francesco", "rafael", "santiago"]
A3 = np.array(listOfNames)


# In[9]:


A3.dtype


# In[10]:


A4 = np.array([True, False, True, False])
A4.dtype


# So we can see that every numpy array has a unique data type, but what would happen if I give it a list made up of different datatypes !
# 

# In[11]:


A5 = np.array([5,"francesco",1.2 ])


# In[12]:


A5


# It converts all of them into a single datatype !!!!

# In[13]:


A6= np.array([2.2,3,5])
A6


# In[15]:


A7 = np.array([2,True, 5])
A7


# In[16]:


A8 = np.array(["jack",2,True, 5])
A8


# This is a huge disadvantage ! and cmmon source of errors !
# but of course it is an awesome tool for vectorized operation

# In[21]:


L9 = [1.4,5.3,7.6]
L10 = [2.2,3.0,9.5]
L11 = L9+L10
L11


# So we saw that lists do not perform vectorized operations! numpy arrays come to help !

# In[23]:


A9 = np.array(L9)
A10=np.array(L10)
A11 = A9+ A10
A11


# In[28]:


A12 = A9 - A10
A12
A13 = A9*A10
A13


# For matrix multiplication you should use A.dot(B)

# multiplication with number, The list does not do what we want! we have to use numpy arrays !!

# In[29]:


L14 = [3,5,6]
L15 = 2*L14
L15


# In[30]:


A14 = np.array(L14)
A15 = 2*A14
A15


# In[55]:


opaque_item_list = ["wall", "ceiling", "door"]
opaque_item_array = np.array(opaque_item_list)
opaque_U_array = np.array([0.438,0.25, 1.78])
opaque_area_array = np.array([105.8,200,2.2])
T_inside_heating = 20
T_outside_heating =-4.8 
DeltaT_heating = T_inside_heating - T_outside_heating
opaque_HF_array  = opaque_U_array*DeltaT_heating
opaque_Q_Array = opaque_HF_array*opaque_area_array
print("opaque HF Values")
print(opaque_HF_array)
print("the laod of each component")
print(opaque_Q_Array)


# In[34]:


opaque_Q_Array_rounded = np.round(opaque_Q_Array,2)
opaque_Q_Array_rounded


# How to extract items from numpy arrays 

# In[36]:


Q_ceiling = opaque_Q_Array_rounded[1]
Q_ceiling


# In[38]:



opaque_Q_Array_rounded[-1] = 0
opaque_Q_Array_rounded


# ## The amazing logical arrays 

# In[39]:


TheONesMoreThan1200 = opaque_Q_Array_rounded > 1200
TheONesMoreThan1200


# Remember if you want t o use logial operators on numpy logical arrays you should use & for and , | for or 
# The alternative solution is to use logical_and , logical_or which are numpy function

# In[47]:


TheONesMoreThan1200LessThan1210 =(opaque_Q_Array_rounded > 1200) & (opaque_Q_Array_rounded < 1210) 
TheONesMoreThan1200LessThan1210


# In[44]:


TheONesMoreThan1200LessThan1210 =np.logical_and(opaque_Q_Array_rounded > 1200,opaque_Q_Array_rounded < 1210) 
TheONesMoreThan1200LessThan1210


# In[48]:


A15 = np.array([3,5,6,11])
A16 = A15 > 5
A16


# In[50]:


A17 = A15[A16]
A17


# You could also do this manually
# 

# In[54]:


A18 = A15[np.array([False,False,False, True])]
A18


# In[62]:


index_wall_arrray = opaque_item_array == "wall"
index_wall_arrray
Q_wall = opaque_Q_Array_rounded[index_wall_arrray]
Q_wall = Q_wall[0]
Q_wall


# In[63]:


Q_wall = opaque_Q_Array_rounded[opaque_item_array=="wall"][0]
Q_wall


# In[64]:


Q_wall_ceiling = opaque_Q_Array_rounded[(opaque_item_array =="wall") | (opaque_item_array== "ceiling")]
Q_wall_ceiling


# In[67]:


Q_tot_opaque = opaque_Q_Array.sum()
round(Q_tot_opaque,2)
Q_avg_opaque = opaque_Q_Array.mean()


# In[71]:


resistance_names = np.array(["R_internal","R_foam","R_wood","R_plaster","R_external"])
resistance_types = np.array(["conv","cond","cond","cond","conv"])
resistance_k = np.array([ None,0.05,0.4,1,None])
resistance_L = np.array([ None,0.06,0.1,0.01,None])
resistance_A = np.array([ 15,15,15,15,15])
resistance_h = np.array([ 8.9,None,None,None,20])


# In[72]:


resistance_RValues = np.zeros(5)
resistance_RValues


# In[ ]:





# In[75]:


resistance_L[resistance_types=="cond"]/ (resistance_k[resistance_types=="cond"]*resistance_A[resistance_types=="cond"])


# In[82]:


resistance_RValues[[resistance_types=="cond"]]=resistance_L[resistance_types=="cond"]/ (resistance_k[resistance_types=="cond"]*resistance_A[resistance_types=="cond"])
resistance_RValues[[resistance_types=="conv"]]=1.0/(resistance_h[resistance_types=="conv"]* resistance_A[resistance_types=="conv"])


# In[83]:


resistance_RValues

