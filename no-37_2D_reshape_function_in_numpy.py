#reshape() Function
'''This function is used to change the shape of array.We can convert 1D array to 2D array or 3D array and vice versa.The new array should have the same number of elements as in the original array.
Syntax:- reshape(array_name, (n,r,c))
where,
array_name = It represents the name of the array whose elements to be converted.
n = n is the number of arrays in the resultant array.
r = r is the number of rows.
c = c is the number of columns.'''

#Converting 1D array to 2D array
from numpy import*
a = array([10,20,30,40,50,60])
b = reshape(a,(2,3))
print(a)
print(b)
print()

#Converting 1D array to 3D array
from numpy import*
a = array([1,2,3,4,5,6,7,8,9,10,11,12])
b = reshape(a,(2,3,2))
print(a)
print(b)
print()

#Converting 2D array to 1D array
import numpy as np
a = np.array([[10,11,12,13],
              [14,15,16,17]])
b = reshape(a,(8))
print(a)
print(b)
print()

#flatten() Method
'''This method is used to convert 2D or 3D array to 1D array
Syntax:- array_name.flatten()'''
import numpy as np
a = np.array([[1,2,3,4,5],
              [6,7,8,9,10]])
b = a.flatten()
print(a)
print(b)
