# These Functions are used to perform basic operations on array elements to give a single output or desired output
# np.sum(array) -> sum of array elements
# np.mean(array) -> average of array elements
# np.min(array) -> minimum element of array
# np.max(array) -> maximum element of array
# np.std(array) -> standard deviation of array
# np.var(array) -> Variance of an array
import numpy as np
arr = np.array([[[3,4,5],
                 [5,6,7]],
                 [[3,10,5],
                 [5,9,8]]])
print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))

