#Input from User in numpy 1D Array
#using for loop
#no-1
from numpy import*
n = int(input("Enter the numbers of elements do you need:"))
a = zeros(n, dtype=int)

for i in range(len(a)):
    x = int(input("Enter elements:"))
    a[i] = x
print(a)

for i in range(len(a)):
    print("index:",i,"=",a[i])

print()

#no-2
import numpy as np
n = int(input('Enter the number of elements do you want:'))
a = np.zeros(n, dtype=int)

for i in range(len(a)):
    x = int(input("Enter the elements:"))
    a[i] = x

for i in range(len(a)):
    print("index:",i,"=",a[i])

print()


#using while loop
from numpy import*
n = int(input("Enter the number of elements:"))

a = zeros(n, dtype=int)
i=0
j=0

while i<len(a):
    x = int(input("Enter the elemets: "))
    a[i] = x
    i+=1

while j<len(a):
    print("index:",j,"=",a[j])
    j+=1