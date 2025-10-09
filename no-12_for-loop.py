#for loop
'''
The for loop is useful to iterate over the elements of sequence such as string,list,tuple etc.
Syntax:
for var in sequence:
    statement
'''

#no-1
name = "Sazzad"
for ch in name:
    print(ch)
print("Rest of the code")

#for loop with range
#no-2
a = range(5)
for i in a:
    print(i)
print('Rest of the code')

#no-3
a = range(1,5)
for i in a:
    print(i)
print('Rest of the code')

#no-4
for i in range(10):  #We can write range function in this way.
    print(i)
print("Rest of the code")

#no-5
for i in range(1,10):
    print(i)
print("Rest of the code")

#no-6
for i in range(1,20,2):
    print(i)
print("Rest of the code")

#no-7
for i in range(-1,-10,-2):
    print(i)
print("Next one")

#no-8
st = "SazzadHossin"
n = len(st)           #len function count length
for i in range(n):
    print(ch,"=",st[i])
print()

#for loop with else
'''
The for loop is useful to iterate over the elements of sequence such as string,list,tuple etc.
This else suite will be always executed irrespective of the statements in the loop are executed or not.
'''
name = "SazzadHossin"
for i in name:
    print(i)
else:
    print("Sojib")
print()


#nasted for loop: for loop inside another for loop is known as nasted for loop.
for i in range(2):
    print("Outer for-loop",i)
    for j in range(1,3):
        print("Inner for-loop",j)
print("Rest of the code")

