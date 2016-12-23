# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html
import matplotlib.pyplot as plt
import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import arange,pi,sin,cos,sqrt,savefig
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

data1 = np.genfromtxt('in_print_descarga_961p_v2.5', delimiter = ' ')
data2 = np.genfromtxt('in_print_descarga_961p_v10.txt', delimiter = ' ')

time=data1[:,0]
evacuated=data1[:,1]
time2=data2[:,0]
evacuated2=data2[:,1]


### PLOT  ###

pylab.figure(1)
pylab.clf()

#plt.plot(time,evacuated,'wo',zorder=3) 
plt.plot(time,evacuated,'k',lw=0.5,zorder=2) 
#plt.errorbar(vd2,tee2,terr2,linestyle='-',fmt='.',color='w',ecolor='k',zorder=1)

#plt.plot(time,evacuated,'wo',zorder=3) 
#plt.plot(time2,evacuated2,'k',lw=0.5,zorder=2) 
#plt.errorbar(vd2,tee2,terr2,linestyle='-',fmt='.',color='w',ecolor='k',zorder=1)



#pylab.xticks(np.arange(6,14,1))
pylab.yticks(np.arange(0,4,1))
pylab.xlabel('time~(s)')
pylab.ylabel('Number of evacuated')
#pylab.legend()
#pylab.ylim(0.05, 0.2)
pylab.xlim(40, 60)

#lgd=plt.legend(numpoints=1,handlelength=0.8) 
#lgd.set_visible(True)
   
pylab.savefig('descarga_961p_v2.5.eps', format='eps', dpi=300, bbox_inches='tight')
#pylab.savefig('descarga_961p_v10.eps', format='eps', dpi=300, bbox_inches='tight')

