#An operator is a symbol that performs an operation.
'''1.Arithmetic operators
2.Relational/comparison operators
3.Logical operators
4.Assignment operators
5.Bitwise operators
6.Membership operators
7.Identity operators
'''

# 1.Arithmetic operators are used to perform basic arithmetic operations such as addition,substraction,multiplication and division.
a = 5
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)


# 2.Relational/comparison operators are used to compare the value of operends to produce a logical value.A logical value either True or False.
b = 5
c = 3

print(b>c)
print(b<c)
print(b>=c)
print(b<=c)
print(b==c)
print(b!=c)


# 3.Logical operators are used to connect more relational operations to from a complex expression called logical expression.A value obtained by evaluating a logical expresssion is always logical.Either True or False.
#Logical and
d = 5
e = 2
f = 3
print(d>e and d>f)
print(d>e and d<f)
print(d<e and d>f)
print(d<e and d<f)

#Logical or
print(d>e or d>f)
print(d>e or d<f)
print(d<e or d>f)
print(d<e or d<f)

#Logical not
a = 5
b = 3
print(not(a>b))
print(not(a<b))


# 4.Assignment operators are used to perform arithmetic operations while assigning a value to a variable
m = 15
m+= 10
print(m)

n = 10
n-= 2
print(n)

o = 5
o*= 2
print(o)

p = 20
p/= 10
print(p)

q = 7
q**= 2
print(q)

r = 15
r//= 10
print(r)

t = 15
t%= 10
print(t)


# 5.Bitwise operators are used to perform operations at binary digit level.This operators are not commonly used and are used only in special application where optmized use of storage is required.
a = 10
b = 15
#Bitwise and &
print('a&b',a&b)
#Bitwise or |
print('a|b', a|b)
#Bitwise xor ^
print('a^b', a^b)
#Bitwise not ~
print('~a',~a)
#Bitwise Leftshift <<
print('a<<2',a<<2)
#Bitwise Rightshift >>
print('a>>2',a>>2)


# 6.Membership operators are useful to text for membership in a sequence such as string,lists,tuple and dictonaries
'''Two types of memebership operators: 
 1. in = This operator is used to find an element in the specified sequence.
         It return True if element is found in a specified sequence else it return False.

2. not in = This operator works reverse manner for in operator.
            It return True if element is not found in a specified sequence else it return False.
'''

# in
st1 = "Hey give it to me"
print("to" in st1)

print("subs" in st1)

#not it
print("subs" not in st1)

print("me" not in st1)

# 7.Identity operators compare the memory locations of two objects.Hence it possible to know whether two objects are same or not.
'''Two types of memebership operators: 
 1. is = This operator is used to compare whether two objects are same or not.
         It return True if memory location of two objects are same else it return Flase.

2. is not = This operator works reverse manner for is operator.
             It return True if memory location of two objects are not same else it return Flase.

'''

#is
a = 10
b = 10
print(a is b)

c = 10
d = '10'
print(c is d)

#is not
print(a is not b)

print(c is not d)

