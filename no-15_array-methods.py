#append() method: This method is used to add an elementat the end of the existing array.
#Syntax: array_name.append(element)

#no-1
from array import*
stu_id = array('i',[101,102,103,104,105])

n = len(stu_id)

for i in range(n):
    print(stu_id[i])

print()

print("Array After Append")

from array import*
stu_id = array('i',[101,102,103,104,105])

stu_id.append(106)
stu_id.append(107)

n = len(stu_id)

for i in range(n):
    print(stu_id[i])

print()

#insert() method: This method is used to insert an element in a particuler position of the existing  array.
#Syntax: array_name.insert(position_number,new_element)

#no-2
from array import*
roll = array('i',[10,11,12,13,14,15])
n = len(roll)

#Before insert new insert in the array
for i in range(n):
    print(roll[i])

#After inster new element in this array.
print("After insert new element in this array")
roll.insert(1,23)
roll.insert(3,25)

for i in range(len(roll)):
    print(roll[i])

print()


#pop() method: This method is used to remove last element from the exixting array.
#Syntax: array_name.pop()

#no-3
from array import*
stu_roll = array('i',[101,102,103,104,105,106,107])
n = len(stu_roll)

#Accessing existing array
for i in range(n):
    print(i,"=", stu_roll[i])

print()

print("Array After pop")

stu_roll.pop()

for x in stu_roll:
    print(x)

print()
#pop(n) method: This method is used to remove an element specified by position number,from the existing array and return's remove element.
#Syntax: array_name.pop(position_number)

#no-4
from array import*
roll_no = array('i',[201,202,203,204,205])

n = len(roll_no)

for i in range(n):
    print(i,"=", roll_no[i])

print("Array After pop")

r = roll_no.pop(2)

for i in range(len(roll_no)):
    print(i,"=",roll_no[i])
print("Removed elemet: ", r)

print()

#remove() method: This method is used to remove first occurrence of give element from the existing array.If it doesn't found any element, show valueError.
#Syntax: array_name.remove(element)

#no-5
from array import*
id = array('i',[101,102,108,101,103,105,106])
n = len(id)

for i in range(n):
    print(i,"=",id[i])

print("After remove element")
id.remove(101)

for i in range(len(id)):
    print(i,"=",id[i])

print()

#index() method: This method returns position number of first occurrence of give element from the existing array.If it doesn't found any element, show valueError.
#Syntax: array_name.index(element)

#no-6
from array import*
roll = array('i',[101,102,103,101,104,102,105])
print(roll.index(103)) #Its value is 2. 
print(roll.index(101)) #Its value is 0. Becaue it gives first occurrence number.
print(roll.index(102)) #Same Its value is 1. Becaue it gives first occurrence number.

print()

#reverse() method: This method is used to reverse the order of elements in the array.
#Syntax: array_name.reverse()

#no-7
from array import*
value = array('i',[10,11,12,13,14,15,16,17])
n = len(value)

print("Before Reverse")
for i in range(n):
    print(i, "=", value[i])

#After reverse
print('After reverse')

value.reverse()

for i in range(len(value)):
    print(i,"=",value[i])

print()

#extend() method: This method is used to append another array or iterable object at the end of the array.
#Syntax: array_name.extend(another_array or iterable_object)

from array import*
stu_id = array('i',[101,102,103,104,105,106])
n = len(stu_id)

for i in range(n):
    print(i,"=",stu_id[i])

#After Extend
print("After extend")

arr = array('i',[107,108,109,110])
stu_id.extend(arr)

for i in range(len(stu_id)):
    print(i,"=",stu_id[i])