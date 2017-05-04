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

data = np.genfromtxt("in_narrow_print_vd2.txt",  delimiter = ' ')
data4 = np.genfromtxt("in_narrow_print_vd4.txt",  delimiter = ' ')
data10 = np.genfromtxt("in_narrow_print_vd10.txt",  delimiter = ' ')


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
t_central=[]
f_roz=[]

i=0
suma_vel=0
while i<len(vx)/3:
  x_central+=[x[i*3]]
  t_central+=[t[i*3]]
  vx_central+= [vx[i*3]]
  f_roz+=[f_granular[i*3]]
  i+=1

#### vd=4 #######
t4= data4[:,0]
x4 = data4[:,1]
y4 = data4[:,2]
vx4 = data4[:,3]
vy4 = data4[:,4]
f_granular4 = data4[:,5]
f_social4 = data4[:,6]
fx4 = data4[:,7]
fy4 = data4[:,8]

x_central4=[]
vx_central4=[]
t_central4=[]
f_roz4=[]

i=0
suma_vel4=0
while i<len(vx4)/3:
  x_central4+=[x4[i*3]]
  t_central4+=[t4[i*3]]
  vx_central4+= [vx4[i*3]]
  f_roz4+=[f_granular4[i*3]]
  i+=1

#### vd=10 #######
t10= data10[:,0]
x10 = data10[:,1]
y10 = data10[:,2]
vx10 = data10[:,3]
vy10 = data10[:,4]
f_granular10 = data10[:,5]
f_social10 = data10[:,6]
fx10 = data10[:,7]
fy10 = data10[:,8]

x_central10=[]
vx_central10=[]
t_central10=[]
f_roz10=[]

i=0
suma_vel4=0
while i<len(vx10)/3:
  x_central10+=[x10[i*3]]
  t_central10+=[t10[i*3]]
  vx_central10+= [vx10[i*3]]
  f_roz10+=[f_granular10[i*3]]
  i+=1


print(len(t_central),len(vx_central))
print(len(t_central4),len(vx_central4))
print(len(t_central10),len(vx_central10))
#plt.plot(t_central,vx_central,'b',label='speed',lw=0.7,zorder=2) 
#plt.plot(t_central,vx_central,'b',label='speed',lw=0.7,zorder=2) 
plt.plot(t_central,vx_central,'b',label='$v_d=2m/s$',lw=0.7,zorder=2)
plt.plot(t_central4,vx_central4,'r',label='$v_d=4m/s$',lw=0.7,zorder=2) 
plt.plot(t_central10,vx_central10,'k',label='$v_d=10m/s$',lw=0.7,zorder=2)
plt.yscale('log')
plt.grid(False, which='minor')
#plt.plot(1,1,'w.',zorder=3) 
#pylab.xticks(np.arange(0,8,2))
#pylab.yticks(np.arange(20,100,20))
pylab.xlabel('t~(s)')
pylab.ylabel('speed~(m/s)')
#pylab.legend()
#pylab.xlim(0, 3)
#pylab.ylim(0.1, 100)
#lgd=plt.legend() 
#lgd.set_visible(True) 
plt.legend(loc=2,labelspacing=0.2,borderpad=0.1,handletextpad=0.1)
pylab.savefig('speed(t)_out.eps', format='eps', dpi=300, bbox_inches='tight')