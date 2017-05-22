import numpy as np 
from matplotlib import pyplot as plt 

def asymtemp(x):
    return -1/(1 + np.exp(-5-2*x)) - 1/(1 + np.exp(5-2*x))


x = np.linspace(-3,3)
y = asymtemp(x)

plt.plot(x, y)
plt.yticks([],[])
plt.xticks([],[])
plt.plot((-3, 3),(-1, -1),'k--', linewidth=1)
plt.plot((-3, 0),(-0.3, -1.7),'k--', linewidth=1)
plt.plot((0, 3),(-0.3, -1.7),'k--', linewidth=1)
plt.xlabel('1/T')
plt.ylabel('log(n)')
plt.title('Concentration of Carriers')
plt.show()
