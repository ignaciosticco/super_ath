import matplotlib.pyplot as plt
import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import arange,pi,sin,cos,sqrt,savefig

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8                           # width  in inches
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

# medio= alude a el punto (x=10,y=10)
t_medio = []
x_medio = []
vx_medio = [] 
f_granular_medio = []
f_social_medio = []
f_desered_medio = []
f_desired_medio=[]
f_neta=[]
comp=[]

m=70
tau=0.5

#vd = np.linspace(1,17,17)
te=[]
vd=np.linspace(2,12,11)

for i in range(0,11):
  v=str(int(vd[i]))
  data = np.genfromtxt("in_narrow_print_fino_vd%s.txt" %v, delimiter = ' ')
  v=int(v)

  t = data[:,0]
  x = data[:,1]
  y = data[:,2]
  vx = data[:,3]
  vy = data[:,4]
  f_granular = data[:,5]
  f_social = data[:,6]
  fx = data[:,7]
  fy = data[:,8]

  te+=[t[len(t)-1]]

### Plot ###

print(len(vd), len(te))
plt.plot(vd,te,'ob',lw=0.7,zorder=2)
pylab.xlabel('vd~(m/s)')
pylab.ylabel('te~(s)')
#pylab.xlim(2, 18)
#pylab.ylim(0, 0.5)
plt.legend(loc='mid right',labelspacing=0.2,borderpad=0.1,handletextpad=0.1)
pylab.savefig('te(vd)_narrow_medio_medio.eps', format='eps', dpi=300, bbox_inches='tight')