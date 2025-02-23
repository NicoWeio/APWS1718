import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
from fractions import * 
 
 
 
x, y = np.loadtxt('streu_48.txt', unpack=True,delimiter=',')


 
plt.figure(1)
plt.plot(x, y,'rx', label='Messdaten')



 
plt.ylabel(r'$Intensität\,\,I$ $/ \, \% $')
plt.xlabel(r'$Eindringtiefe\,\,x$ $/ \, mm$')
plt.grid()
plt.legend()
 
 
plt.savefig('streu_48.pdf')
print ('Fertig')