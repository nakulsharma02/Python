'''1. Create a 4 x 4 matrix and add values 4,5,6 above the parent diagonal.

2. Given a Numpy array arr = np.arange(11), negate all the elements between 6 and 10.

3. Given a matrix mat and an array arr, for each row of the matrix if elements of Column 1 are equal to the corresponding element of the array, then print the corresponding value of Column 2 of the matrix.
'''
# Ques-1 
import numpy as np
matrix = np.matrix([[0,4,0,0],[0,0,5,0],[0,0,0,6],[0,0,0,0]])
print(matrix)

# Ques-2
arr = np.arange(11)
start_index = 7
end_index = 10
arr[start_index:end_index]*=-1
# arr[[6,7,8]]*=-1
print(arr)

# Ques-3
mat = np.array([['abc','A'],['def','B'],['ghi','C'],['jkl','D']])
arr = np.array(['abc','dfe','ghi','kjl'])
rows = 4
column = 2
result = np.array([],dtype='<U1')
for i in range(rows):
    if mat[i][0] == arr[i]: 
            result = np.append(result,mat[i][1])
print(result)

# Ques-4 
# 4. Given a matrix mat, sort it by the second column.
import numpy as np
mat = np.array([[1,21,3],[5,4,2],[56,12,4]])
mat_new = np.argsort((mat[:,1]),axis=0)
mat = mat[mat_new]
print(mat)
'''For multiple columns use lexsort() method of numpy'''

#  Find the nearest number from the given number in an array.
# Use Argmin
arr = np.array([10,55,22,3,6,44,9,54])
nearest_to = 50
# numpy.argmin(a, axis=None, out=None, *, keepdims=<no value>)
absolute_diff = np.abs(arr - nearest_to)
min_index = np.argmin(absolute_diff)
print(arr[min_index])

# 5. Given an array arr, find the top 4 maximum values.

 
import numpy as np
arr = np.array([90, 14, 24, 13, 13, 590, 0, 45, 16, 50])
arr1 = np.sort(arr)
sorted_desc = arr1[::-1]
print("The Top Four Maximum Values are:")
print(sorted_desc[0:4])

# Using argpartition()
arr2indices = np.argpartition(arr,-1)
arr2 = arr[arr2indices[-4:]]
print(arr2)
