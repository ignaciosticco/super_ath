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

print("Calcula la compresion y la velocidad relativa (asociada a Froz) de un individuo")

data = np.genfromtxt("print_comp_vel_225p_1.2m_6.txt",  delimiter = ' ')

id_part = data[:,0]
t= data[:,1]
x = data[:,2]
y = data[:,3]
vx = data[:,4]
vy = data[:,5]
f_desired = data[:,6]
f_social = data[:,7]
f_granular = data[:,8]
bc = data[:,9]


def dist(x1,y1,x2,y2):
	return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))


cant_indiv=225
t_tot= len(t)/cant_indiv
id_tracked=99

time=[]
v_comp=[]
f_roz=[]
end=0
i=0
x_100=0
while i<t_tot and x_100<20:
    compresion = 0
    time+=[t[i*cant_indiv+id_tracked]]
    f_roz+=[f_granular[i*cant_indiv+id_tracked]]
    x_100=x[i*cant_indiv+id_tracked]
    y_100=y[i*cant_indiv+id_tracked]
    #if x_100>20 and end==0:
    #	end=i
    j=0
    while j<cant_indiv:   
		distij=dist(x_100,y_100,x[i*cant_indiv+j],y[i*cant_indiv+j])
		if distij<0.6 and id_part[id_tracked]!=id_part[i*cant_indiv+j]:
			compresion +=(0.6-distij)/2
		j+=1
    v_comp+=[compresion]
    i+=1

#time_end=end*0.05

v_comp = [x / max(v_comp) for x in v_comp]
f_roz = [x / max(f_roz) for x in f_roz]

plt.plot(time,v_comp,'b',label='compress',lw=0.7,zorder=2) 
plt.plot(time,f_roz,'r',label='friction',lw=0.7,zorder=2) 
#plt.plot(1,1,'w.',zorder=3) 
#pylab.xticks(np.arange(0,8,2))
#pylab.yticks(np.arange(20,100,20))
pylab.xlabel('t~(s)')
pylab.ylabel('value~(au)')
#pylab.legend()
#pylab.ylim(20, 80)
#pylab.xlim(0, time_end)
#lgd=plt.legend() 
#lgd.set_visible(True) 
plt.legend(loc=2)
pylab.savefig('comp(t)_1.2m_vd6.eps', format='eps', dpi=300, bbox_inches='tight')


