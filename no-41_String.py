#String
'''String represents group of characters.String are enclosed in double quotes or single quotes.The str datatype represents a String.
Ex:- "Hello", 'Sojib', "Sazzad" 
'''

#Creating String
#Single quotes
str1 = 'Sazzad'
print(str1)
print()

#Double quotes
str2 = "Sazzad Hossin"
print(str2)
print()

#Tripple Single quotes- This is useful to create strings which span into several lines.
str3 = '''Hello!
How are you?
I am fine.'''
print(str3)
print()

#Tripple Double quotes- This is useful to create strings which span into several lines.
str4 = """Hey buddy!
What are you doing?"""
print(str4)
print()

#Double quote inside Single quotes
str5 = 'Hello "Sojib" How are you?'
print(str5)

#Single quotes inside Double quotes.
str6 = "Jarif is a 'Good' Boy"
print(str6)
print()

#Using Escape Characters
str7 = "Hello \n How are you?"
print(str7)
print()

#Raw String- Row string is used to nullify the effect of escape characters.
str8 = r"Hey \nwhat are you doing?"
print(str8)
print()


#Memory Allocation
str9 = "Sazzad"
str10 = "Sazzad"
str11 = "Python"
str12 = str11
print("Str9",id(str9))
print("Str10",id(str10))
print("Str11",id(str11))
print("Str12",id(str12))

str13 = "Sazzad"
print("Str13", id(str13))
str13 = "Sojib"
print("Str14", id(str13))
print(str13)
print()

#Index- Index represents the position number of characters in a string.
str14 = "Sazzad"
print(str14[0])
print(str14[1])
print(str14[2])
print(str14[3])
print(str14[4])
print(str14[5])

print()

#String Length
'''Length of String represents the number of characters in a string.
len() Function is used to get length of string.'''
val = "Sazzad"
n = len(val)
print(n)
print()

#Mutable Object
'''Mutable Object are those Object whose value or content can be changed as and when required.
Ex:- List,Set,Dictionaries.'''

#Immutable Object
'''Immutable Object are those Object whose value or content can not be changed.
Ex:- Numbers,String,Tuple'''

'''value = "Sazzad"
value[3] = 'i'  #It is not possible. That's why String are immutable.It shows a TypeError.
for c in value:
    print(c)'''

#Repetition Operator
'''Repetation Operator is used to repeat the string for several times.It denoted by *'''
print("$"*7)
val = "SazzadHossin"
print(val*5)
print(val[0:6]*6)
print()

#Concatenation Operator
'''Concatenation Operator is used to join two String.It denoted by +'''
value = "Sazzad" + "Hossin" + "Sojib"
print(value)
print()

name = "sojib"
print("Hello"+name)
print("Hello",name)
print()


#Comparing String
val1 = "Sojib"
val2 = "Sojib"
val3 = val1 == val2
print(val3)
print()
val4 = "Sazzad"
val5 = "Python"
val6 = val4 == val5
print(val6)
print()

str1 = "A"
str2 = "B"
print(str1<str2)
print()