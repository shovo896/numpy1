import numpy as np
load_data=np.load('file2.npz')
array1=load_data['file1']
array2=load_data['file2']
print(array1)
print(array2)