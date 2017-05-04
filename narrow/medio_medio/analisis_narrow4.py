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
vd=[1.25,2,3,4,5,6,7.5,9,10]
for i in range(0,9):
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

  # central= particula que se mueve 
  x_central_dmedio=[]   # distancia al centro (10,10) del peaton que se mueve (central) 

  x_central=[]
  vx_central=[]
  f_granular_central=[]
  f_social_central=[]
  locals()['t_central_vd{0}'.format(v)]=[]
  locals()['x_central_vd{0}'.format(v)]=[]
  locals()['f_x_central_vd{0}'.format(v)]=[]
  locals()['f_neta_central_vd{0}'.format(v)]=[]

  ## filtrar datos de la particula central ##
  i=0
  suma_vel=0
  #fin=len(vx)/3    # cantidad de timesteps a considerar
  fin=3
  while i<fin:
      x_central_dmedio+=[abs(x[i*3]-10)]
      x_central+=[x[i*3]]
      vx_central+= [vx[i*3]]
      f_granular_central+=[f_granular[i*3]]
      f_social_central+=[f_social[i*3]]
      locals()['t_central_vd{0}'.format(v)]+= [t[i*3]]
      locals()['x_central_vd{0}'.format(v)]+=[x[i*3]]
      locals()['f_x_central_vd{0}'.format(v)]+=[fx[i*3]]
      locals()['f_neta_central_vd{0}'.format(v)]+=[((v-vx[i*3])*m/tau)+f_social[i*3]+campo_externo-f_granular[i*3]] # F neta part central(t)
      i+=1
  index_min = np.argmin(x_central_dmedio)



### Plot ###

#plt.semilogy(t_central_vd2,f_x_central_vd2,'b',label='vd=2',lw=0.7,zorder=2)
#plt.semilogy(t_central_vd4,f_x_central_vd4,'r',label='vd=4',lw=0.7,zorder=2)
#plt.semilogy(t_central_vd7,f_x_central_vd7,'k',label='vd=7.5',lw=0.7,zorder=2)

plt.plot(t_central_vd1,f_x_central_vd1,'orange',label='vd=1.25',lw=0.7,zorder=2)
plt.plot(t_central_vd2,f_x_central_vd2,'b',label='vd=2',lw=0.7,zorder=2)
plt.plot(t_central_vd3,f_x_central_vd3,'c',label='vd=3',lw=0.7,zorder=2)
plt.plot(t_central_vd4,f_x_central_vd4,'r',label='vd=4',lw=0.7,zorder=2)
plt.plot(t_central_vd5,f_x_central_vd5,'g',label='vd=5',lw=0.7,zorder=2)
plt.plot(t_central_vd6,f_x_central_vd6,'y',label='vd=6',lw=0.7,zorder=2)
plt.plot(t_central_vd7,f_x_central_vd7,'k',label='vd=7.5',lw=0.7,zorder=2)
plt.plot(t_central_vd9,f_x_central_vd9,'*c',label='vd=9',lw=0.1,zorder=2)
plt.plot(t_central_vd10,f_x_central_vd10,'m',label='vd=10',lw=0.7,zorder=2)

pylab.xlabel('time~(s)')
pylab.ylabel('f neta~(N)')
plt.grid(False, which="minor")
pylab.xlim(-0.001, 0.005)
pylab.ylim(0, 1000)
plt.legend(loc='center up',labelspacing=0.1,borderpad=0.01,handletextpad=0.05)
pylab.savefig('f(t)_4.eps', format='eps', dpi=300, bbox_inches='tight')