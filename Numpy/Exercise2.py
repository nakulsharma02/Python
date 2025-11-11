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

