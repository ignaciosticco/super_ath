# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

import matplotlib.pyplot as plt
import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
#import numarray
from pylab import arange,pi,sin,cos,sqrt,savefig

# a dos columnas: 3+3/8 (ancho, in)
# a una columna : 6.5   (ancho  in)

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8 			    # width  in inches
fig_height = fig_width*golden_mean          # height in inches
fig_size =  [fig_width,fig_height]

params = {'backend': 'ps',
          'axes.titlesize': 8,
          'axes.labelsize': 9,
          'axes.linewidth': 0.5, 
          'axes.grid': True,
          'axes.labelweight': 'normal',  
          'font.family': 'serif',
          'font.size': 8.0,
          'font.weight': 'normal',
          'text.color': 'black',
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'legend.fontsize': 8,
          'figure.dpi': 300,
          'figure.figsize': fig_size,
          'savefig.dpi': 300,
         }

pylab.rcParams.update(params)

### DATA ###


data1 = np.genfromtxt('in_print_compresion_helbing_g0.txt', delimiter = '   ')

vd1=data1[:,0]
te1 =data1[:,2]


num_vel1=11   # Cantidad de velocidades del data1
terr1=[]
tee1=[]
for i in range(0,num_vel1):
  tee1+=[np.mean(te1[30*i:30*i+29])]
  terr1+=[np.std(te1[30*i:30*i+29])]
vd1=np.linspace(1,11,11) 

for i in range(0,len(terr1)):
  if (i+1)%3 != 0:
    terr1[i]=0

### PLOT  ###

pylab.figure(1)
pylab.clf()


plt.plot(vd1,tee1,'w^',label='225 p',zorder=3) 
plt.plot(vd1,tee1,'k',lw=1.0,zorder=2) 
plt.errorbar(vd1,tee1,terr1,linestyle='-',fmt='.',color='w',ecolor='k',zorder=1) 

#pylab.xticks(np.arange(6,14,1))
#pylab.yticks(np.arange(0.1,0.3,0.05))
pylab.xlabel('$v_d$~(m/s)')
pylab.ylabel('evacuation time~(s)')
pylab.legend()
#pylab.ylim(0.05, 0.2)
#pylab.xlim(8, 12.3)

lgd=plt.legend(numpoints=1,handlelength=0.8) 
lgd.set_visible(True)
   
pylab.savefig('fis_compresion_helbing1.eps', format='eps', dpi=300, bbox_inches='tight')

