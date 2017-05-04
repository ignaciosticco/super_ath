# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

import matplotlib.pyplot as plt
import pylab
import numpy as np
import math

golden_mean = (math.sqrt(5)-1.0)/2.0       # Aesthetic ratio
fig_width = 3+3/8 			                   # width  in inches
fig_height = fig_width*golden_mean         # height in inches
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

###  DATA  ###

data1 = np.genfromtxt('print_superath_961p_fisf.txt', delimiter = '   ')
data2 = np.genfromtxt('print_superath_529p_fisf.txt', delimiter = '   ')

vd_raw = data1[:,0]
iteracion = data1[:,1]
te_raw = data1[:,2] 
num_iteraciones = 30   # cantidad de iteraciones 
num_vd=10           # cantidad de velocidades de deseo 
vd = []
te = []
terr = []
i = 0
while i<num_vd+1:
     vd+=[vd_raw[i*num_iteraciones]]
     te+=[np.mean(te_raw[i*num_iteraciones:i*num_iteraciones+num_iteraciones])/683]
     terr+=[np.std(te_raw[i*num_iteraciones:i*num_iteraciones+num_iteraciones])/683]
     i+=1


vd_raw2 = data2[:,0]
iteracion2 = data2[:,1]
te_raw2 = data2[:,2] 
num_iteraciones2 = 30   # cantidad de iteraciones 
num_vd2 = 10           # cantidad de velocidades de deseo 
vd2 = []
te2 = []
terr2 = []
i = 0
while i<num_vd2+1:
     vd2+=[vd_raw2[i*num_iteraciones2]]
     te2+=[np.mean(te_raw2[i*num_iteraciones2:i*num_iteraciones2+num_iteraciones2])/376]
     terr2+=[np.std(te_raw2[i*num_iteraciones2:i*num_iteraciones2+num_iteraciones2])/376]
     i+=1


###  PLOT  ###

pylab.figure(1)
pylab.clf()
plt.plot(vd,te,'wo',zorder=3,markeredgecolor='b',label='N=961') 
plt.plot(vd,te,'b',lw=1.0,zorder=2) 
plt.errorbar(vd[::2],te[::2],terr[::2],linestyle='-',fmt='.',color='w',ecolor='k',zorder=1) 

plt.plot(vd2,te2,'bo',zorder=3,markeredgecolor='b',label='N=529') 
plt.plot(vd2,te2,'b',lw=1.0,zorder=2) 
plt.errorbar(vd2[::2],te2[::2],terr2[::2],linestyle='-',fmt='.',color='w',ecolor='k',zorder=1) 

#pylab.xticks(np.arange(0,14,2))
#pylab.yticks(np.arange(20,80,20))
pylab.xlabel('$v_d$~(m/s)')
pylab.ylabel('evacuation time~(s)~/N')
pylab.legend()
#pylab.ylim(10, 40)
#pylab.xlim(0, 8)
lgd=plt.legend(numpoints=1,handlelength=0.8) 
lgd.set_visible(True)
pylab.savefig('fisf_529_961.eps', format='eps', dpi=300, bbox_inches='tight')

