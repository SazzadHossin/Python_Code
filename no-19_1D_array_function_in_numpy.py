#One Dimensional Array

'''Single row multiple column.
   EX: [101,102,103,104,105]

Ways of createing numpy array:
1.array()Function
2.linespace()Function
3.logspace()Function
4.arange()Function
5.zeros()Funtion
6.ones()Functions
'''

#array()Function: array()Function of numpy is used to create an array.
import numpy as np
stu_roll = np.array([101,102,103,104,105])
print(stu_roll)
print(type(stu_roll))
print(stu_roll.dtype)
##indexing
print("Asseccing 1D array elements")
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

print()

#Modify 1D array
from numpy import*
roll = array([101,102,103,104,105])
roll[1] = 111
print(roll)
