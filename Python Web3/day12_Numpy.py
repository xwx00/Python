'''
NumPy is a Python library.

NumPy is used for working with arrays.

NumPy is short for "Numerical Python".
'''

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))


arr2 = np.array([1, 2, 3, 4, 5])
print(arr2)
print(type(arr2))

print(arr2.ndim) #ndim = number of dimensions
print(arr2.shape) #shape = tuple of array dimensions

arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr3[1, 1:4])


arr4 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr4[0:2, 2])
print(arr4[0:2, 1:4])

# convert data type of an array
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

# copy() vs view()
# the copied array is a new array, and changes made to the copied array will not affect the original array, and vice versa.
# the view is just a view of the original array, and any changes made to the view will affect the original array, and vice versa.
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

x[1] = 99
print(arr)
print(x)

# check if array owns its data
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

# shape of array

# arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)