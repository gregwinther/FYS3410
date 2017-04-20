import numpy as np
from matplotlib import pyplot as plt

# Parameters
a = 1
N = 1
c = np.linspace(0, 1, 1001)

# Fermi vector function
# Dependent on divalent atom composition
def k_F(x):
    Z = (1 - x) + 2*x
    e_1 = (3*np.pi*np.pi)**(1/3)
    e_2 = ((Z*N)**(1/3)) / (N*a)
    return e_1*e_2

# Brillouin zone
k_BZ = np.pi / a

# Counter
i = 0

# For loop comparing vectors
for value in k_F(c):
    i += 1

    # Printing result and breaking
    if (np.abs(value - k_BZ) < 0.001):
        print("Optimum divalent mix is ", c[i])
        break
