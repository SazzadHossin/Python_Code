#Multi Dimensional array = The 2D arrays, 3D arrays, etc are called multidimensional array.

#Two D Numpy array using array () Function
'''If an array contains more than 1 row and 1 column that is known as Two dimensional array. It is also known as array of arrays'''

'''ways of creating Multi-D Array in numpy
   array() Function
   zeros() Function
   ones() Function
   reshape() Function'''

#array()Function: 
'''array()Function of numpy is used to create a multi dimensional array.
Syntax:- numpy.array(object,dtype=None,copy=True,order='K',subbok=Flase,ndim=0)
'''


#Creating 2D array using array() Function
'''import numpy as np
a = np.array([[10,20,30,40],[50,60,70,80]])
b = np.array([[10,11,12,13,13],
              [15,16,17,18,19],
              [20,21,22,23,24]])'''

#Accesssing 2D array elements
#no-1
from numpy import*
a = array([[10,20,30,40,50],
           [60,70,80,90,100]])

print(a)
print(a.dtype)

print()

#no-2
import numpy as np
val = np.array([[5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])
print(val[0][0])
print(val[0][1])
print(val[0][2])
print(val[0][3])
print(val[1][0])
print(val[1][1])
print(val[1][2])
print(val[1][3])
print(val[2][0])
print(val[2][1])
print(val[2][2])
print(val[2][3])

print()

#no-3
import numpy as np
val = np.array([[5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]], dtype=float)
print(val[0][0])
print(val[0][1])
print(val[0][2])
print(val[0][3])
print(val[1][0])
print(val[1][1])
print(val[1][2])
print(val[1][3])
print(val[2][0])
print(val[2][1])
print(val[2][2])
print(val[2][3])

print()

#no-4
import numpy as np
val = np.array([[5,6,7,8],
                [9,10,11.8,12],
                [13,14,15,16]])
print(val[0][0])
print(val[0][1])
print(val[0][2])
print(val[0][3])
print(val[1][0])
print(val[1][1])
print(val[1][2])
print(val[1][3])
print(val[2][0])
print(val[2][1])
print(val[2][2])
print(val[2][3])

print()

#no-5
import numpy as np
val = np.array([["Sabbir","Ovi","Riyad","Rafi"],
                ["Mehedi","Tashrif","Minhaj","Tanjil"]])
print(val)
print(val.dtype)
print(val[0][0])
print(val[0][1])
print(val[0][2])
print(val[0][3])
print(val[1][0])
print(val[1][1])
print(val[1][2])
print(val[1][3])

#Modifying 2D array elements
