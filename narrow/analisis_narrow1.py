# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

import matplotlib.pyplot as plt
import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import arange,pi,sin,cos,sqrt,savefig

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8 			 			    # width  in inches
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

print("Calcula v(t) de la particula central de narrow")

data = np.genfromtxt("in_narrow_print_vd17.txt",  delimiter = ' ')

t= data[:,0]
x = data[:,1]
y = data[:,2]
vx = data[:,3]
vy = data[:,4]
f_granular = data[:,5]
f_social = data[:,6]
fx = data[:,7]
fy = data[:,8]

x_central=[]
vx_central=[]
t_cental=[]
f_roz=[]

i=0
suma_vel=0
while i<len(vx)/3:
  x_central+=[x[i*3]]
  vx_central+= [vx[i*3]]
  t_cental+= [t[i*3]]
  f_roz+=[f_granular[i*3]]
  i+=1


#plt.plot(t_cental,vx_central,'b',label='speed',lw=0.7,zorder=2) 
#plt.plot(t_cental,f_roz,'b',label='speed',lw=0.7,zorder=2) 
plt.plot(t_cental,x_central,'b',label='speed',lw=0.7,zorder=2)
#plt.plot(time,f_roz,'r',label='friction',lw=0.7,zorder=2) 
#plt.plot(time,v_speed_100,'g',label='speed',lw=0.7,zorder=2) 
#plt.plot(1,1,'w.',zorder=3) 
#pylab.xticks(np.arange(0,8,2))
#pylab.yticks(np.arange(20,100,20))
pylab.xlabel('t~(s)')
pylab.ylabel('speed~(m/s)')
#pylab.legend()
pylab.xlim(0, 3)
#pylab.ylim(0, 25)
#lgd=plt.legend() 
#lgd.set_visible(True) 
#plt.legend(loc=2,labelspacing=0.2,borderpad=0.1,handletextpad=0.1)
pylab.savefig('x(t)narrow_vd17.eps', format='eps', dpi=300, bbox_inches='tight')
