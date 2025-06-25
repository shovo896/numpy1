import numpy as np
array1=np.array([[1,7,9],
                 [14,19,21],
                 [25,29,35]])
boolean_mask=array1>9
result =array1[boolean_mask]

print(result)