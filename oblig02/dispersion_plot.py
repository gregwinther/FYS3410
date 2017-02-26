import numpy as np
from matplotlib import pyplot as plt

def dispersion(k, a=1, g=9.81, m=1):
    return 2*np.sqrt(g/m)*np.abs(np.sin(k*a/2))

k = np.linspace(-2*np.pi, 4*np.pi,1001)

omega = dispersion(k)

plt.plot(k, omega)
plt.plot((-np.pi,-np.pi),(0,dispersion(np.pi)), 'k--', label="First Brillouin Zone")
plt.plot((np.pi,np.pi),(0,dispersion(np.pi)), 'k--')
plt.xticks([-np.pi, np.pi], [r'$-\frac{\pi}{a}$', r'$\frac{\pi}{a}$'],
        fontsize=14)
plt.yticks([],[])
plt.title("Dispersion Relation")
plt.ylabel(r'$\omega$', fontsize=16)
plt.legend(loc=1)
plt.show()