# Broadcasting simply means an numpy way in where we perform different kinds of Operations without using loops. And it helps data operations faster than loops. simply like 1d and 2d operations.
# Don't use for loops and faster and earlier.

import numpy as np
prices = np.array([100,200,300])
discount = 10
final_price = prices - (prices*(discount/100))
print(final_price)

'''How Numpy handles arrays of different shapes?
-> Matching Dimensions 
-> Expanding Single Elements 
-> Incompatibe Shapes
'''
# Vectorization simply means Performs operations on the entire array and also perform all kinds of matrix Operations and it makes data operations 100th times faster than loops.

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result1 = arr1 + arr2
result2 = arr1*2
print(result1,result2)


