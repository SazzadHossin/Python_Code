#Mathmetical Operations on Arrays using numpy.
'''We can perform mathmetical operations like addition,substraction,multiplication,division etc on the elements of an array.Math functions from the math module can also be possible to apply the elements of the array.'''

#no-1
#addition
from numpy import*
a = array([101,102,103,104,105])
a = a+5
print(a)
print()

#no-2
#substraction
from numpy import*
a = array([101,102,103,104,105])
a = a-5
print(a)
print()

#no-3
#multiplication
from numpy import*
a = array([101,102,103,104,105])
a = a*5
print(a)
print()

#no-4
#division
from numpy import*
a = array([101,102,103,104,105])
a = a/5
print(a)
print()


#using loop
from numpy import*
num1 = array([10,11,12,13,14,15])
num2 = array([1,2,3,4,5,6])
res = num1+num2
n = len(res)
for i in range(n):
    print("index:",i,"=",res[i])