import numpy as np
array1=np.array([1,2,3,4,5,6,7,8,9,10,40,23,24,33,22,31,44])
boolean_mask = array1 % 2 != 0
boolean_mask1=(array1 <10 ) | (array1 > 40 )
result = array1[boolean_mask]
result1=array1[boolean_mask1]

print(result)
print(result1)

