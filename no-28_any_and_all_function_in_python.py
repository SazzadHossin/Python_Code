#These are Python buit-in Function

# any() Function 
'''The functions returns True,if any one element of the iterable is True.If iterable is empty then returns Flase.'''
#no-1
from array import*
a = array('i',[101,102,103,104,105])
b = array('i',[101,10,11,104,12])
value = a==b
print(value) #It just return Flase.

print()

#no-2
from numpy import*
a = array([100,200,300,400,500])
b = array([100,20,300,40,50])
res = a==b
print(res) #It will return True Flase Ture Flase Flase
print(any(res))

print()

# all() Function 
'''The functions returns True,if all the elements of the iterable are True or iterable is empty'''
#no-3
import numpy as np
a = np.array([100,200,300,400,500])
b = np.array([100,200,300,400,500])
val = a==b
print(val)
print(all(val))
