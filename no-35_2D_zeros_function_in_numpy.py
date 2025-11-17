#zeros() Function in 2D array
'''zeros() Function is used to create an array with all zeros.
Syntax:
numpy.zeros(shape,dtype=float,order='C')
where,
shape = shape of new array.It can be an int which will be represent number of elements or can be tuple of int. ex: (3,1)
dtype = The desired data-type for the array.By default data type is float.
order = Whether to store multi-dimensional data in row-major (C-style) or column major (Fortran-style) order in memory. It can be C or F.'''

#Creating 2D array using zeros() function
#no-1
from numpy import*
a = zeros((3,2))
print(a)

print()

#no-2
from numpy import*
a = zeros((3,3), dtype=int)
print(a)

#Accessing 2D arrays elements
#no-3
import numpy as np
a = zeros((3,2), dtype=int)
print(a)
print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])
print(a[2][0])
print(a[2][1])

print()

#Accessing 2D arrays elements using for loop
#without index
#no-4
from numpy import*
a = zeros((3,3),dtype=int)

for row in a:
    for column in row:
        print(column)
    print()
print()

#with index
#no-5
import numpy as np
a = np.zeros((4,4), dtype=int)
n = len(a)

for i in range(n):
    for j in range(len(a[i])):
        print("index:", i, j, "=",a[i][j])
    print()
print()

#Accessing 2D arrays elements using while loop
#no-6
from numpy import*
val = zeros((5,4), dtype=int)
n = len(val)
i = 0

while i<n:
    j = 0
    while j<len(val[i]):
        print("index:",i,j,"=",val[i][j])
        j+=1
    i+=1
    print()
print()