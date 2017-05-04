## Este script calcula el cociente de las fuerzas positivas (fs y deseo) y las fuerzas negativas (rozamiento)
## La fuerza social es: campo externo + proyeccion en el eje x. 
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

m=70
tau=0.5

#vd = np.linspace(1,17,17)
vd=[1.75,3.5,11.25]

for i in range(0,3):
  v=str(vd[i])
  data = np.genfromtxt("in_narrow_print_fino_vd%s.txt" %v, delimiter = ' ')
  v=int(vd[i])

  t = data[:,0]
  x = data[:,1]
  y = data[:,2]
  vx = data[:,3]
  vy = data[:,4]
  f_granular = data[:,5]
  f_social = data[:,6]
  fx = data[:,7]
  fy = data[:,8]
  campo_externo=2000.0*vd[i]

  x_central=[]
  vx_central=[]
  f_granular_central=[]
  f_social_central=[]
  f_desired_central=[]

  locals()['t_vd{0}'.format(v)]=[]
  locals()['x_vd{0}'.format(v)]=[]
  locals()['f_x_vd{0}'.format(v)]=[]
  locals()['fmas_fmenos_vd{0}'.format(v)]=[]

  ## filtrar datos de la particula central ##
  i=0
  suma_vel=0
  fin=len(vx)/3    # cantidad de timesteps a considerar
  #fin=3
  while i<fin:
      dist=math.sqrt((x[i*3]-x[1+i*3])**2+(y[i*3]-y[1+i*3])**2)
      nx = (x[i*3]-x[1+i*3])/dist
      x_central+=[x[i*3]]
      vx_central+= [vx[i*3]]
      f_granular_central+=[f_granular[i*3]]
      f_social_central+=[f_social[i*3]*nx+campo_externo]
      f_desired_central+=[(v-vx[i*3])*m/tau]
      locals()['t_vd{0}'.format(v)]+= [t[i*3]]
      locals()['x_vd{0}'.format(v)]+=[x[i*3]]
      locals()['f_x_vd{0}'.format(v)]+=[fx[i*3]]
      i+=1
  i=0
  while i<fin:
    locals()['fmas_fmenos_vd{0}'.format(v)]+=[(f_desired_central[i]+f_social_central[i])/f_granular_central[i]] # cociente de fuerzas que empujan adelante y fuerzas que empujan para atras 
    i+=1
#print(fmas_fmenos_vd2) 
#print(f_desired_central) 
### Plot ###

#plt.semilogy(t_central_vd2,f_x_central_vd2,'b',label='vd=2',lw=0.7,zorder=2)

plt.plot(t_vd1,fmas_fmenos_vd1,'b',label='vd=1.75',lw=0.7,zorder=2)
plt.plot(t_vd3,fmas_fmenos_vd3,'r',label='vd=3.5',lw=0.7,zorder=2)
plt.plot(t_vd11,fmas_fmenos_vd11,'g',label='vd=11.25',lw=0.7,zorder=2)


pylab.xlabel('time~(s)')
pylab.ylabel('cociente $f+\_f-$')
plt.grid(False, which="minor")
pylab.xlim(0.71, 0.72)
#pylab.ylim(0, 1000)
plt.legend(loc='left up',labelspacing=0.1,borderpad=0.01,handletextpad=0.05)
pylab.savefig('cociente(t)_2.eps', format='eps', dpi=300, bbox_inches='tight')