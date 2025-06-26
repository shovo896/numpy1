import numpy as np

# get the current date and time 
result = np.datetime64('now')

date_today=np.datetime64('today','D')
print(result)
print(date_today)