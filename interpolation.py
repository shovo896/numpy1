import numpy as np

day = np.array([2, 4, 7])
gold_price = np.array([55, 58, 65])

# find the value of gold on day 3
day3_value = np.interp(3, day, gold_price)

print("The value of gold on day 3 is", day3_value)