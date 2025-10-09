#range() Function
'''
range() function is used to generate a sequence of integers starting from 0 by default,
and increments by 1 by default, till j-1
syntax:
range(start,stop,stepsize)

start = Starting position. If we do not mention start by default it's 0
end(mendatory) = Ending Position. The range of integers stops one element prior to stop.If stop is j
                 then it will stop at j-1
stepsize = Increment by stepsize. If we do not mention start by default it's 1

Rules:
1.All arguments must be integers,whether its positive or negative.
2.You can not pass a string or float number or any other types of start,end and stepsize.
3.The stepsize value should not be 0.
'''

#no-1
a = range(5)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print("End")

#no-2
b = range(1,10)
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])
print(b[5])
print(b[6])
print(b[7])
print(b[8])
print("End")

#no-3
c = range(1,20,2)
print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])
print(c[5])
print(c[6])
print(c[7])
print(c[8])
print(c[9])



