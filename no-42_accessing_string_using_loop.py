#Accessing String Using for loop
#without index
str1 = "SazzadHossinSojib"
for i in str1:
    print(i)
print()

#with index
str2 = "Sazzad"
n = len(str2)
for i in range(n):
    print("index",i,"=",str2[i])
print()

#Accessing String Using while loop
str3 = "Sazzad Hossin Sojib"
n = len(str3)
i = 0

while i<n:
    print("index",i,"=",str3[i])
    i+=1
print()