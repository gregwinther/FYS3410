import numpy as np
from matplotlib import pyplot as plt

def fermidirac(eps,T=1):
    return 1/(np.exp((eps - 1)/T) + 1)

eps = np.linspace(0, 2, 500)

f_1 = fermidirac(eps, 0.01)
f_2 = fermidirac(eps, 0.1)
f_3 = fermidirac(eps, 0.5)
f_4 = fermidirac(eps, 1.2)

plt.plot(eps, f_1, label=r"$T = 0.01T_F$")
plt.plot(eps, f_2, label=r"$T = 0.1T_F$")
plt.plot(eps, f_3, label=r"$T = 0.5T_F$")
plt.plot(eps, f_4, label=r"$T = 1.2T_F$")

plt.legend()

plt.title("Fermi-Dirac Distribution")
plt.xlabel(r"$\epsilon / \mu$", fontsize = 16)
plt.ylabel(r"$f(\epsilon)$", fontsize = 16)

plt.show()