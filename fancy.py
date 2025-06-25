import numpy as np

# create a numpy array
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# select elements at index 1, 2, 5, 7
select_elements = array1[[1, 2, 5, 7]]

print(select_elements)

simple_indexing = array1[3]
print("simple Indexing :",simple_indexing)
fancy_indexing=array1[[1,2,5,7]]
print("Fancy Indexing:",fancy_indexing) # [2 3 6,8]

sorted_array=array1[np.argsort(array1)]
print(sorted_array)
sorted_array1=array1[np.argsort(-array1)]
print(sorted_array1)
indices=[1,3,6]
new_values = [10,20,30]
array1[indices]=new_values
print(array1)