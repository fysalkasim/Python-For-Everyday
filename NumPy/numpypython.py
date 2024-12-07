# import numpy as np
# # import time
# # a = np.array([1,2,3])  #one dimensional. #two dimesional
# # print(a)
# # print(type(a))

# # dt = np.dtype("i4")
# # print(dt)

# # student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
# # print(student)

# # size = 1000000000

# # numbers = list(range(size))
# # st1 = time.time()
# # for i in numbers:
# #     i * 10
# # end1 = time.time()
# # print("List",end1-st1)

# # numbers = np.arange(size)
# # st2 = time.time()
# # numbers*10
# # end2 = time.time()
# # print("Numpy",end2-st2)


# # a = np.array([[1,2,3],[4,5,6]])
# # print(a)
# # print(a.shape)

# # a = np.array([[1,2,3],[4,5,6]])
# # print(a)
# # b = a.reshape(6,1)
# # print(b)

# # a = np.arange(24)
# # # print(a)
# # # print(a.ndim)
# # b= a.reshape(3,4,2)
# # print(b.ndim)

# # x = np.array([1,2,3,4,5],ndmin=10)
# # # print(x)
# # # print(x.nbytes)
# # print(x.size)

# # x = np.zeros([5,10,6],dtype="i2")
# # print(x)\

# # import numpy as np
# # list = range(5)
# # it = iter(list)

# # # use iterator to create ndarray
# # x = np.fromiter(it, dtype = float, count=2)
# # print(x)

# a = np.array([[1,2,3],[3,4,5],[4,5,6]])
# print('Our array is:')
# print(a)
# # this returns array of items in the second column
# print('The items in the second column are:')
# print(a[..., 1])
# print('\n')

# # Now we will slice all items from the second row
# print('The items in the second row are:')
# print(a[1, ...])
# print('\n')

# # Now we will slice all items from column 2 onwards
# print('The items column 2 onwards are:')
# print (a[...,1:])

# import numpy as np
# arr1 = np.array([[1,2,3,4,6,7,8,9,1,2,3,4,5,65,1,2]])

# print(arr1.reshape(2,2,2,2))