import numpy as np

# Ignore division warnings
np.seterr(divide='ignore')

array1 = np.array([1, 2, 3])
array2 = np.array([0, 2, 0])

# Use where to avoid division by zero
result = np.divide(array1, array2, out=np.full_like(array1, np.nan, dtype=float), where=array2 != 0)

print(result)

#another program 

np.seterr(divide='raise')

array1 = np.array([1, 2, 3])
array2 = np.array([1, 2, 1])  # No zero

result = np.divide(array1, array2)

print(result)



