#break statement: Break statement is used to jump out of loop to process the next statement in the program.
#no-1
for i in range(10):
    if(i == 5):
        break
    print(i)
print()

#continue statement: Continue statement is used in a loop to go back to the begining of the loop.
#no-2
for i in range(10):
    if(i == 5):
        continue
    print(i)
print()

#pass statement
'''Pass statement is use to do nothing.It can be used inside a loop or if statement to 
   represent no operation.Pass is useful when we need statement syntacitically correct
   but we do not want to do any operation.
'''
#no-3
if 5>2:
    pass
else:
    print("Else part")
print('Rest of the code')
print()

#no-5
if 5<2:
    pass
else:
    print("Else part")
print('Rest of the code')