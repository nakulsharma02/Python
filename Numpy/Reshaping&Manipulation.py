# Reshaping -> without modify dimension or shape
# 1d->2d->3d->2d->1d
# syntax -> arr.reshape()
# Total No. of Elements will be same
# import numpy as np
# arr = np.array([1,2,3,4,5,6])
# reshaped_Arr = arr.reshape(2,3)
# for making one d array(-1)
# print(reshaped_Arr)
# Note -> Reshape doesn't create copy(view).
# Flattening Array -> Flattening of array means conversion in one d array
# Two methods of flattening of array
# ravel(), flatten()
# ravel() -> view
# flatten() -> copy
# print(type(arr))
import numpy as np
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())
arr1 = arr_2d.ravel()
arr2 = arr_2d.flatten()
print(type(arr1))
print(type(arr2))
print(arr1)
add1 = np.sum(arr1)
add2 = np.sum(arr2)
print(add1)
print(add2)
print(arr_2d)