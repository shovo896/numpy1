import numpy as np
import time
start=time.time()



array1=np.array([[1,2,3],[4,5,6]])
array2=np.array([[0,1,2],[0,1,2]])
number=10
result=array1 + number
print(result)
array_sum = array1+array2
print(array_sum)
result2=array2+10
end=time.time()
print("vectorization time :",end-start)

# function that returns a square number
def find_square(x):
    if x<0:
        return 0
    else:
        return x**2
vectorized_function=np.vectorize(find_square)
result=vectorized_function(array1)
print(result
