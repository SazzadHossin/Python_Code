#Slicing on arrays can be used to retrieve a piece of the array that contains a group of elements. Slicing is useful to retrieve a a range of elements. If we didn't define stop by default it will show to last elements.
#Syntax: new_array_name = array_name[start:stop:step size]

#no-1
from array import*
stu_id = array('i',[101,102,103,104,105,106,107,108])

n = len(stu_id)

print("Printing Original Array")
for i in range(n):
    print(i,"=",stu_id[i])

print("After Slicing")

a = stu_id[1:5]
a = stu_id[0:] #It will show 0 to last elements
a = stu_id[3:] #It will show 3 to last elements
a = stu_id[:5] #For this case it will start from 0 and end end with n-1 index.Ex:(5-1=4)
a = stu_id[-4:] #It will print last 4 items.
a = stu_id[-5:-3]
a = stu_id[-6:-2]
a = stu_id[0:7:2]

for i in a:
    print(i)

print()

#no-2
from array import*
stu_roll = array('i',[201,202,203,204,205,206,207,208,209,210])

for i in stu_roll[2:6]:
    print(i)
