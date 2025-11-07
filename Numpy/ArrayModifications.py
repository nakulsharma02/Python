# Modifiers -> add , remove , stack, split, New data points add, Remove, merge/split
# Array has a fixed size and after adding or deleting an element you have to make a new array.
"""insert() method -> np.insert(array,index,value,axis=None)"""
import numpy as np
arr = np.arange(10,60,10)
print(arr)
new_arr = np.insert(arr,2,100)
print(new_arr)
# for 2d array
arr_2d = np.array([[1,2],[3,4]])
new_arr_2d = np.insert(arr_2d,1,[5,6],axis=0)
print(new_arr_2d)
'''Append(add element at last)'''
new_arr = np.append(arr,[70,80,90])
print(new_arr)
'''np.concadenate((array1,array2),axis=0)'''
# axis 0 -> vertical stacking
# axis 1 -> horizontal stacking
arr1 = np.arange(1,4,1)
arr2 = np.arange(4,7,1)
new_arr = np.concatenate((arr1,arr2),axis=0)
print(new_arr)