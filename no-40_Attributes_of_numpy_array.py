from numpy import*
a = array([101,102,103,104,105])
b = array([[10,20,30,40],
           [50,60,70,80]])

#ndim  
'''This attributes represents the number of dimensions or axes of the array.The number of dimensions is also referred as Rank.
Syntax: array_name.ndim'''
print("1D array ndim:", a.ndim)
print("2D array ndim:", b.ndim)
print()
#shape
'''This attributes represents the shape of an array.The shape is a tuple listing the number of elements along each dimension.
Syntax: array_name.shape'''
#For 1D array shape elements in the row
print("1D array shape:", a.shape)
#For 2D array shape specifies number of row and column in each row
print("2D array shape:", b.shape)
print()
#size
'''This attributes represents the total number of elements in the array.
Syntax: array_name.size'''
print("1D array size:", a.size)
print("2D array size:", b.size)
print()
#itemsize
'''This attributes represents the memory size of the array element in bytes.
Syntax: array_name.itemsize'''
print("1D array itemsize :", a.itemsize)
print("2D array itemsize:", b.itemsize)
print()

#dtype
'''This attributes represents the datatype of elements in the array.
Syntax: array_name.dtype'''
print("1D array dtype :", a.dtype)
print("2D array dtype:", b.dtype)
print()

#nbytes
'''This attributes represents the total number of bytes occupied by an array
Total number of bytes = size of array*item size of each element in the array.
Syntax: array_name.nbytes'''
print("1D array nbytes :", a.nbytes)
print("2D array nbytes:", b.nbytes)
print()