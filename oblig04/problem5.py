import numpy as np 
from matplotlib import pyplot as plt 

def asymtemp(x):
    for x_ in x:
        if (x_ <= 2):
            return 2./(1 + np.exp(x)) - 1
        else:
            return -10


x = np.linspace(0,10)
y = asymtemp(x)

plt.plot(x, y)
plt.show()