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