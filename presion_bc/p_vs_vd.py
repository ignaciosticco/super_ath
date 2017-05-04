# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html
import matplotlib.pyplot as plt
import pylab
import numpy as np
import math
from pylab import arange,pi,sin,cos,sqrt,savefig
# a dos columnas: 3+3/8 (ancho, in)
# a una columna : 6.5   (ancho  in)
golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8  							# width in inches
fig_height = fig_width*golden_mean      	# height in inches
fig_size =  [fig_width,fig_height]
params = {'backend': 'ps',
          'axes.labelsize': 10,			# Poner en 8
          'text.fontsize': 10,
          'legend.fontsize': 10,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'figure.figsize': fig_size}
pylab.rcParams.update(params)

### DATA

vd=[4,4.5,5,5.5,6,6.5,7,7.5,8]
#vd=[4,5,6,7,8]
p=[8580,9150,9749,10440,11050,11580,12280,12910,13500]
error=[2580,2740,2950,3180,3440,3620,3800,3970,4250]
coef=np.polyfit(vd,p,1)
print(coef[0])
print(coef[1])
x=np.linspace(4,8,50)
y=coef[0]*x+coef[1]
###
pylab.figure(1)
pylab.clf()
plt.errorbar(vd,p,error,linestyle=' ',marker='o',color='k',markersize=5)
#plt.plot(x,y,'r')
pylab.xticks(np.arange(4,9,1))
pylab.yticks(np.arange(8000,18000,4000))
pylab.xlabel('$V_d$~(m/s)')
pylab.ylabel('3PV~(N.m)')
pylab.ylim(6000, 18000)
pylab.xlim(4, 8.5)
plt.legend(loc=4)
pylab.grid(True)   
#pylab.savefig('p_vs_vd_225p_g0.eps', format='eps', dpi=600, bbox_inches='tight')



