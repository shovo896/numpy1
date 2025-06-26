import numpy as np


array1 = np.array([2, 6, 10])
array2 = np.array([4, 8, 12])

np.savez('file2.npz', file1 = array1, file2 = array2)