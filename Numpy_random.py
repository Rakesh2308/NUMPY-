import numpy as np

"""The default_rng function in NumPy is used to create a new instance of the Generator class, 
which is a core part of NumPy's random number generation framework introduced in version 1.17. 
This function provides a convenient way to generate random numbers with better statistical
 properties compared to the older numpy.random methods"""

rng = np.random.default_rng()
print(rng.integers(1,10,5))
print(rng.random(5))  # 5 random floats between [0,1)
print(rng.choice([1,2,3,4,5,6],2)) # select 2 numbers from list random ly
print(rng.permutation([1,2,3,4,5])) # Shuffle the list
normal_values = rng.normal(loc=0, scale=1, size=5)  # 5 values from N(0,1)
print(normal_values)
uniform_values = rng.uniform(low=10, high=20, size=5)  # 5 values between [10,20)
print(uniform_values)
poisson_values = rng.poisson(lam=5, size=5)  # Mean=5
print(poisson_values)

