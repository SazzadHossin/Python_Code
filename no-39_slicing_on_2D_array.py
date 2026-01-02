#Slicing on array can be used to retrieve a piece of the array that contains a group of elements.Slicing is useful to retrieve a range of elements.If we didn't define stop by default it will show to last elements.

'''Syntax: new_array_name = array_name[start:stop:step size,start:stop:step size]
"Here first start:stop:step size for row and second start:stop:step size for column"
The default start value is 0
The default stepzise is 1'''

#no-1
from numpy import*
n = array([[10,20,30],
           [40,50,60],
           [70,80,90]])
print("Original Array")
print(n) 
print()

print("0th row all Columns")
a = n[0, :]
print(a)
print()
print("1st row all Columns")
b = n[1, :]
print(b)
print()
print("3rd row all Columns")
c = n[2, :]
print(c)
print()
print("0th column")
d = n[:,0]
print(d)
for i in d:
    print(i)
print()
print()
print("1st column")
e = n[:,1]
print(e)
for i in e:
    print(i)
print()
print()
print("3rd column")
f = n[:,2]
print(f)
for i in f:
    print(i)
print()
g = n[0:1, 0:1]
print(g)
print()

h = n[0:2,1:3]
print(h)
print()

i = n[1:3,1:3]
print(i)
print()

j = n[1:3,0:2]
print(j)