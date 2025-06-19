import numpy as np
radius = 2
circumference =2*np.pi*radius
print(circumference)
y=np.e
print(y)
x=1
y1=np.exp(x)
print(y1)
array1=np.array([1,2,3])
y2=array1+np.pi
print(y2)
median=np.median(array1)
print(median)

array2=np.array([[2,4,6],
                 [8,10,12],
                 [14,16,18]])
result1=np.median(array2,axis= 1 )
print(" Median along horizontal axis : ",result1)

result2=np.median(array2,axis=0)
print(" Median along vertical axis:",result2)

result3 = np.median(array2)
print (" Median of entire array:",result3)
mean=np.mean(array2)
print(mean)

std_div=np.std(array2)
print(std_div)
result3=np.percentile(array2,25)
print("25th percentile :",result3)

max_val=np.max(array2)
print(max_val)
min_val=np.min(array2)
print(min_val)


array3=np.array(['iphone:','Price:'])
array4=np.array(['15','$900'])
result4=np.char.add(array3,array4)
print(result4)

array5=np.array(['A','B','C'])
result5=np.char.multiply(array5,2)
print(result5)

array6=np.array(['npEall','AmericaN','CanADIan'])
result6=np.char.upper(array6)
result7=np.char.lower(array6)
print("To Uppercase:",result6)
print(" To Lowercase:",result7)
result8=np.char.join('-',array6)
print(result8)