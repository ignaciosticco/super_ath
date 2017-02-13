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


def delay(time,evacuated):
     i=0
     j=0
     v_delay=[]
     while i<len(time):
          if evacuated[i]==0:
               j+=1
          elif evacuated[i]>0 and evacuated[i-1]==0:
               v_delay+=[j]
               j=0
          else:
               j=0
          i+=1
     return v_delay,len(v_delay)


#print(delay(time,evacuated))

delay=delay(time,evacuated)[0]
for i in range(len(delay)):
     delay[i]=delay[i]*0.05

print(np.sum(delay))
print(delay)


fft = np.fft.fft(delay,10)
### PLOT  ###


pylab.figure(1)
pylab.clf()
plt.plot(fft,markersize=4,zorder=2) 
#pylab.xticks(np.arange(6,14,1))
#pylab.yticks(np.arange(0,6,1))
#pylab.xlabel('Tau~(s)')
pylab.ylabel('fft')
#pylab.legend()
#pylab.ylim(0, 1.6)
#pylab.xlim(0, 120)
#lgd=plt.legend(numpoints=1,handlelength=0.8) 
#lgd.set_visible(True)   
pylab.savefig('fft_delay_225p_v4.eps', format='eps', dpi=300, bbox_inches='tight')
