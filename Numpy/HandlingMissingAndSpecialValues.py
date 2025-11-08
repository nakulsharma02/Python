# There are some built-in methods or functions in numpy for Handling Missing and Special Values.
''' np.isnan() -> detect missing values.
    np.nan_to_num() -> convert the not a number values into a number in every place of a dataset.
    np.isinf() -> check the the given values in the datasets are infinity or not.
'''
import numpy as np
arr = np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr))

# Note -> We can't compare Nan values directly.

''' nan_to_num() 
    np.nan_to_num(array,nan=value)
    default nan = 0'''
cleared_arr1 = np.nan_to_num(arr)
print(cleared_arr1)
cleared_arr2 = np.nan_to_num(arr,nan=5)
print(cleared_arr2)

''' np.isinf()
    like 10^1000
         1/0
'''
arr1 = np.array([1,2,np.inf,4,-np.inf,6])
print(np.isinf(arr1))
cleaned_arr = np.nan_to_num(arr1,posinf=1000,neginf=-1000)
print(cleaned_arr)