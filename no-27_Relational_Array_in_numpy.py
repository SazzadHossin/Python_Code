#Relational/Compairing Array using Numpy
'''Comparison operator can be used to compare array.The size of array must be same.Comperison operators compares the corresponding elements of the arrays and returns another array with boolen value.'''
from numpy import*
a = array([100,200,300,400,500])
b = array([100,20,30,400,50])
res = a==b
res1 = a>b
print(res)
print(res1)