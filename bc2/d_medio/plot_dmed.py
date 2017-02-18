# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

import matplotlib.pyplot as plt
import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
#import numarray
from pylab import arange,pi,sin,cos,sqrt,savefig


golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8  			    # width  in inches
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

### DATA

data = np.genfromtxt('out_distbc_225p_1.2m.txt', delimiter = ' ')

vd = data[:,0]
distance = data[:,1]
error = data[:,2]

### PLOT

pylab.figure(1)
pylab.clf()


plt.plot(vd,distance,'wo',zorder=3) 
plt.plot(vd,distance,'k',lw=1.0,zorder=2) 
plt.errorbar(vd,distance,error,linestyle='-',fmt='.',color='w',ecolor='k',label='N=225',zorder=1) 


#pylab.xticks(np.arange(0,8,2))
#pylab.yticks(np.arange(20,100,20))
pylab.xlabel('$v_d$~(m/s)')
pylab.ylabel('Distance~(m)')
pylab.legend()
#pylab.ylim(20, 80)
#pylab.xlim(0, 6)
lgd=plt.legend() 
lgd.set_visible(False)
   
pylab.savefig('distancebc_225p_1.2m.eps', format='eps', dpi=300, bbox_inches='tight')



'''

####################OLD STUFF#########################

#plt.legend(loc=4)
#pylab.grid(True)

#plt.scatter(gap1,te1,marker='o',s=50, color='w', zorder=0)
#plt.axhline(y=31, xmin=0, xmax=8, linewidth=1, color = 'black',ls='dashed')

plt.figure(1)
plt.errorbar(gap1,te1,yerr1,linestyle='',marker='o',color='red',label='vd= 4 m/s ')
plt.errorbar(gap2,te2,yerr2,linestyle='',marker='o',label='vd= 8 m/s')
plt.errorbar(gap3,te3,yerr3,linestyle='',marker='o',color='green',label='N= 961')
#plt.axhline(y=40, xmin=0, xmax=21, linewidth=2, color = 'green')  #linea horizontal
#plt.axvline(1.2,linewidth=2, color='k', linestyle='-')
plt.legend(loc=4)
plt.xlabel('Gap size (m)',fontsize=22)
plt.ylabel('Evacuation Time (s)', fontsize=22)
'''

