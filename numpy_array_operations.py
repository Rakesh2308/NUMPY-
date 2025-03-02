import numpy as np

ar1 = np.array([1,2,3,4,5])
ar2 = np.array([5,4,3,2,1])
print(ar1+ar2) # [6 6 6 6 6]
print(ar1-ar2) # [-4 -2  0  2  4]
print(ar1*ar2) # [5 8 9 8 5]
print(ar1/ar2) # [0.2 0.5 1.  2.  5. ]
print(ar1+3) # [4 5 6 7 8]

#2. Broadcasting (Different Shapes)
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10

print(arr3 + scalar)  # Adds 10 to each element
# Output:
# [[11 12 13]
#  [14 15 16]]

#3. array aggrigate functions

print(ar1.sum())
print(ar2.mean())
print(ar1.max())
print(ar1.min())
print(np.std(ar1))       # Output: 1.7078 (Standard deviation)
print(np.sum(arr3, axis=0))  # Sum along columns: [5 7 9]
print(np.sum(arr3, axis=1))  # Sum along rows: [6 15]
