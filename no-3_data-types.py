#Datatype represent the type of data stored into a variable or memory.
'''Types of Datatype: 
1.Built-in DataType
2.User define Datatype'''

#Buit-in DataType

# int = The int datatype represent an integer number.An integer number without any decimal point.Ex: 10,20,30,-10,-100
x = 10
pin_code = 4550
y = 200

print(x)
print(type(x))
print(pin_code)
print(type(pin_code))
print(y)
print(type(y))

# float = The float datatype represent floting point numbers.A floating point number is a number that contains decimal point.Ex:26.56,5.45,3.1416
price = 25.50
print(price)
print(type(price))


# complex = A complex number is a number that is written in form of a+bj or a+BJ.

''' a = real part of the number
 b = imaginary part of number
 j or J = square root value of -1
 a or b conatains int or float number. Ex: 5+7j or 6+8.5j
 '''

com = 5+7j
print(com)
print(type(com))


# bool = The bool datatype represent blooean type value True or False.Python internally represent True as 1 and False as 0.


# string = String represents group of characters.Strings are inclosed in double or single quotes
name = "Sojib"
print(name)
print(type(name))

str1 = 'sazzad hossin'
print(str1)
print(type(str1))


# list = A list represent a group of elements.A list can store different types of elements which can be modified.List are dynamic which means size not fixed.List are represented using square bracket []
data = [10,20,50,-10,"Sojib"]
print(data)
print(type(data))

print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])

data[1] = 30
print(data[1])

print(data)

# tuple = A tuple contains a group of elements which can be different types.It similar to list but tuples are read-only which means we can not modify it's element.Tuple are represented using parentheses ().
data1 = (50,55,70.50,-50,"Sazzad")
print(data1)
print(type(data1))

print(data1[0])
print(data1[1])
print(data1[2])
print(data1[3])
print(data1[4])

# range = Range represents a sequence of numbers.The numbers in the range are not modifiable.
rg = range(5)
print(rg[0])
print(rg[1])
print(rg[2])
print(rg[3])
print(rg[4])

rgb = range(10,20,2)
print(rgb[0])
print(rgb[1])
print(rgb[2])
print(rgb[3])
print(rgb[4])


# set = A set is an unorderd collecton of elements much like a set in mathmetics.The order of elements is not mainteined in the sets.It means the elements may not appare in the same order as they are intered into the sets.
''' A set does not accept duplicate elements.
 sets are unorderd so we can not access its element using index.
 stes are represented using curly brackets {}.
 '''
data2 = {100,20,60,"sojib","mehedi","rafi"}
print(data2)


# map/dict/dictonary = A map represents of a group of elements in the form of key vlaue pairs.
d1 = {1: 'sojib', 2: 'rafi', 3: 'mehedi'}
print(d1)

# create dictionary using dict() constructor
d2 = dict(a = "sazzad", b = "hossin", c = "sojib")
print(d2)


# There is no concept of char datatype in python to represent individual character.

#Declaring and initializing variable
a = b = c = d = 10
print(a)
print(b)
print(c)
print(d)

x,y,z = 500,15.70,"sojib"
print(x)
print(y)
print(z)