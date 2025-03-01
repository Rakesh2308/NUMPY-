import numpy as np

s1 = np.ones((2, 3), int)  # Creating an arraay with 2 rows with 3 columns using ones function
s2 = np.zeros((3, 3), int)  # Creating an array with zeros
s3 = np.arange(1, 10, 2)
l = []
for i in range(2):
    l.append(list(np.arange(i, 10, 2)))

s4 = np.linspace(1, 10, 5)  # creating float valus by specifing start end and number of values between them you wnt
s = np.reshape([1,2,3,4,5,6,7,8,],(2,2,2)) # reshaping a one dimrow into two dimenional arrry on two arrays
print(s)
