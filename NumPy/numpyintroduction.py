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


# import numpy as np
# a = np.array([[30,40,70],[80,20,10],[50,90,60]])


# print('Our array is:')
# print(a)
# print('\n')

# print('Applying percentile() function:')
# print(np.percentile(a, 50))
# print('\n')
# #10,20,20,40,50,60,70,80,90
# print('Applying percentile() function along axis 1:')
# print(np.percentile(a, 50, axis=1))
# print('\n')

# print('Applying percentile() function along axis 0:')
# print(np.percentile(a, 50, axis=0))


# import numpy as np
# a = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
# print('Our array is:')
# print(a)
# print('\n')
# print('Applying argmax() function:')
# print(np.argmax(a))
# print('\n')

# print('Index of maximum number in flattened array')
# print(a.flatten())
# print('\n')

# print('Array containing indices of maximum along axis 0:')
# maxindex = np.argmax(a, axis=0)
# print(maxindex)
# print('\n')

# print('Array containing indices of maximum along axis 1:')
# maxindex = np.argmax(a, axis=1)
# print(maxindex)
# print('\n')

# print('Applying argmin() function:')
# minindex = np.argmin(a)
# print(minindex)
# print('\n')

# print('Flattened array:')
# print(a.flatten())
# print('\n')

# print('Flattened array along axis 0:')
# minindex = np.argmin(a, axis=0)
# print(minindex)
# print('\n')

# print('Flattened array along axis 1:')
# minindex = np.argmin(a, axis=1)
# print(minindex)

import numpy as np
# print(np.average([1, 2, 3, 4], weights=[4, 3, 2, 1], returned=False))

# wt = np.array([3,5])
# a = np.arange(6).reshape(3,2)
# print(np.average(a, axis=1, weights=wt))
# print('\n')


# print('Modified array:')
# print(np.average(a, axis=1, weights=wt, returned=False))


import numpy as np
# a = np.array([[30,40,0],[0,20,10],[50,0,60]])
# print('Our array is:')
# print(a)
# print('\n')
# print('Applying nonzero() function:')
# c = np.nonzero(a)   #index of nonzero element
# print(a[c])


# a = np.array([[3, 7], [9, 1]])
# print('Our array is:')
# print(a)
# print('Applying sort() function:')
# print(np.sort(a))
# print('Sort along axis 0:')
# print(np.sort(a, axis=0))
# print("AXIS 1")
# print(np.sort(a, axis=1))


# import numpy.matlib
# import numpy as np
# print(np.matlib.eye(n=3, M=3, k=0, dtype=float))