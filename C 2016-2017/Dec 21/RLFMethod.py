# -*- coding: utf-8 -*-
import sys
import os
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory)
print os.getcwd()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp


#Inputs:
    
Latitude = 45
Location_deltaTCooling = 7.9
location_deltaTHeating = 24.8
location_DRcooling= 11.9

  

# Let's start creating a table for windows:
# Cooling
windows_DataFrame = pd.read_csv("windows.csv",sep=";",index_col= 0)
windows_DataFrame["Tx"]["east"]
windows_DataFrame["Area"] = windows_DataFrame["Height"]*windows_DataFrame["width"]

windows_DataFrame.to_csv("windows_completed.csv",sep =";")


C_value= Location_deltaTCooling-0.46*location_DRcooling
C_value_vector = C_value*np.ones(4)
windows_DataFrame["C_value"]  = C_value_vector

DF_IAC_cl = pd.read_csv("IAC_cl.csv",sep = ";",index_col=1)
IAC_cl_value= DF_IAC_cl["DrapesLightOpen"]["5c"]

#Now let's define it as a function
def IAC_CL_finder(windowID,IntShadingID):
    DF_IAC_cl = pd.read_csv("IAC_cl.csv",sep = ";",index_col=1)
    IAC_cl_value= DF_IAC_cl[IntShadingID][windowID]
    return IAC_cl_value
    
IAC_CL_finder("5c","DrapesLightOpen") #check
IAC_values=[]
for index in windows_DataFrame.index.tolist():
    print index
    IAC_values = np.append(IAC_values,IAC_CL_finder(windows_DataFrame["Window_ID"][index],windows_DataFrame["IntShading_ID"][index]))
    
windows_DataFrame["IAC_cl"] = IAC_values

windows_DataFrame["IAC"] = 1.0+(windows_DataFrame["IAC_cl"]-1.0)*windows_DataFrame["IntShading_closeness"]

windows_DataFrame.to_html("windowsInf.html")

 #Beam Irradiance
BeamIrradianceFile = "BeamIrradiance.csv"
df_BeamIrradiance = pd.read_csv(BeamIrradianceFile,sep=";",index_col=0)
print(df_BeamIrradiance)
result=df_BeamIrradiance["30"]
df_BeamIrradiance.loc["N"]["30"]

name_of_columns=df_BeamIrradiance.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)


ED=sp.interp(Latitude,name_of_columns_as_numbers,df_BeamIrradiance.loc["S"])

 #Diffuse Irradiance
DiffuseIrradiaceFile = "DiffuseIrradiance.csv"
df_DiffuseIrradiance = pd.read_csv(DiffuseIrradiaceFile,sep=";",index_col=0)
print(df_DiffuseIrradiance)
result=df_DiffuseIrradiance["30"]
df_DiffuseIrradiance.loc["N"]["30"]

name_of_columns=df_DiffuseIrradiance.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)

Ed=sp.interp(Latitude,name_of_columns_as_numbers,df_DiffuseIrradiance.loc["S"])

SLF_file = "SLF.csv"
df_SLF = pd.read_csv(SLF_file,sep=";",index_col=0)
print(df_SLF)
name_of_columns_SLF=df_SLF.columns.get_values()
name_of_columns_SLF_as_numbers = name_of_columns.astype(np.int32, copy=False)
SLF=sp.interp(Latitude,name_of_columns_SLF_as_numbers,df_SLF.loc[windowDirection])

Fshd = min([1,max([0,((SLF*window_OverhandDepth-window_OverhangDistance)/window_height)])])
Et=Ed+ED*(1-Fshd)
print "maximum total Irradiance value is: "+str(Et)


# exterior attachment 
if ExteriorAttachment =="None":
    Tx = 1
elif ExteriorAttachment =="ExteriorInsectScreen":
    Tx = 0.64
else:
    Tx = 1
    print "Warning *  Exterior Attachment type was not known,, I considered Tx to be Tx = 1."
PXI = Tx*Et

IAC_file = "IAC_cl.csv"
df_IAC= pd.read_csv(IAC_file,sep=";")
print(df_IAC)

ChosenRow_Type_IAC = df_IAC["Type"] == windowType
ChosenRow_ID_IAC = df_IAC["ID"] == windowID
if ChosenRow_Type_IAC.any():
    ChosenRow_IAC = ChosenRow_Type_IAC
elif ChosenRow_ID_IAC.any():
    ChosenRow_IAC = ChosenRow_ID_IAC
else:
    windowType = "clear_1Layer"
    print "your input for this window is not included in the library I considered it to be clear_1Layer"
    ChosenRow_Type_IAC = df_IAC["Type"] == windowType
    ChosenRow_IAC
    
    
 

if windowType in list(availableWindowTypes):
    if (windowInternalShadingType in availableWinowInternalShadingTypes):
        IAC_cl = float(df_IAC[df_IAC["Type"] == "clear_1Layer"][windowInternalShadingType])
    else:
        windowInternalShadingType = "DrapesLightOpen"
        IAC_cl = df_IAC.loc[windowType][windowInternalShadingType]      
 
elif windowID in list(availableWindowIDs):
    if (windowInternalShadingType in availableWinowInternalShadingTypes):
        IAC_cl = df_IAC.loc[windowID][windowInternalShadingType]
    else:
        windowInternalShadingType = "DrapesLightOpen"
        IAC_cl = df_IAC.loc[windowID][windowInternalShadingType]      
