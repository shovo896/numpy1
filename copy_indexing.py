import numpy as np
numbers=np.array([1,2,3,4,5,6,7,9,10])
numbers_copy =numbers.copy()
numbers_copy[numbers %2 == 0] = 0
# print the modified copy
print(numbers_copy)