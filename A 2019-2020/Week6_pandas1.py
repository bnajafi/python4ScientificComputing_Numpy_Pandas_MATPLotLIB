#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# ## Pandas Series !
# A 1D array in numpy was called array !, which in pandas it is called a Series

# In[4]:


S1 = pd.Series([1,2,3,4])
S2 = pd.Series([4,5,6, 0.1])
print(S2)


# The vectorized operations are exactly like numpy arrays !!

# In[6]:


S3 = S1+S2
S4 = S1-S2
print(S3)


# You can also create logical Series (boolean)

# In[8]:


S5 = S1>S2
print(S5)


# You can also use the awesome logical indexing in pandas (similar to numpy)
# 

# In[9]:


S2[3]
S2[pd.Series([False,True,True,False])]


# In[ ]:


S1[S1>S2]


# The awesome thing about pandas is that you can give names to elements (we call them indexes)

# In[11]:


S6 = pd.Series([1,3,6,9],["a","b","c","d"])


# In[13]:


print(S6)


# Let's define a vector S7 that is using similar indexes but with a different order 

# In[15]:


S6 = pd.Series([1,3,6,9],["a","b","c","d"])
S7 = pd.Series([4,5,7,9], ["d","b","c","a"])
S8 = S6+S7
print(S8)


# We can observe that it considers the indexes not the order !! that is a nice advantage !!

# Let's solve out problem using this advantage

# In[17]:


Q_heating = pd.Series([1150,1240,124], index= ["wall","ceiling", "door"])
print(Q_heating)


# Pay attention that you can create a pandas Series either like this:
# Q_heating = pd.Series([1150,1240,124], ["wall","ceiling", "door"])
# 
# or like this:
# 
# Q_heating = pd.Series([1150,1240,124], index= ["wall","ceiling", "door"])
# 
# Clearly, the second option is better because it is easier to understand
# 

# Furhtermore, you can define a pandas Series by providing a dictionary as the input
# 
# Pandas_series = pd.Series(youDictionary)
# 

# In[19]:


Q_heating_dict = {"walls":1150,"ceiling":1240,"door":124}
Q_heating = pd.Series(Q_heating_dict)
print(Q_heating)


# The fact that we have indexes in pandas Series means that we can use them to extract the elements !

# In[21]:


Q_door = Q_heating["door"]
print(Q_door)


# You can also concert numpy arrays into pandas Series

# In[24]:


opqaue_item_array  = np.array(["wall","ceiling","door"])
opaque_U_array = np.array([0.438,0.25,1.78])
opaque_area_array = np.array([105.8,200,2.2])
T_inside_heating = 20
T_outside_heating = -4.7
DeltaT_heating= T_inside_heating - T_outside_heating
opaque_HF_array = DeltaT_heating * opaque_U_array
opaque_Q_array = opaque_HF_array*opaque_area_array
Q_heating = pd.Series(opaque_Q_array, index= opqaue_item_array)
Q_heating["wall"]


# Clearly, we could do the whole process using Pandas Series, as follows:
# 

# In[27]:


opaque_U = pd.Series([0.438,0.25,1.78], index = ["wall","ceiling","door"])
opaque_area = pd.Series([105.8,200,2.2], index = ["wall","ceiling","door"] )
temperatures = pd.Series([20,-4.8], index=["T_inside_heating","T_outside_heating"])
opaque_HF = opaque_U * (temperatures["T_inside_heating"]-temperatures["T_outside_heating"])
opaque_Q = opaque_HF*opaque_area
print(opaque_Q)


# ## applying a function to Series
# you can use pandas .apply function to apply a function to Series!

# In[30]:


def toKw(inputValue):
    outputValue = inputValue/1000
    return outputValue

Q_heating_kw = Q_heating.apply(toKw)
print(Q_heating_kw)


# ## Pandas DataFrames !
# Using Pandas DataFrames you can define 2 D matrixes, each column in this matrix can have a different datatype !

# In[32]:


resistance_names = ["R1","R2","R3","R4","R5"]
resistances_types = ["conv","cond","cond","cond","conv"]
resistances_h = [10,None,None,None,25]
resistances_k=  [None,0.8,1.5,0.05,None]
resistances_L= [None,0.5,0.3,0.6,None]
resistances_RValues=[0,0,0,0,0]
resistance_listofLists = [resistances_types,resistances_h,resistances_k,resistances_L,resistances_RValues]


# In[33]:


resistances_DF = pd.DataFrame(resistance_listofLists,
                              index=["type","h","k","L","RValue"], 
                              columns = ["R1","R2","R3","R4","R5"])
print(resistances_DF)


# LEt me transpose it (which means changing the columsn with rows) so that each item would be a row and each property would be columns

# In[35]:


resistances_DF2 = resistances_DF.transpose()
print(resistances_DF2)


# ### Extracting data from DataFrames
# #### using iloc (number)
# 

# In[36]:


resistances_DF2.iloc[1,2]


# In[38]:


resistances_DF2.iloc[3,3]


# In[39]:


resistances_DF2.iloc[0,:]


# In[41]:


resistances_DF2.iloc[:,-1]



# In[42]:


resistances_DF2.iloc[2,:]



# In[ ]:





# ### .loc[] Extracting elements using their name !!
# We do not like the numbers in pandas !
# 

# In[43]:


resistances_DF2.loc["R3","k"]


# In[44]:


resistances_DF2.loc["R3",:]


# In[45]:


resistances_DF2.loc["R3"]



# **Note** For extracting columsn you do not need .loc

# In[46]:


resistances_DF2["h"]


# In[ ]:





# Now let's do the calculation

# In[47]:


resistances_DF2


# In[51]:


resistances_DF2["type"]=="conv"


# In[58]:


1.0/resistances_DF2[resistances_DF2["type"]=="conv"]["h"]



# In[59]:


resistances_DF2[resistances_DF2["type"]=="conv"]["RValue"]


# In[62]:


resistances_DF2.loc[resistances_DF2["type"]=="conv","RValue"] = 1.0/resistances_DF2.loc[resistances_DF2["type"]=="conv","h"]
resistances_DF2





