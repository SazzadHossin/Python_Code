#Accessing Array using for loop

#Without Index
print("Accessing numpy array using for loop but with out index")
#no-1
from numpy import*
roll = array([10,11,12,13,14,15])
for element in roll:
    print(element)

print()

#with index
print("Accessing numpy array using for loop but with index")
#no-2
from numpy import*
stu_roll = array([101,102,103,104,105])

n = len(stu_roll)
for i in range(n):
    print(i, "=", stu_roll[i])

print()

#Modification numpy array 
#no-3
from numpy import*
stu_roll = array([201,202,203,204])
stu_roll[2] = 250

n = len(stu_roll)
for i in range(n):
    print('index:',i,"=",stu_roll[i])

print()


#Accessing Array using while loop
print("Accessing numpy array using while loop")

#no-4
from numpy import*
roll_no = array([101,102,103,104,105])

i = 0
n = len(roll_no)

while i<n:
    print("index:", i, "=", roll_no[i])
    i+=1
print()