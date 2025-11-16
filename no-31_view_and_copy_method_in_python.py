#View() and Copy Method in Python

#View Method
'''This method is used to construct a new view of array with same data of existing array.The existing array and new array will share different memeory locations.
If the new array get modified,the existing will also be modified as the elements in both the arrays will be like mirror image.'''
import numpy as np
a = np.array([10,20,30,40,50])
b = a.view()
a[1] = 80
b[4] = 500
print(a)
print(b)
print('a', id(a))
print('b', id(b))

print()

#Copy Method
'''This method is used to create a copy of an existing array.If the new array get modified the existing array will not be affected or vice versa.Both array are independent.'''
from numpy import*
a = array([101,102,103,104,105])
b = a.copy()
a[2] = 500
b[1] = 200
print(a)
print(b)
print('a', id(a))
print('b', id(b))