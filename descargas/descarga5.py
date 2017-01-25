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

data1 = np.genfromtxt('in_print_descarga_225p_v2.5', delimiter = ' ')
data2 = np.genfromtxt('in_print_descarga_225p_v4', delimiter = ' ')
data3 = np.genfromtxt('in_print_descarga_225p_v10', delimiter = ' ')

time=data1[:,0]
evacuated=data1[:,1]
time2=data2[:,0]
evacuated2=data2[:,1]
time3=data3[:,0]
evacuated3=data3[:,1]

### DATA ANALYSIS ###
tau=3
steps=len(time)/tau
i=0
t1=[]
e1=[]
time_step=(time[tau-1]-time[0])/2
lapso=0
lap=[]
while i<steps:
     t1+=[round(time_step+time[i*tau],3)]
     e1+=[np.sum(evacuated[i*tau:i*tau+tau])]
     if np.sum(evacuated[i*tau:i*tau+tau])>2:
          lap+=[round(time_step+time[i*tau]-lapso,3)]     
          lapso=round(time_step+time[i*tau],3)
     i+=1
print(lap[1:])
print(np.mean(lap[1:]))

if (len(time)%tau)!=0:
     t1+=[round(np.mean(time[steps*tau:]),3)]
     e1+=[np.sum(evacuated[steps*tau:])]



steps=len(time2)/tau
i=0
t2=[]
e2=[]
time_step=(time2[tau-1]-time2[0])/2
lapso=0
lap=[]
while i<steps:
     t2+=[round(time_step+time2[i*(tau)],3)]
     e2+=[np.sum(evacuated2[i*tau:i*tau+tau])]
     if np.sum(evacuated2[i*tau:i*tau+tau])>2:
          lap+=[round(time_step+time2[i*tau]-lapso,3)]     
          lapso=round(time_step+time2[i*tau],3)
     i+=1
print(lap[1:])
print(np.mean(lap[1:]))

if (len(time2)%tau)!=0:
     t2+=[round(np.mean(time2[steps*tau:]),3)]
     e2+=[np.sum(evacuated2[steps*tau:])]

steps=len(time3)/tau
i=0
t3=[]
e3=[]
lapso=0
lap=[]
time_step3=(time3[tau-1]-time3[0])/2
while i<steps:
     t3+=[round(time_step+time3[i*(tau)],3)]
     e3+=[np.sum(evacuated3[i*tau:i*tau+tau])]
     if np.sum(evacuated3[i*tau:i*tau+tau])>2:
          lap+=[round(time_step+time3[i*tau]-lapso,3)]     
          lapso=round(time_step+time3[i*tau],3)
     i+=1
print(lap[1:])
print(np.mean(lap[1:]))

if (len(time2)%tau)!=0:
     t3+=[round(np.mean(time3[steps*tau:]),3)]
     e3+=[np.sum(evacuated3[steps*tau:])]



### PLOT  ###

'''
pylab.figure(1)
pylab.clf()
plt.plot(t1,e1,'k',lw=1,zorder=2) 
#pylab.xticks(np.arange(6,14,1))
pylab.yticks(np.arange(0,6,1))
pylab.xlabel('time~(s)')
pylab.ylabel('Number of evacuated')
#pylab.legend()
pylab.ylim(0, 4)
pylab.xlim(0, 25)
#lgd=plt.legend(numpoints=1,handlelength=0.8) 
#lgd.set_visible(True)   
pylab.savefig('test_descarga_225p_v2.5.eps', format='eps', dpi=300, bbox_inches='tight')


pylab.figure(2)
pylab.clf()
plt.plot(t2,e2,'k',lw=1,zorder=2) 
#pylab.xticks(np.arange(6,14,1))
pylab.yticks(np.arange(0,6,1))
pylab.xlabel('time~(s)')
pylab.ylabel('Number of evacuated')
#pylab.legend()
pylab.ylim(0, 4)
pylab.xlim(0, 25)
#lgd=plt.legend(numpoints=1,handlelength=0.8) 
#lgd.set_visible(True)   
pylab.savefig('test_descarga_225p_v4.eps', format='eps', dpi=300, bbox_inches='tight')

pylab.figure(3)
pylab.clf()
plt.plot(t3,e3,'k',lw=1,zorder=2) 
#pylab.xticks(np.arange(6,14,1))
pylab.yticks(np.arange(0,6,1))
pylab.xlabel('time~(s)')
pylab.ylabel('Number of evacuated')
#pylab.legend()
pylab.ylim(0, 4)
pylab.xlim(0, 25)
#lgd=plt.legend(numpoints=1,handlelength=0.8) 
#lgd.set_visible(True)   
pylab.savefig('test_descarga_225p_v10.eps', format='eps', dpi=300, bbox_inches='tight')
'''