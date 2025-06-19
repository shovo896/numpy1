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


result1=array1< array2
print(" array1 < array2 :",result1)
result2 = array1 > array2
print(" array1 > array2 : ",result2)
result3=array1==array2
print("array1 == array2: ",result3)

x1 = np.array([True,True,False])
x2=np.array([False,True ,False])
print(np.logical_and(x1,x2))

print(np.logical_or(x1,x2))
print(np.logical_not(x1))


angles=np.array([0.1,2])
print("Angles:",angles)
sine_values=np.sin(angles)
print("Sine Values : ",sine_values)
inverse_sine=np.arcsin(angles)
print(" Inverse Sine Values : ",inverse_sine)
