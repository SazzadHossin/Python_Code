# if: It is used to execute an instruction or block of instructions only if a condition is fuilfilled.
if 5>2:
    print("Greater")

if 5<3:
    print("Right")
print("Hi")

if 7>5:
    print("Obviously")
    print("7 is greater than 5")
print("Rest of the code")


# user input
'''a = int(input("Enter a number greater than 2:"))
if a>2:
    print("You have entered", a)
'''


# Nasted if statement
if (8>5):
    print("Greater")
    print("8 is greater than 5")
    if(6>3):
        print("6 is grater than 3")
print("Rest of the code")


# if statement with logical operator
if 8>5 and 6>3:
    print("Yes! you are right")

if 8>5 and 6<3:
    print("you are right")
print("Bye Bye!")

if 7>5 or 8>6:
    print("Good work!")

if 7>5 or 8<6:
    print("nice buddy")

if 7<5 or 8<6:
    print("Do your work!")
print("Rest of the code")