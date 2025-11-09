# Creating Array From Python list
# np.array(e1e1,e1e2,e1e3)
'''import numpy as np
arr = np.array([[1,2,3,4],[6,7,8,9]])
print(arr)'''
# With default values creating array
# np.zeros(shape)(ex-(3)for 1d,(3,3)for 2d)
import numpy as np
zeros_array = np.zeros(4)
print(zeros_array)
# ones(shape)
ones_array = np.ones(45)
print(ones_array)
# Full(shape,value)
filled_array = np.full((2,2,4,5),7)
print(filled_array)
# Create sequences of Numbers in numpy
# arange(start,stop,steps)
arr = np.arange(3.35,56.12,10.12)
print(arr)
'''Note -> Default value of step will be 1'''

# with the help of linspace
array = np.linspace(0,20,5)
print(array)