import numpy as np
from matplotlib import pyplot as plt

def dump(x, center=1):
    return 2 - np.exp(-(center-x)**2 / 10)

x = np.linspace(-15, 15, 1001)

plt.plot(x, dump(x, -5))

plt.title("Electrical Conductivity vs Composition")
plt.xlabel("Share of Mg")
plt.xticks([-15,15],["0 %","100 %"])
plt.ylabel(r"$\sigma$", fontsize=16)
plt.yticks([],[])
plt.ylim([0,3])
plt.show()