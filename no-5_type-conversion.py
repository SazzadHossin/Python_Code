#Converting one datatype to another datatype is called Type conversion.
'''There are two types of Type Conversion:
1.Implicit type conversion
2.Explicit type conversion'''

# 1.Implicit type conversion: In the implicit type conversion python autometically converts one data type into another datatype.
a = 5
b = 2
res = a/b
print(res) 
print(type(res))

#It will shows error.
'''c = 10
d = '10'
res1 = c+d
print(res1)'''

e = "Hello"
f = "world"
res2 = e+f
print(res2)


# 2.Explicit type conversion: In the explicit type conversion, programmer converts one datatype into another datatype.
x = 5
y = 2
z = x/y
value = int(z)
print(value)

p = 20
q = 10
r = p+q
print(r)
val = float(r)
print(val)
print(type(val))


s = 20
t = '40'
#print(s+t) It will show error
print(type(t))
w = s+int(t)
print(w)
print(type(w))