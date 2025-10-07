#To Show a multi-way decesion based on several conditions, we use is if elif else statement.
day = "sunday"

if (day == "monday"):
    print("Today is Monday")
elif (day == "tuesday"):
    print("Today is Twesday")
elif (day == "wednesday"):
    print("Today is Wednesday")
elif (day == "thursday"):
    print("Today is Thursday")
elif (day == "sunday"):
    print("Today is Sunday")
elif (day == "staturday"):
    print("Today is Saturday")
else:
    print("Today is Friday")


#Taking user input
age = int(input("Enter your age: "))

if (age>10):
    print("You're child! You can not drive")
elif (age>15):
    print("You can not drive yet")
elif (age>=18):
    print("You can drive")
else:
    print("You can not drive!")

