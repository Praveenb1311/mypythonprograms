import numpy as np

print(np.array([1,4,2,5,3]))    #Int
print(np.array([3.14, 4, 2, 3]))  #float
print(np.array([1, 2, 3, 4], dtype='float32'))  #manually set the data type


# A list of lists in converted to a 2-dimensional array
original_list = [[1,2,3],[3,4,5],[6,7,8]]
two_dimensional_array = np.array(original_list)
print(original_list)
print(two_dimensional_array)
print(two_dimensional_array.dtype)


# An array of length 10, filled with 0:
print(np.zeros(10, dtype=int))
# An array of size 3x5 filled with 1.0 (float)
print(np.ones((3, 5), dtype=float))
# An array of size 3x5 filled with 3.14
print(np.full((3, 5), 3.14))
# An array containing a linear sequence starting at 0 and
# going up to 20, with steps of 2
print(np.arange(0, 20, 2))
# An array of 5 numbers, linearly spaced between 0 and 1
print(np.linspace(0, 1, 5))
# An array of the given shape and populate it with random
# samples. You can also try using "randint" and "normal"
print(np.random.random((3, 3)))
# The identity matrix of size 3
print(np.eye(3))
print(np.eye(2))


print(np.zeros(2))
print(np.ones(2))
print(np.ones((4,5)))
print(np.full((2,3), 3.14))


x = np.full((3, 4), 5)

print(x)
print(x.dtype)
print(x.shape)
print(x.size)
print(x.ndim)

y = np.full((10, 20), 5, dtype=float)
print(y)


print(y.size)    #to check the how many number of elements are present
print(y.shape)    #to check the matrix x and y
print(y.dtype)    #to check the data type
print(y.ndim)  #to check the dimensional arry



