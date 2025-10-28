# Shape Attribute 
import numpy as np
arr = np.array([[[[2,3,4],
                [5,6,7]],
                [[7,8,9],
                 [5,6,4]]],
                 [[[2,3,4],
                [5,6,7]],
                [[7,8,9],
                 [5,6,4]]]])
print(arr.shape)
# size Attribute
print(arr.size)
# ndim Attribute
print(arr.ndim)
# dtype Attribute
print(arr.dtype)
# astype() is a method which is used to change the datatype in the numpy
float_arr = arr.astype(float)
print(float_arr,float_arr.dtype)

'''
l1 = [45,56]
l2 = 34
print(l1+l2)'''
# we cannot directly add number in the list without loop in python or doesn't perform such kind of operations without loop.
# But in the numpy array we can
print(arr + 10)
print(arr * 20)
print(arr ** 2)
