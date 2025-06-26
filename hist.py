import numpy as np
from matplotlib import pyplot as plt

# create an array of data
data = np.array([5, 10, 15, 18, 20])

# create bin to set the interval
bins = [0,10,20,30]

# create histogram
graph = np.histogram(data, bins)
print(graph)

# plot histogram
plt.hist(data, bins)

plt.show()