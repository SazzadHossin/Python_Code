#Loop Control Statement
'''Loop Control Statement are used when a section of code may either be executed a fixed number of times or while some conditions are true
1.while loop
2.for loop
'''

#while loop: The while loop keep repeating an action until an associated condition returns false.
#no-1
a = 1

while a<=10:
    print(a)
    a += 1
print('Rest of the code')

#no-2
a = 2

while a<=20:
    print(a)
    a += 2
print("Rest of the code")

# no-3 
i = 3

while i<=30:
    print(i)
    i += 3
print('End')

#while loop with else
'''This repeatedly tests the conditon and if it is True,execute the statement 1,
if the condition is False the statement 2 of the else clause is execute and the loop terminates.
This else suite will be always executed irrespective of the statements in the loop are executed or not.
'''
#no-4
i = 1

while i<=5:
    print(i)
    i += 1

else:
    print("while condition False or while condition excute not this else statement will be executed")

print('Rest of the code')

#no-5
a = 6

while a<=5:
    print(a)
    a += 1

else:
    print("Execute")
print("Rest of the code")


#infinite while loop
'''
#no-6
while True:
    print("Sazzad")
print("Rest of the code")
'''

#no-7
i = 0
while True:
    print(i)
    i += 1
    if(i == 10):
        break
print("Rest of the code")


#nasted while loop
i = 1

while i<=3:
    print("Outer Loop:",i)
    i+= 1
    j = 0
    while j<=5:
        print("Inner Loop",j)
        j+= 1
print("Rest of the code")
