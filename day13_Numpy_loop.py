import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

# use 3 for loops to print all elements
for x in arr:
  for y in x:
    for z in y:
      print(z)

# The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration, lets go through it with examples.

for x in np.nditer(arr):
    print(x)

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

# enumeration with ndenumerate()
for idx, x in np.ndenumerate(arr):
  print(idx, x)

# Join arrays

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

# Join 2D arrays along rows (axis=1):
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr_stack = np.stack((arr1, arr2), axis=1)
arr_hstack = np.hstack((arr1, arr2))
arr_vstack = np.vstack((arr1, arr2))
arr_dstack = np.dstack((arr1, arr2))

print(arr_stack)
print(arr_hstack)
print(arr_vstack)
print(arr_dstack)

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)

print(newarr[0])
print(newarr[1])
print(newarr[2])

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)