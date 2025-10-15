#Getting Array input from user using for loop
from array import*
stu_id = array('i',[])
n = int(input("Number of elements:")) #Getting user input

for i in range(n):
    stu_id.append(int(input("Element:"))) #Append user input to the array

#Accessing
'''p = len(stu_id)
for i in range(p):'''

#or we can use
for i in range(len(stu_id)):
    print(stu_id[i])


#Getting Array input from user using while loop
from array import*
roll = array('i',[])

n = int(input("Enter the num of elements: "))
i = 0

while i<n:
    roll.append(int(input("Enter the elements: ")))
    i += 1

j = 0
while j<(len(roll)):
    print(roll[j])
    j += 1