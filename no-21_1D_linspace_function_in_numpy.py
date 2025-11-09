#1D linspace() in numpy
#linspace() Function is used to create an array in numpy with evenly spaced numbers between a start point and stop point.
'''start --> It represents starting elements
   stop --> It represents stop elements
   num --> It represents number of parts the elements should be devided.Default is 50.It must be positive.
   endpoint --> If True, stop is last element. If false stop is not included.

Syntax:

from numpy import*
array_name = linspace(start, stop, num=50, endpoint=True)

'''

#Creating numpy array using linspace() Function.
'''from numpy import*
a1 = linspace(1,8)
a2 = linspace(1,8,num=5)
a3 = linspace(1,8,5)         Here a2 and a3 are same
a4 = linspace(1,8,5,True)    Here a4 and a5 are same
a5 = linspace(1,8,5)'''

#Accessing 1D array elements
from numpy import*
a = linspace(1,8,5)
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

print()

#Accessing using for loop
#without index
print("Accessing by for loop but without index")
from numpy import*
a = linspace(1,10,5)
for i in a:
    print(i)
print()

#Accessing using for loop
#without index
print("Accessing by for loop with index")
import numpy as np
a = np.linspace(1,8,5)
n = len(a)

for i in range(n):
    print("index:",i, "=", a[i])
print()

#Accessing using while loop
#without index
print("Accessing by while loop with index")
from numpy import*
value = linspace(1,15,5)

n = len(value)
i = 0

while i<n:
    print("index:", i, "=", value[i])
    i+= 1
print()