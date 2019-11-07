# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 07:54:58 2017

@author: behzad
"""
import matplotlib.pyplot as plt
plt.figure()
x = [1,2,3,4]
y1 = [1,4,9,16]
y2 = [1,8,27,64]

plt.plot(x,y1,label = "PowerOfTwo",color='r',marker = '*')
plt.plot(x,y2,label = "PowerOfthree",color = 'b',marker = 'd')
plt.legend()


plt.title("Just a random title")
plt.xlabel("my X axis")
plt.ylabel("my y axis")
plt.show()

orderedNumbers = [1,2,3]
CoolingPowerValues= [5600,2400,250]
ElementLabels= ["wall","ceiling","door"]

plt.bar(orderedNumbers,CoolingPowerValues,align="center")
plt.xticks(orderedNumbers,ElementLabels)

plt.ylabel("maximum load")
plt.xlabel("Opaque Element")


chosenColors = ["blue","red","green"]

plt.pie(CoolingPowerValues,labels=ElementLabels,colors=chosenColors)


#NOw let's see scatter
import numpy as np
N= 50
x=np.random.rand(N)
y=np.random.rand(N)
ourChosenColors=np.random.rand(N)
random_radius_1= np.random.rand(N)
random_areas=np.pi*(15*random_radius_1)**2

plt.scatter(x,y,c=ourChosenColors,s=random_areas)

