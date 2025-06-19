import numpy as np
first_array =np.array([1,3,5,7])
second_array=np.array([2,4,6,8])
result1=first_array+second_array
print("Using the + operator :",result1)
result2=np.subtract(first_array,second_array)
print("Using the subtract function:",result2 )

result3=np.multiply(first_array,second_array)
print("Using the multiply () function:",result3)

result4=np.divide(first_array,second_array)
print("using the divide () function :",result4)
result5=np.power(first_array,2);
print("Using the power() function:",result5)

result6=np.mod(first_array,second_array)
print("using the mod function :",result6)



