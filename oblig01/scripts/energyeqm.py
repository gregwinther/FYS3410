import numpy as np 
from matplotlib import pyplot as plt 

def total_energy(alpha, R, z=2, lambd=1E3, rho=0.32, q=1):
	return z*lambd*np.exp(-R/rho) - alpha*q**2/R

def madelung(N):
	alpha = 0
	for n in range(1, np.int(N)+1):
		alpha += -2.0*(-1)**n/n
	return alpha

crystal_size = np.linspace(1, 50)
d = []

for size in crystal_size:
	
	alpha = madelung(size)
	r = 0.1
	
	U_new = total_energy(alpha, r)
	U_old = 100*U_new
	print(U_old, U_new)
	print(U_old-U_new >1E-10)

	while (U_old-U_new) > 1E-10:
		r += 0.01
		U_old = U_new
		U_new = total_energy(alpha, r)
		print("r = ", r, " U = ", U_new)

	d.append(r)

plt.plot(crystal_size, d)
plt.title("Simulation of repulsive and attractive forces")
plt.xlabel("Unitcells in crystal")
plt.ylabel("Lattice constant")
plt.show()
