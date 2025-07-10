import numpy as np
# pip install numpy

# create a numpy array
a=np.array([1,2,3])

# creating array of zeroes, size = 2 x 3 ; says matrix
b=np.zeros((2,3))

# create 3x3 array of only 1's
c=np.ones((3,3))

# create 5 evenly space number between 0 and 1
d=np.linspace(0,1,5)

# identity matrix of 4x4
e=np.eye(4)

print(a)
print("-"*10)
print(b)
print("-"*10)
print(c)
print("-"*10)
print(d)
print("-"*10)
print(e)