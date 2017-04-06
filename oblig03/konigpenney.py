import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-1,2,1000)
V = np.zeros(len(x))

V[0]   = 1
V[333] = 1
V[666] = 1
V[999] = 1

x0 = np.linspace(-1.5, 2.5,1200)
V0 = np.ones(len(x0))

plt.plot(x, V)
plt.plot(x0, V0, 'k--')
plt.ylim([-0.01, 3])
plt.xlim([-1.5, 2.5])
plt.text(1.7, 1.1, r'$V_0$', fontsize = 14)
plt.xticks([-1, 0, 1, 2],[r'$-a$', r'$0$', r'$a$', r'$2a$'], fontsize = 14)
plt.yticks([],[])
plt.title(r"$\delta$-function Potential", fontsize = 20)
plt.xlabel(r"$x$", fontsize = 16)
plt.ylabel(r"$V(x)$", fontsize = 16)
plt.show()
