import numpy as np 
from matplotlib import pyplot as plt 

def madelung(N):
	alpha = 0
	for n in range(1, np.int(N)+1):
		alpha += -2.0*(-1)**n/n
	return alpha

crystal_size = np.linspace(1, 50)
madelung_constants = []

for size in crystal_size:
	madelung_constants.append(madelung(size))

plt.plot(crystal_size, madelung_constants)
plt.title("Madelung's constant for different crystal sizes")
plt.xlabel("Crystal size")
plt.ylabel("Madelung's constant")
plt.show()
