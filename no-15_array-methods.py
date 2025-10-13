#append method: This method is used to add an elementat the end of the existing array.
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