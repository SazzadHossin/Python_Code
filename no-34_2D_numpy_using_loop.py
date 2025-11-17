#Accessing 2D array using loop

#Using for loop

#Accessing 1D array using for loop
#no-1
from numpy import*
a = array([10,11,12,13,14,15])
n = len(a)
for i in range(n):
    print(a[i])
print()

#Accessing 2D array using for loop
#without index
#no-2
from numpy import*
a = array([[10,20,30,40,50],
           [60,70,80,90,100]])
for row in a:
    for column in row:
        print(column)
    print()

print()

#no-3
import numpy as np
a = np.array([[10,11,12,13],
             [14,15,16,17]])
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(a[i][j])
    print()

print()

#Modifying 2D array elements
#without index in for loop
#no-4
import numpy as np
val = np.array([[100,200,300,400],
                [500,600,700,800]])
val[0][2] = 45
val[1][3] = 55

for row in val:
    for column in row:
        print(column)
    print()
print()

#with index in for loop
#no-5
from numpy import*
value = array([[10,11,12,13],
              [14,15,16,17]])
value[0][0] = 70
value[1][2] = 90

n = len(value)

for i in range(n):
    for j in range(len(value[i])):
        print(value[i][j])
    print()
print()

#Accessing 2D array using while loop
#no-6
from numpy import*
val = array([[10,20,30,40],
             [50,60,70,80]])

n = len(val)
i = 0

while i<n:
    j = 0
    while j<len(val[i]):
        print(val[i][j])
        j+= 1
    i+=1
    print()
print()

#Modifying 2D array elements
import numpy as np
a = np.array([[20,21,22,23],
              [24,25,26,27]])
a[0][2] = 600
a[1][1] = 110

n = len(a)
i = 0
while i<n:
    j = 0
    while j<len(a[i]):
        print("index:",i,j,"=",a[i][j])
        j+=1
    i+=1
    print()
