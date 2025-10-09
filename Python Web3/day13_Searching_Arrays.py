
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

x = np.where(arr == 4)
print(x)

# Search sorted
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 10, side='left')

print(x)


arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)