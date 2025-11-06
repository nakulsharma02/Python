# Indexing and Slicing 
# Indexing --> (Single element can be detected)
# Slicing --> (Select a portion (start stop step))
# Numpy has zero based indexing 
import numpy as np
arr = np.arange(10,60,10)
print(arr)
# Indexing
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])
# Slicing
print(arr[1:5])
print(arr[:4])
print(arr[::2]) # use start stop step
print(arr[::-1])
# Fancy Indexing -> Select Multiple elements at once
print(arr[[0,2,4]])
# Boolean Masking -> Used in Machine Learning
# Filtering the elements on the basis of conditions.
print(arr[arr>30])
