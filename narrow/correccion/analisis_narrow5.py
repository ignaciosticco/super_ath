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

'''
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
'''


m=70
tau=0.5


#vd = np.linspace(1,17,17)
vd=[2,4,10]
for i in range(0,3):
  v=str(vd[i])
  data = np.genfromtxt("in_narrow_print_vd%s.txt" %v, delimiter = ' ')
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
  campo_externo=2000.0*vd[i]

  # central= particula que se mueve 
  x_central_dmedio=[]   # distancia al centro (10,10) del peaton que se mueve (central) 

  x_central=[]
  vx_central=[]
  locals()['t_central_vd{0}'.format(v)]=[]
  locals()['x_central_vd{0}'.format(v)]=[]
  f_granular_central=[]
  f_social_central=[]
  f_desired_central=[]
  locals()['dif_relativa_vd{0}'.format(v)]=[]
  locals()['fx_vd{0}'.format(v)]=[]



  ## filtrar datos de la particula central ##
  i=0
  suma_vel=0
  while i<len(vx)/3:
      x_central_dmedio+=[abs(x[i*3]-10)]
      x_central+=[x[i*3]]
      locals()['x_central_vd{0}'.format(v)]+= [x[i*3]]
      vx_central+= [vx[i*3]]
      f_desired_central+= [(v-vx[i*3])*m/tau]
      locals()['t_central_vd{0}'.format(v)]+= [t[i*3]]
      locals()['fx_vd{0}'.format(v)]+= [abs(fx[i*3])]
      f_granular_central+=[f_granular[i*3]]
      f_social_central+=[f_social[i*3]+campo_externo]
      locals()['dif_relativa_vd{0}'.format(v)]+=[(((v-vx[i*3])*m/tau)-f_granular[i*3])/(((v-vx[i*3])*m/tau)+f_granular[i*3])] # F neta part central(t)
      i+=1
  #index_min = np.argmin(x_central_dmedio)


#print(f_neta_central_vd2)
### Plot ###

plt.semilogy(x_central_vd2,fx_vd2,'k',label='$v_d=2m/s$',lw=0.7,zorder=2)
plt.semilogy(x_central_vd4,fx_vd4,'g',label='$v_d=4m/s$',lw=0.7,zorder=2)
plt.semilogy(x_central_vd10,fx_vd10,'r',label='$v_d=10m/s$',lw=0.7,zorder=2)


pylab.xlabel('x~(m)')
pylab.ylabel('fx~(N)')
pylab.xlim(9.5, 10.5)
#pylab.ylim(10, 100000)
plt.grid(False)
plt.legend(loc='mid right',labelspacing=0.2,borderpad=0.1,handletextpad=0.1)
pylab.savefig('dif_desired_roz.eps', format='eps', dpi=300, bbox_inches='tight')