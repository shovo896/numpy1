import numpy as np
array1=np.array([1,3,5])
array2=np.array([2,4,6])
array3=np.array([[1,3],
                 [5,7]])
result=np.dot(array1,array2)
print(result)
result1=np.inner(array1,array2)
print(result1)
result2=np.outer(array1,array2)
print(result2)
result3=np.linalg.det(array3)