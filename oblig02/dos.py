import numpy as np
from matplotlib import pyplot as plt

k = np.linspace(0, np.pi/4)
dos_k = np.ones(len(k))/(2*np.pi)

omega = np.linspace(0, np.pi/4)
dos = lambda omg: (1/np.pi)*(1/np.sqrt(1-omega**2))
dos_omg = dos(omega)


fig, ax1 = plt.subplots()
ax1.plot(k, dos_k)
ax1.set_ylabel(r"$D(k)$", color='b', fontsize=16)
plt.yticks([],[])

ax2 = ax1.twinx()
ax2.plot(omega, dos_omg, 'r')
ax2.set_ylabel(r"$D(\omega)$", color='r', fontsize=16)
ax2.set_ylim([0.3, 0.55])

plt.yticks([],[])
plt.xticks([],[])
plt.title("Density of States", fontsize=18)

plt.show()
