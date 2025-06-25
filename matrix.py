import numpy as np
matrix1=np.array([[1,3,3],
                  [5,7,2],
                  [2,4,6]])
print("3x3 Matrix:\n",matrix1)
matrix2=np.array([[2,3,5],
                  [7,3,5],
                  [1,3,5]])
print(matrix2)
result=np.dot(matrix1,matrix2)
print(result)
result1=np.transpose(matrix1)
print(result1)
result2=np.linalg.inv(matrix2)
print(result2)
result3=np.linalg.det(matrix2)
print(result3)
result4=matrix1.flatten()
print(result4)
result5=np.union1d(matrix1,matrix2)
print(result5)
result6=np.intersect1d(matrix1,matrix2)

print(result6)


# difference
result7=np.setdiff1d(matrix1,matrix2)
print(result7)
A=matrix1
B=matrix2
print(A)
print(B)
result8=np.setxor1d(A,B)



result9=np.unique(A)
print(result9)