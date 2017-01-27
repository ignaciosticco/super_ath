import numpy as np
import matplotlib.pyplot as plt
import math
import pylab

# a dos columnas: 3+3/8 (ancho, in)
# a una columna : 6.5   (ancho  in)

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8                            # width  in inches
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


print("F(t)")

mean_desired=[]
mean_social=[]
mean_granular=[]

data = np.genfromtxt("print_forces_1.2m_v10.txt", delimiter = ' ')

x = data[:,0]
y = data[:,1]
f_desired = data[:,2]
f_social = data[:,3]
f_granular = data[:,4]
bc = data[:,5] 
t=np.linspace(0,len(x)*0.05,len(x))



plt.plot(t,f_desired,'k',lw=1.0,zorder=2)  
plt.plot(t,f_granular,'b',lw=1.0,zorder=2)  
plt.plot(t,f_social,'r',lw=1.0,zorder=2)  

#plt.plot(1,1,'w.',zorder=3) 
#pylab.xticks(np.arange(0,8,2))
#pylab.yticks(np.arange(20,100,20))
#pylab.xlabel('$v_d$~(m/s)')
#pylab.ylabel('Force')
#pylab.legend()
#pylab.ylim(20, 80)
#pylab.xlim(0, 6)
#lgd=plt.legend() 
#lgd.set_visible(False) 
pylab.savefig('f(t)_1.2m.eps', format='eps', dpi=300, bbox_inches='tight')