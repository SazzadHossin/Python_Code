#where() Function 
'''This Function is used to create a new array which contains,returned element choosen from expression 1 or expression 2 depending on condition,If condition is True expresion 1 will be executed else expression 2.
Syntax:- numpy.where(condition, expression1, expression2)'''
#no-1
from numpy import*
a = array([100,200,300,400,500])
b = array([100,20,3000,40,501])
res = where(a>b, a, b)
print(res)

print()

#nonzero() Function
'''This function is used to determine the positions of elements which are non zero.This function returns an array that contains the indexex of the element of the array which are not equal to zero.
Syntax: numpy.nonzero(a)'''
#no-2
from numpy import*
a = array([100,12,300,0,43,32,0,14,18,0,31])
res = nonzero(a)
print(res)
