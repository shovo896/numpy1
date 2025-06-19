import numpy as np
array1=np.array([1,3,5])
print("np.array():\n",array1)
array2=np.zeros((3,3))
print("\nnp.zeros():\n",array2)
array3=np.ones((2,4))
print("\nnp.ones():\n",array3)



array4=np.array([1,3,5,7,9,11])
print("Orginal array",array4)
array5=np.reshape(array4,(2,3))
print("\n Reshaped array:\n",array5)


array6=np.transpose(array5)
print("\n Transposed array :\n",array6)



