#1D ones() Function in numpy
'''ones() Function is used to create an array with all 1.
Syntax:
numpy.ones(shape,dtype=float,order='C')
where,
shape = shape of new array.It can be an int which will be represent number of elements or can be tuple of int. ex: 5, (5,) (3,1)
dtype = The desired data-type for the array.By default data type is float.
order = Whether to store multi-dimensional data in row-major (C-style) or column major (Fortran-style) order in memory. It can be C or F.'''

#Creating array using ones() Function
'''from numpy import*
array_name = ones(shape, dtype=float)
a = ones(5)
a = ones(5,dtype=int)
a = ones((3,2))'''

#no-1
from numpy import*
a = ones(5)
print(a)

print()

#no-2
import numpy as np
a = np.ones(10,dtype=int)
print(a)

print()

#Accessing 1D ones() Funtion elements
#no-3
from numpy import*
a = ones(5)
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

print()


#Accessing 1D ones() Funtion elements using for loop
#without index
#no-4
import numpy as np
val = np.ones(7)

for i in val:
    print(i)
print()

#with index
#no-5
from numpy import*
a = ones(10,dtype=int)
n = len(a)
for i in range(n):
    print("index:",i,"=",a[i])

print()

#Accessing 1D ones() Funtion elements using while loop
#no-6
import numpy as np
val = ones(7)
n = len(val)
i = 0
while i<n:
    print("index",i,"=",val[i])
    i+=1
print()