import numpy as np
int_array=np.array([1,3,5,7])
float_array=int_array.astype('float')
print(int_array,int_array.dtype)
print(int_array,float_array.dtype)