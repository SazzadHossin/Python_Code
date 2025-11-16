#Aliasing Array
'''Aliasing means giving another name to the existing object.It doesn't mean copying.'''

from numpy import*
a = array([10,20,30,40,50])
b = a
print(a)
#Aliasing
print(b)
print("a", id(a))
print("b", id(b))