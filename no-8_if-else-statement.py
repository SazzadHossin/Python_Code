#if....else statement it used when a different sequence of instruction is to be executed depending on logical value of the condition evaluated.
a = 5
b = 2

if a>b:
    print("Greater")
else:
    print("Smaller")
print("Rest of the code")

# We can write it like this also
print("Yes") if a>b else print("No")


#Getting user input
num = int(input("Enter Number Greater than 3: "))
if num>=3:
    print("Correct! You have entered", num)
else:
    print("Wrong! You have entered", num)



#Nasted if-else statement: In nasted if-else statement, an either if-else construct is written within either the body of the if statement or the body of an else statement.
a = 5
b = 2
c = 6
d = 3

if(a>b):
    print("a is greater than b")
    if(c>b):
        print("c is grater than b")
    else:
        print("b is grater than c")
else:
    print("c is grater than d")
