'''Given two NumPy arrays arr1 = [25, 56, 12, 85, 34, 75] and arr2 = [42, 3, 86, 32, 856, 46], solve the following:

1.  Create a new NumPy array Narr with the shape equal to arr1 filled with random values.

2.  Permanently change the dtype of arr1 to complex.

3.  Transform arrays arr1 and arr2 into two matrices (arr1_mat and arr2_mat) of shape (2,3) and arrive at the solution of the following equation:

'''
import numpy as np
arr1 = np.array([25,56,12,85,34,75])
arr2 = np.array([42,3,86,32,856,46])
print(np.shape(arr1))
# 1.
Narr = np.random.rand(int(arr1.size))
print(Narr)
print(np.shape(Narr))
# 2.
arr1 = arr1.astype(complex)
print(arr1.dtype)
print(arr1)
# 3.
arr1_mat = arr1.reshape(2,3)
arr2_mat = arr2.reshape(2,3)
print(arr1_mat,arr2_mat)
solution = (((arr1_mat + arr2_mat)*(arr1_mat - arr2_mat))/(arr1_mat-arr2_mat))
print(solution)
