#Getting user input using zeros() function by for loop
import numpy as np
r = int(input("Enter the number of Row: "))
c = int(input("Enter the number of Columns: "))
a = np.zeros((r,c), dtype= int)
n = len(a) #It Counts number of rows.

print(a)

for i in range(n):
    for j in range(len(a[i])):
        x = int(input("Enter Elements:"))
        a[i][j] = x

#with index
'''for i in range(n):
    for j in range(len(a[i])):
        print("index",i,j,"=",a[i][j])
    print()
print(a)'''

#Without index
for r in a:
    for c in r:
        print(c)
    print()
print(a)

print()



#Getting user input using zeros() function by while loop
from numpy import*
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))
value = zeros((r,c), dtype=int)

n = len(value)
i = 0

while i<n:
    j=0
    while j<len(value[i]):
        x = int(input("Enter Elements:"))
        value[i][j] = x
        j+=1
    i+=1

i = 0
while i<n:
    j = 0
    while j<len(value[i]):
        print("index",i,j,"=",value[i][j])
        j+=1
    i+=1
print(value)
