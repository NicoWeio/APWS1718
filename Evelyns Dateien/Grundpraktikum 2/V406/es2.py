import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
from astropy.io import ascii


plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 0.5

U, I = np.genfromtxt('einzelspalt_b.txt', unpack=True,delimiter=',')
# U = U[4:]
# I = I[4:]
I = I-0.0043
l = 635*10**-6
L = 1000


def T(x, I0, b, x0):
    return I0**2 * b**2 * (l/(np.pi*b*np.sin((x-x0)/L)))**2 * (np.sin(np.pi * b * np.sin((x-x0)/L)/l))**2

params1, covariance1 = curve_fit(T, U, I, p0=[np.max(I), 0.075, 0.1])
# covariance is the covariance matrix

errors1 = np.sqrt(np.diag(covariance1))
print('         Parameter für die erste Linie: ')
print('             A =', params1[0], '±', errors1[0])
print('             b =', params1[1], '±', errors1[1])
print('             x0 =', params1[2], '±', errors1[2])
b = ufloat(params1[1], errors1[1])

x_plot = np.linspace(-12, 12, 100000)
plt.plot(U, I, 'rx', label='Messwerte')
plt.plot(x_plot, T(x_plot, params1[0], params1[1], params1[2]), 'b-', label='Regression')
plt.legend(loc='best')
plt.ylabel(r'$(I-I_{du})\,\,/ \,\,\mathrm{µA}$')
plt.xlabel(r'$x \,\,/ \,\,\mathrm{mm}$')
# plt.xlim(9, 1e2)
# plt.ylim(1e1, 1e4)
plt.grid()
plt.tight_layout()
plt.savefig('es2.pdf')
print('     relativer Fehler Spaltbreite :', (b*(-100)/0.075 - 1)*100, ' %')

