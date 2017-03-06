import numpy as np 
from matplotlib import pyplot as plt


def savitzky_golay(y, window_size, order, deriv=0, rate=1):
    
    from math import factorial
    
    #try:
    #    window_size = np.abs(np.int(window_size))
    #    order = np.abs(np.int(order))
    #except ValueError, msg:
    #    raise ValueError("window_size and order have to be of type int")
    #if (window_size % 2 != 1) or (window_size < 1):
    #    raise TypeError("window_size size must be a positive odd number")
    #if window_size < order + 2:
    #    raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order+1)
    half_window = (window_size -1) // 2
    # precompute coefficients
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
    # pad the signal at the extremes with
    # values taken from the signal itself
    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m[::-1], y, mode='valid')

def conductivity(T):
    y =  np.where(T < 1, T**3, 1/T)
    return savitzky_golay(y, 100, 2)
    #return y

def conductivity2(T):
    y = np.where(T < 1, T**3, np.exp(1/(2*T) - (np.exp(0.5) + 1) ))
    #y = np.exp(1/(2*T) - (np.exp(0.5) + 1) )
    return savitzky_golay(y, 100, 2)
    #return y

T1 = np.linspace(0.1,2.5,1001)
T2 = np.linspace(0.1, 2.5,1001)
kappa1 = conductivity(T1)
kappa2 = conductivity2(T2)

plt.plot(T2,kappa2, 'r', label='Umklapp')
plt.plot(T1,kappa1, 'b', label='Normal')
#plt.yscale('log')
plt.xticks([],[])
plt.yticks([],[])
plt.ylabel(r'$\kappa$', fontsize=18)
plt.xlabel('T', fontsize=16)
plt.title('Umklapp vs Normal', fontsize=16)
plt.legend()
plt.show()