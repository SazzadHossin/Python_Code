#1D arange() Function in numpy
#arange() Function is used to create an array with a group of elements from start to one element prior to stop in steps of stepsize.
'''Syntax:
    numpy.arange(start, stop, stepsize, dtype=none)
Where,
start = Start of interval.The interval includes this value.The default start value is 0.
stop = End of interval.The interval does not include this value,except in some cases where step is not an integer and floating point round-off affects the length of out.
stepsize = Spacing between values.The default stepsize is 1.
dtype = The type of output array.
'''

#Creating array using arange() Function
'''from numpy import*
array_name = arange(start, stop, stepsize, dtype=none)
a = arange(1,5)
a = arange(1,5,1)'''

#no-1
import numpy as np
a = np.arange(1,10)
print(a)

print()

#no-2
from numpy import*
val = arange(1,10,2)
print(val)

#Accessing 1D arange() Funtion elements
#no-3
from numpy import*
a = arange(1,5)
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])

print()

#Accessing 1D arange() Funtion elements using for loop
#without index
#no-4
from numpy import*
a = arange(1,10)
for element in a:
    print(element)

print()


#with index
#no-5
from numpy import*
a = arange(2,20,2)
n = len(a)
for i in range(n):
    print("index:",i,"=",a[i])

print()

#Accessing 1D arange() Funtion elements using while loop
#no-6
import numpy as np
val = np.arange(1,30,3)
n = len(val)
i = 0

while i<n:
    print("index:",i,"=",val[i])
    i+=1

print()