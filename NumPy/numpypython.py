# # import numpy as np
# # # import time
# # # a = np.array([1,2,3])  #one dimensional. #two dimesional
# # # print(a)
# # # print(type(a))

# # # dt = np.dtype("i4")
# # # print(dt)

# # # student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
# # # print(student)

# # # size = 1000000000

# # # numbers = list(range(size))
# # # st1 = time.time()
# # # for i in numbers:
# # #     i * 10
# # # end1 = time.time()
# # # print("List",end1-st1)

# # # numbers = np.arange(size)
# # # st2 = time.time()
# # # numbers*10
# # # end2 = time.time()
# # # print("Numpy",end2-st2)


# # # a = np.array([[1,2,3],[4,5,6]])
# # # print(a)
# # # print(a.shape)

# # # a = np.array([[1,2,3],[4,5,6]])
# # # print(a)
# # # b = a.reshape(6,1)
# # # print(b)

# # # a = np.arange(24)
# # # # print(a)
# # # # print(a.ndim)
# # # b= a.reshape(3,4,2)
# # # print(b.ndim)

# # # x = np.array([1,2,3,4,5],ndmin=10)
# # # # print(x)
# # # # print(x.nbytes)
# # # print(x.size)

# # # x = np.zeros([5,10,6],dtype="i2")
# # # print(x)\

# # # import numpy as np
# # # list = range(5)
# # # it = iter(list)

# # # # use iterator to create ndarray
# # # x = np.fromiter(it, dtype = float, count=2)
# # # print(x)

# # a = np.array([[1,2,3],[3,4,5],[4,5,6]])
# # print('Our array is:')
# # print(a)
# # # this returns array of items in the second column
# # print('The items in the second column are:')
# # print(a[..., 1])
# # print('\n')

# # # Now we will slice all items from the second row
# # print('The items in the second row are:')
# # print(a[1, ...])
# # print('\n')

# # # Now we will slice all items from column 2 onwards
# # print('The items column 2 onwards are:')
# # print (a[...,1:])

# # import numpy as np
# # arr1 = np.array([[1,2,3,4,6,7,8,9,1,2,3,4,5,65,1,2]])

# # print(arr1.reshape(2,2,2,2))

# # x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# # print('Our array is:')
# # print(x)
# # print('\n')

# # rows = np.array([[0, 0], [3, 3]])
# # cols = np.array([[0, 2], [0, 2]])
# # y = x[[[0, 0], [3, 3]], [[0, 2], [0, 2]]]
# # print(y)

# # a = np.arange(0,60,5)
# # a = a.reshape(3,2,2)

# # print(a)
# # for i in a:
# #     for j in i:
# #         for k in j:
# #             print(k)

# # a = np.array([[[1,2][3,4][4,6]]])

# # print('First array:')
# # print(a)

# # b = np.array([[5,6],[7,8]])

# # print('Second array:')
# # print(b)

# # # both the arrays are of same dimensions

# # print('Joining the two arrays along axis 0:')  #
# # print(np.concatenate((a, b)))

# # print('Joining the two arrays along axis 1:')
# # print(np.concatenate((a, b), axis=1))


# # bc = np.arange(1,31).reshape(10,3)
# # print(bc.shape)




# # a = np.array([5,2,6,2,7,5,6,8,2,9])
# #[2 5 6 7 8 9]
# # print('First array:')
# # print(a)
# # print('\n')

# # print('Unique values of first array:')
# # u = np.unique(a)
# # print(u)
# # print('\n')

# # print('Unique array and Indices array:')
# # u,indices = np.unique(a, return_index = True)
# # print(indices)
# # print('\n')

# # print('We can see each number corresponds to index in original array:')
# # print(a)
# # print('\n')

# # print('Inverses of unique array:')
# # u,inverse = np.unique(a,return_inverse = True)
# # print(u)
# # print('\n')

# # print('Indices are:')
# # print(inverse)
# # print('\n')

# # print('Reconstruct the original array using indices:')
# # print(u[indices])
# # print('\n')

# # print('Return the count of repetitions of unique elements:')
# # u,indices = np.unique(a,return_counts = True)
# # print(u)
# # print(indices)

# # a = np.array([[1,2,3],[4,5,6]])
# # print(a)
# # b = np.split(a,[5,6],0)
# # print(b)

# # import numpy as np
# # a = np.array([[1, 2], [3, 4]])
# # b = np.array([[11, 12], [13, 14]])

# # print("Vdot Product:")
# # print(np.vdot(a, b))  #11+24+39+56 = 130



# # a = np.array([[1, 2], [3, 4]])
# # b = np.array([[5, 6], [7, 8]])
# # print(a)
# # print(b)

# # print("Inner Product (2D):")
# # print(np.matmul(a, b))












# # import numpy as np
# # list = range(5)
# # it = iter(list)

# # # use iterator to create ndarray
# # x = np.fromiter(it, dtype ="i1",count = )
# # print(x)





# # print(a.shape)
# # # (2, 3, 4, 5)
# # print(a)
# # print(a[0, 2:5])   #[rows,columns]    #[2,1]


# import numpy as np
# # a = np.arange(12).reshape(2,3,2)

# # print(a.ndim)

# # print(a)

# # for i in a:
# #     for j in i:
# #         for k in j:
# #             print(k)

# # for i in np.nditer(a):
# #     print(i)

# # a= np.array([[1,2,3,4],[5,6,7,8]])
# # print(a.shape)   #(2,4)
# # print(a.size)    #8
# # b=a.reshape(4,2)  #2dimension
# # print(b)
# # c=np.resize(a,[4,4,12,25])
# # print(c)


# import numpy as np
# a = np.array([5,2,6,2,7,5,6,8,2,9])

# print('First array:')
# print(a)
# print('\n')

# print('Unique values of first array:')
# u = np.unique(a)
# print(u)
# print('\n')

# print('Unique array and Indices array:')
# u,indices = np.unique(a, return_index = True)
# print(indices)
# print('\n')

# # print('We can see each number corresponds to index in original array:')
# # print(a)
# # print('\n')

# print('Inverses of unique array:')
# u,inverses = np.unique(a,return_inverse = True)
# print(inverses)
# print('\n')

# # print('Indices are:')
# # print(indices)
# # print('\n')

# # print('Reconstruct the original array using indices:')
# # print(u[indices])
# # print('\n')

# # print('Return the count of repetitions of unique elements:')
# # u,indices = np.unique(a,return_counts = True)
# # print(u)
# # print(indices)


# name = "Python"
# name2 = ["a","b"]

# print(name.join(name2))



# import numpy as np
# a = np.array([[3,7,5],[8,4,3],[2,4,9]])
# print('Our array is:')
# print(a)
# print('\n')

# print('Applying ptp() function:')
# print(np.ptp(a))
# print('\n')

# print('Applying ptp() function along axis 1:')
# print(np.ptp(a, axis=1))
# print('\n')

# print('Applying ptp() function along axis 0:')
# print(np.ptp(a, axis=0))


# def msg(*names,year):
#     for i in names:
#         print(f"{i} is on the {year}")
# msg("hridya","fysal",year =2024)




# import numpy as np
# a = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
# print('Our array is:')
# print(a)
# print('\n')
# print('Applying argmax() function:')
# print(np.argmax(a))
# print('\n')

# # print('Index of maximum number in flattened array')
# # print(a.flatten())
# # print('\n')

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
# print(a.flatten()[minindex])
# print('\n')

# print('Flattened array along axis 0:')
# minindex = np.argmin(a, axis=0)
# print(minindex)
# print('\n')

# print('Flattened array along axis 1:')
# minindex = np.argmin(a, axis=1)
# print(minindex)

# import numpy as np
# x = np.arange(9.).reshape(3, 3)

# print('Our array is:')
# print(x)

# print('Indices of elements > 3')
# y = np.where(x > 3)
# print(y)

# print('Use these indices to get elements satisfying the condition')
# print(x[y])

# import numpy.matlib
# import numpy as np
# print(np.matlib.eye(n=3, M=4, k=0, dtype=float))


# import numpy as np
# a = np.array([1,2])
# b = np.array([11,12])
# print("Array a")
# print(a)
# print("Array b")
# print(b)
# print("Dot product")
# print(np.dot(a,b))


# print(np.allclose(10, 10))

# s1="hai"
# s=s1 +","+str(25)
# print(s)
