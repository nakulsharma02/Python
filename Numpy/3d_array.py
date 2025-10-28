# Example of 3d Array
import numpy as np
array_3d = np.array([[[2,3,4],
                     [3,4,5],
                     [6,7,8]],
                     [[5,9,9],
                      [5,6,7],
                      [6,9,2]]])
print(array_3d) # Print whole array
print(array_3d.shape) # Print (2,3,3)
print(array_3d.size) # Print (18)
print(array_3d[0,1,2]) # Print (5)
print(array_3d[1,0,:]) # Print ([5,9,9])
print(array_3d[1,2,2]) # Print (2)
