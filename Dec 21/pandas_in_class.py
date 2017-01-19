# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 10:01:37 2016

@author: behzad
"""
import numpy as np
import pandas as pd 
import scipy as sp
S1 = pd.Series([1,2,3,4])
S2 = pd.Series([7,8,9,10])

S3 = S1+S2
print S3

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

DF1 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])

DF2 = pd.DataFrame([[1,20,32,67],[4,55,61,89],[74,82,95,23]],index=["sample 1","sample 2","sample 3"],columns = ["prop 1","prop 2","prop 3","prop 4"])
employees = pd.DataFrame([[26,3,27000],[30,4,28000],[40,10,35000],[24,1,23000],[55,15,40000]],columns = ["age","experience","salary"],index= ["Paolo", "sara","stefano", "andrea","matteo"])

print employees["age"] #to extract using column name
print employees.loc["stefano"] #to extract using index
#print employees.loc["stefano"]["experience"]#to extract using index
print employees.loc["stefano","experience"]#to extract using index

print employees["salary"]
print employees.loc["andrea","salary"]
print employees.iloc[1,2]
print employees.iloc[3]
print employees.iloc[:,2]

# Now Charles elie asks how to extract the length of indices or columns
print employees.index.tolist()
print employees.columns.tolist()
print len(employees.index.tolist())

#saddam asked us how to convert Series into lists
print employees.iloc[3].tolist()
DF1 = pd.DataFrame(ListOFLists,index=["index1","index2","index3"],columns =["column 1","column 2","column 3"])
print DF1.iloc[0]
print DF1.loc['type',"R1"]
print DF1['R1']
print DF1.iloc[1, 3]

R1=["conv",10,None,None,0]
R2=["cond",None,0.8,0.5,0]
R3=["cond",None,1.5,0.3,0]
R4=["cond",None,0.05,0.6,0]
R5=["conv",25,None,None,0]

resistances_listOFLists = [R1,R2,R3,R4,R5]
resistance_DF = pd.DataFrame(resistances_listOFLists,index=["R1","R2","R3","R4","R5"],columns = ["type","hconv","kcond","L","RValue"])
resistance_DF["RValue"]

print resistance_DF["type"] == "conv"
print resistance_DF["type"] == "cond"
condition_conv = resistance_DF["type"] == "conv"
resistance_DF["hconv"][condition_conv]

RValues_conv = 1.0/resistance_DF["hconv"][condition_conv]
resistance_DF["RValue"][condition_conv] = RValues_conv


resistance_DF["RValue"][ resistance_DF["type"] == "conv"] = 1.0/ resistance_DF["hconv"][ resistance_DF["type"] == "conv"]

condition_cond = resistance_DF["type"] == "cond"
resistanceValues_cond = resistance_DF["L"][condition_cond]/resistance_DF["kcond"][condition_cond]

resistance_DF["RValue"][condition_cond] = resistanceValues_cond

Rtot_wall = resistance_DF["RValue"].sum()


# The second way of defininig a DataFrame 

DF4 = pd.DataFrame({"name":["R1","R2","R3","R4","R5"],
"type":["conv","cond","cond","cond","conv"],
"hconv": [10,None,None,None,25],"kcond":[None,0.8,1.5,0.05,None],
"L":[None,0.5,10.3,0.6,None],"RValue":[0,0,0,0,0]})

# how to see !! the first two lines or the last two
DF4.head(2)
DF4.tail(2)

DF4.set_index("name",inplace=True) # Pay attention that inplace= True kinda saves this modification!!
import os
os.chdir("C:/Users/behzad/Dropbox/_2_Teaching Activities/POLIMI 2016-2017 Energy and Environmental Technolgoies for Building Systems/3 Python Files/Dec 21")
window_DF  = pd.read_csv("windows.csv",sep = ";")
window_DF.set_index("Name",inplace=True)
window_DF["Area"] =[0,0,0,0]
window_DF["Area"] = window_DF["width"]*window_DF["Height"]
window_DF.to_html("mywindows.html")
window_DF.to_csv("windows_modified.csv") # this is acutally ho w you save it !!!

#Inputs:
    
Latitude = 45
Location_deltaTCooling = 7.9
location_deltaTHeating = 24.8
location_DRcooling= 11.9

C_value = Location_deltaTCooling - 0.46*location_DRcooling
window_DF["C_value"] = C_value

# if you want drop a specific column you acn use:
#window_DF.drop("nameOf the column",axis=1)    

# now I want to see how to read from Tables !!!!
IAC_cl_DF = pd.read_csv("IAC_cl.csv",sep = ";",index_col = 1)
myValue = IAC_cl_DF["RollerOpaqueDark"]["1c"]
myValue2 = IAC_cl_DF.loc["1c","RollerOpaqueDark"]

DF_IAC_cl = pd.read_csv("IAC_cl.csv",sep = ";",index_col=1)
IAC_cl_value= DF_IAC_cl["DrapesLightOpen"]["5c"]

def IAC_cl_finder(window_ID,shading_ID):
    DF_IAC_cl = pd.read_csv("IAC_cl.csv",sep = ";",index_col=1)
    IAC_cl_value= DF_IAC_cl[shading_ID][window_ID]
    return IAC_cl_value
    
IAC_cl_finder("5c","DrapesLightOpen")
IAC_cl_values = []
for index in window_DF.index.tolist():
    #print "i am now checking out "+index
    #print "here is my window ID!!: "+window_DF["Window_ID"][index]
    #print "here is my window's internalShading_ID!! :  "+ window_DF['IntShading_ID'][index]
    print IAC_cl_finder(window_DF["Window_ID"][index],window_DF['IntShading_ID'][index])
    IAC_values=np.append(IAC_cl_values,IAC_cl_finder(window_DF["Window_ID"][index],window_DF["IntShading_ID"][index]))
    #print IAC_cl_values
    
window_DF["IAC_cl"] = IAC_cl_values

window_DF.columns.tolist() 

window_DF["IAC"]  = 1.0+window_DF['IntShading_closeness']*(window_DF["IAC_cl"]-1.0)


 #Beam Irradiance
BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
BeamIrradiance_DF.columns.tolist()
BeamIrradiance_DF["45"]["E"]
latitude = 45
direction = "S"
input_vector_strings = BeamIrradiance_DF.columns.get_values()
input_vector_numbers=input_vector_strings.astype(np.int32,copy=False)
output_vector_number = BeamIrradiance_DF.loc[direction]
myValue = sp.interp(latitude,input_vector_numbers,output_vector_number)
 
BeamIrradianceFile = "BeamIrradiance.csv"
df_BeamIrradiance = pd.read_csv(BeamIrradianceFile,sep=";",index_col=0)
print(df_BeamIrradiance)
result=df_BeamIrradiance["30"]
df_BeamIrradiance.loc["N"]["30"]

name_of_columns=df_BeamIrradiance.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)


ED=sp.interp(Latitude,name_of_columns_as_numbers,df_BeamIrradiance.loc["S"])