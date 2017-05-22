import numpy as np 
from matplotlib import pyplot as plt 

def scurve(x):
    return 1.0/(1 + np.exp(-0.2*x))

x = np.linspace(-20,20)
y = scurve(x)

plt.text(-20, -0.35, r"$E_i$", fontsize=14)
plt.plot((-20,20), (0,0), 'k--', linewidth=1)

plt.text(-20, -2.8, r"$E_V$", fontsize=14)
plt.plot((-20,20), (-3,-3), 'k')

plt.text(-20, 1.5, r"$E_C$", fontsize=14)
plt.plot((-20,20), (1.8, 1.8), 'k')

plt.plot((-20,20), (1, 1), 'k--', linewidth=1)


plt.xticks([],[])
plt.yticks([],[])

plt.xlabel("1/T", fontsize=18)
plt.ylabel("E", fontsize=18)

plt.title("Fermi Energy vs Temperature")

plt.plot(x, y)

plt.show()