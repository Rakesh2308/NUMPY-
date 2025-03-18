import numpy as np
"""
syntax :
        array[index] - this is for onedimentional array
        array[start:stop:step]

"""

arr = np.array([1,2,3,4,5,78])
print(arr[4])
print(arr[1:5:2])

"""

syntax:
        array[row_index, col_index]
        array[start:stop:step, start:stop:step]

"""

arr = np.array([[1,2,3,4,5],[11,12,13,14,15],[21,22,23,24,25]])
# print(arr[1][1]) # 12
print(arr[1:3, 1:3])  # Select row index 1 and columns 1 to 2