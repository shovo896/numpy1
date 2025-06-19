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


arr_sqrt=np.sqrt(array2)
print(" \nSquare root of second array:\n",arr_sqrt)

mean_marks=np.mean(array1)
print(" mean ", mean_marks)
median_marks=np.median(array4)
print(" Median", median_marks)
min_marks=np.min(array5)
print(" Minimum marks : " ,min_marks)


loaded_data=np.loadtxt('array4.txt')
print(loaded_data)