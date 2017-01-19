import numpy as np

#Defining arrays

A1 = np.array([1,2,3,4])  # An array of integrs
A2 = np.array([1.2,3.2,4.5,1.7]) #an array of floats
A3 = np.array(["John", "Carlo","Gianluca","paolo"]) #an array of strings
A4 = np.array([True,False,False,True]) #an array of booleans

# you could clearly have defined the list before
L5 = [4,5,6,7]
A5 = np.array(L5)

A1.dtype
A2.dtype
A3.dtype
A4.dtype


# numpy arrays can just have one type!!!
L6 = ["Paolo", "Sara", 256, True, 13.14]
A6 = np.array(L6)
A6.dtype

L7 = [1,3,4.5, 9]
A7= np.array(L7)
A7.dtype

# extracting an elemenet by position
A1[0]
A3[1]
A4[2:]
A7[1]

for name in A3:
    print name


# So why do we really need Numpy arrays ?!? Vectorized Operation!
#of course just for integers and floats 
L1 = [1,2,3,4,5]
L2 = [11,12.1,13,14,15]

L3= L1+L2

a1=np.array(L1)
a2= np.array(L2)
a3= a1+a2
a4=a1-a2
a5=(a2)/a1


#multiplying by a constant
# A list:
C= 10
L=[1,2,3,4]
L2=C*L

#an Np array:!
A6 = np.array(L)
A7= A6*C

# How to apply it to the RLF method
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

# logical arrays:
#How to Build one:

A8 = np.array([2,3,5,10])
AL1 = A8 >5
AL2= A8 < 5
Al3 = np.array([True,False,False,True])


#Logical Operations in Python:
# and : &
# or : | 
# not:~

AL4 = AL1 & AL2
AL5 = AL1 |  AL2

#  Using index arrays

A10 = np.array([7,8,9,10])
AL = np.array([True,False,False,True])
print A10[AL]

Age= np.array([18, 25,14, 35, 29,13,38])
Income_k = np.array([0,18,0,25,22,0,40])

income_mean = Income_k[Age > 18].mean()


# for the case of RLF 
indexes_wall = Opaque_items_array=="wall" 
indexes_door = Opaque_items_array=="door"

indexes = indexes_door | indexes_wall
OurOutCome = Opaque_QHeating_array[indexes].sum()

#• for the case of resistances:
    
resistance_names = np.array(["R1","R2","R3","R4","R5"])
resistances_types = np.array(["conv","cond","cond","cond","conv"])
resistances_h = np.array([10,None,None,None,25])
resistances_k=  np.array([None,0.8,1.5,0.05,None])clear
resistances_L= np.array([None,0.5,0.3,0.6,None])
Resistances_RValues= np.array(np.zeros(5))
Resistances_RValues[resistances_types=="cond"] = resistances_L[resistances_types=="cond"]/ resistances_k[resistances_types=="cond"]
Resistances_RValues[resistances_types=="conv"] = 1.0 / resistances_h[resistances_types=="conv"]
Resistances_Rtot=Resistances_RValues.sum()


#but what if we want to define it in 2D

# so let's see how to define 2D Matrixes
A1_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])

# how to obtain data:
element = A1_2D[2,1]

Resistance_parameter_matrix = np.array([resistances_h,resistances_k,resistances_L])

#what if we want to include the names:
Resistance_matrix = np.array([resistance_names,resistances_types,resistances_h,resistances_k,resistances_L,Resistances_RValues])
print Resistance_matrix[0,0]
print  Resistance_matrix[2,0]
# how to obtain data from it
Resistance_matrix[-1,:].sum()



A17[A17>5].mean()

AL2 = A17 < 12

AL3 = AL1 & AL2

A17[AL1 & AL2]

myListOfList = [[1,2,3],[4,5,6],[7,8,9]]
my2DArray = np.array(myListOfList)
myArray2D_2 = np.array([[5,15,12],[17,18,19],[51,45,61]])

myArray2D_2.sum()
print myArray2D_2.sum(axis = 1)










