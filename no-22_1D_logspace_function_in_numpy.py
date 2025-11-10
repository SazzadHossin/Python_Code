#1D logspace() Function in numpy
#logspace() Funtion is used to create an array with evenly spaced numbers logarithmically.The sequence starts at base ** start (base to the power of start) and ends with base ** stop.
'''numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=none, axis=0)
where,
start = Its represents starting element which will become base to the power of start(base^start)
stop = Its represents ending element which will become base to the power of stop (base^stop)
num = It represents number of parts the elements should be devided.Default is 50.It must be positive.
endpoint = If True, stop is last element. If false stop is not included.
base = The base of the logspace.
dtype = The type of output array.
'''

#Creating Array using logspace()
'''Syntax:
from numpy import*
array_name = logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=none)

a = logspace(1,3)
a = logspace(1,3,5)
a = logspace(1,3,5,base=12.0)'''

#no-1
import numpy as np
a = np.logspace(1,3,5)
print(a)

print()

#no-2
from numpy import*
a = logspace(1,3,5)
print(a)

print()


#Accessing 1D logspace() Funtion elements
#no-3
from numpy import*
a = logspace(1,5,5,base=12.0)
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

print()


#Accessing 1D logspace() Funtion elements using for loop
#without index
#no-4
import numpy as np
a = np.logspace(1,3,5,base=12.0)

for el in a:
    print(el)

print()

#with index
#no-5
from numpy import*
value = logspace(1,3,5,base=11.0)

n = len(value)

for i in range(n):
    print("index:",i,"=",value[i])
print()


#Accessing 1D logspace() Funtion elements using while loop
#no-6
import numpy as np
val = np.logspace(1,5,5,base=12.0)

n = len(val)
i = 0

while i<n:
    print("Index:",i,"=",val[i])
    i+=1
print()