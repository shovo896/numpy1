import numpy as np
import matplotlib.pyplot as plt
car=np.array(["caterham","Tesla","Audi","BWW","Ford","Jeep"])
weight=np.array([0.48,1.7,2,2,2.3,3])
colors=np.array([0,1,2,3,4,5])
sizes=np.array([20,40,60,80,100,120])
plt.scatter(car,weight,c=colors,s=sizes)
plt.show()
plt.bar(car,weight)
plt.title('Bar Graph')
plt.show()
