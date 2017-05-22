from matplotlib import pyplot as plt
import numpy as np

E_g =  1.420 # eV 
A_1 =  0.569 # eVnm**2
A_2 = -0.465 # eVnm**2
A_3 = -0.085 # eVnm**2

x = np.linspace(-1.2,1.2)

def quadratic(a, b, x):
    return a + b*x*x

# Electron
plt.plot(x, quadratic(E_g, A_1, x), "b", label="Electron")

# Light hole
plt.plot(x, quadratic(0, A_2, x), "g", label="Hole")

# Heavy hole
plt.plot(x, quadratic(0, A_3, x), "g")

# Lables and stuff
plt.title("GaAs Charge Carriers")
plt.xlim([-1.5, 1.5])
plt.xticks([],[])
plt.yticks([],[])
plt.text(-1.4, E_g/2, r'$E_g$', fontsize=16)

# Straight lines
plt.plot((-1.2, -1.2), (0, E_g), 'k-')
plt.plot((-1.21, -1.19), (0, 0), 'k-')
plt.plot((-1.21, -1.19), (E_g, E_g), 'k-')
plt.plot((-1.1, 1.1), (0, 0), 'k--')
plt.plot((-1.1, 1.1), (E_g, E_g), 'k--')
plt.legend()

plt.plot()
