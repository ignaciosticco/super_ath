# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html
import matplotlib.pyplot as plt
import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import arange,pi,sin,cos,sqrt,savefig
golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8 			    # width  in inches
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

### DATA ###

data1 = np.genfromtxt('in_print_descarga_225p_v4', delimiter = ' ')

time=data1[:,0]
evacuated=data1[:,1]

#####################
#   DATA ANALYSIS   #
#####################


def evac_vst(tau):
     steps=len(time)/tau
     i=0
     t1=[]
     e1=[]
     time_step = (time[tau-1]-time[0])/2
     lapso=0
     lap=[]
     while i<steps:
          t1+=[round(time_step+time[i*tau],3)]
          e1+=[np.sum(evacuated[i*tau:i*tau+tau])]
          i+=1
     ## Para agregar los ultimos valores
     if (len(time)%tau)!=0:
          t1+=[round(np.mean(time[steps*tau:]),3)]
          e1+=[np.sum(evacuated[steps*tau:])]
     return t1,e1

def avalanchas(tau):
     t1 = evac_vst(tau)[0]
     e1 = evac_vst(tau)[1]
     i=0
     contador = 0
     avalancha_size=[]
     num_avalancha=0

     while i<len(e1):
          if e1[i]>0:
               contador+=1
          elif i>0 and e1[i]==0 and e1[i-1]>0:
               avalancha_size+=[contador]
               num_avalancha +=1
               contador = 0
          else: 
               contador = 0
          
          i+=1
     return num_avalancha, avalancha_size

print(avalanchas(10))

def burst(begin, end):
     burst=[]
     vector_tau=[]
     for tau in range(begin,end+1):
          burst+=[avalanchas(tau)[0]]
          vector_tau+=[tau*0.05]
     return vector_tau, burst
print(burst(1, 24))

tau = burst(1, 24)[0]
burst = burst(1, 24)[1]


### PLOT  ###


pylab.figure(1)
pylab.clf()
plt.plot(tau,burst,'ok',markersize=4,zorder=2) 
#pylab.xticks(np.arange(6,14,1))
#pylab.yticks(np.arange(0,6,1))
pylab.xlabel('Tau~(s)')
pylab.ylabel('Number of burst')
#pylab.legend()
pylab.ylim(0, 120)
#pylab.xlim(0, 120)
#lgd=plt.legend(numpoints=1,handlelength=0.8) 
#lgd.set_visible(True)   
pylab.savefig('tau_vs_burst_225p_v4_g0.eps', format='eps', dpi=300, bbox_inches='tight')
