import numpy as np

day = np.array([2, 4, 7, 10])
gold_price = np.array([55, 58, 65, 70])

# days whose value is to be interpolated
interpolate_days = np.array([1, 3, 5, 6, 8, 9])

interpolated_price= np.interp(interpolate_days, day, gold_price)

print(interpolated_price)