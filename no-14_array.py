#Array
'''In python Array is a object that provide a machanism for storing several data items with
   only one identifier,thereby simplifying the task of data management.Array is beneficial if you need to store group of elements of same datatype.
   In python,Array size is not fixed. Array can increases or decrease their size dynamically.
   Array can store one type of data.
   Ex: Group of integer: 1,2,3,4,55
       Group of float: 14.3,23.4,29.2
    Array and list are not same.
    Array uses less memory than list.

    Types of Array: There are two types of array.
                    1.One Dimension Array/One D Array -->Single row multiple column
                    2.Multi Dimension Array/Multi D Array -->Multiple row multiple column
    Note: Python does not support multi dimension array but we can create multi dimension array using
        packages like numpy.

    Two way to import array module:
    1. import array -->This will import the array module
       syntax:
        array_name = array.array('type code',[elements])
    2. from array import* -->This will import all class,objects,variable etc from array module.
    Here * means All.
        syntax:
            array_name = array('type code',[elements])
    
    Note:When we use integer then use 'i' as a type code and if we use float then use 'f' or 'd' as a    type  code.
'''

#index: An index represents the position number of an array's element.Index always starts with 0.

# One Dimension Array: Single row single column.

#no-1
import array
stu_roll = array.array('i',[1,2,3,4,5])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

print()

#no-2
import array as arr  #using as to name array to arr
stu_roll = arr.array('i',[1,2,3,4,5])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

print()

#no-3
from array import*
stu_roll = array('i',[101,102,103,104,105])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

print()

#no-4
from array import*
stu_roll = array('f',[10.1,10.2,10.3,10.4,10.5])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

print()

#no-4
from array import*
stu_roll = array('f',[10,20,45.6,60.2,70])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

print()

#no-5
#This is throws an error because float object can not be interpreted as an integer.
'''from array import*
stu_roll = array('i',[10,20,45.6,60.2,70])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])        
print(stu_roll[3])
print(stu_roll[4])'''


#Accessing Array using for loop
#no-6
#without index
from array import*
stu_roll = array('i',[101,102,103,104,105])

for i in stu_roll:
    print(i)

print()

#no-7
#with index
#Here accessing index with elements
from array import*
stu_roll = array('i',[101,102,103,104,105])
n = len(stu_roll)

for i in range(n):
    print(stu_roll[i])

print()

#no-8
#with index no
#Here accessing index with elements
from array import*
stu_roll = array('i',[101,102,103,104,105])
n = len(stu_roll)

for i in range(n):
    print(i,"=",stu_roll[i])

print()

#no-9
#Accessing Array using while loop
#without index
from array import*
num = array('i',[10,20,30,40,50])

i = 0
n = len(num)

while i<n:
    print(num[i])
    i += 1
print()


#no-10
#With indexing
from array import*
num = array('i',[10,11,12,13,14,15])
n = len(num)
i = 0

while i<n:
    print(i,"=",num[i])
    i += 1
print()
