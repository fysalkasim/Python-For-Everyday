# import numpy as np
# a = np.array([[1,2,3],[4,5,6]],dtype="i4")     #matrix
# print(a)
# print(a.ndim)
# print(a.shape)
# print(a.dtype)
# size = 100000000
# numbers = list(range(size))
# import time
# st1 = time.time()
# for i in numbers:
#     i * 10
# end1 = time.time()
# print(end1-st1)
# numbers = np.arange(size)
# import time
# st1 = time.time()
# np.multiply(numbers,10)
# end1 = time.time()
# print(end1-st1)
# arr = np.array([[4,5,6],[7,8,9],[10,1,3]],dtype="i2")
# print(arr)
# print(arr.shape)
# print(arr.dtype)
# arr.shape = (1,1,1,1,1,1,1,1,1,1,9)
# print(arr.ndim)
# print(arr.size)   #number of elements
# print(arr.itemsize)   #each element size
# print(arr.nbytes)     #total size (size*itemsize)
# bc = np.array([[[1,2,3],[5,6,7]]])
# x = np.ones([5,4],dtype="i1")
# print(x)
# x = np.full([6,6,5,5,4],50)
# print(x)
# list = range(5)
# it = iter(list)
# # use iterator to create ndarray
# x = np.fromiter(it, dtype = np.int8,count=2)
# print(x)
# x = np.arange(10).reshape(5,2)
# print(x)
# x.shape = (2,5)
# print(x)
# print(x.reshape(2,5))
# print(np.reshape(x,[2,5]))