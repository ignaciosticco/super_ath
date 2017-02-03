# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

import matplotlib.pyplot as plt
import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
#import numarray
from pylab import arange,pi,sin,cos,sqrt,savefig

# a dos columnas: 3+3/8 (ancho, in)
# a una columna : 6.5   (ancho  in)

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

### DATA

data1 = np.genfromtxt('fig7_version0_in_print_225personas.txt', delimiter = '   ')
data2 = np.genfromtxt('in_print_fis_225p_g0.txt', delimiter = '   ')
data3 = np.genfromtxt('in_print_fis_225p_g0_v8_v12.txt', delimiter = '   ')
data4 = np.genfromtxt('in_print_fis_225p_g1_ath2.txt', delimiter = '  ')

data5 = np.genfromtxt('in_print_compresion_helbing_g0.txt', delimiter = '   ')


vd1 =data1[:,1]
te1 =data1[:,3]
vd2 =data1[:,1]
te2 =data1[:,3]
vd3 =data1[:,1]
te3 =data1[:,3]

vd4=data2[:,1]
te4 =data2[:,3]
vd5=data3[:,1]
te5 =data3[:,3]
vd6=data4[:,1]
te6=data4[:,3]

n=690

vdd1=np.zeros(n)
tee1=np.zeros(n)
vddd1=np.zeros(n/30)
teee1=np.zeros(n/30)
terr1=np.zeros(n/30)
vdd2=np.zeros(n)
tee2=np.zeros(n)
vddd2=np.zeros(n/30)
teee2=np.zeros(n/30)
terr2=np.zeros(n/30)
vdd3=np.zeros(n)
tee3=np.zeros(n)
vddd3=np.zeros(n/30)
teee3=np.zeros(n/30)
terr3=np.zeros(n/30)

vdd1[0:n-1]=vd1[0:n-1]		# gap=0
tee1[0:n-1]=te1[0:n-1]		# gap=0
vdd2[0:n-1]=vd2[1381:1381+n-1]	# gap=1
tee2[0:n-1]=te2[1381:1381+n-1]	# gap=1
vdd3[0:n-1]=vd2[2761:2761+n-1]	# gap=2
tee3[0:n-1]=te2[2761:2761+n-1]	# gap=2

j=0
for i in range(0,n/30):
	vddd1[j]=np.mean(vdd1[30*i:30*i+29])
        teee1[j]=np.mean(tee1[30*i:30*i+29])
	terr1[j]=np.std(tee1[30*i:30*i+29])
	vddd2[j]=np.mean(vdd2[30*i:30*i+29])
        teee2[j]=np.mean(tee2[30*i:30*i+29])
	terr2[j]=np.std(tee2[30*i:30*i+29])
	vddd3[j]=np.mean(vdd3[30*i:30*i+29])
	teee3[j]=np.mean(tee3[30*i:30*i+29])
	terr3[j]=np.std(tee3[30*i:30*i+29])
	j=j+1

### Nueva info a pedido del referee ###
num_vel=9
terr4=[]
tee4=[]
for i in range(0,num_vel):
  tee4+=[np.mean(te4[30*i:30*i+29])]
  terr4+=[np.std(te4[30*i:30*i+29])]
vd4=np.linspace(6,8,9) 
#print(len(vd4),len(tee4),len(terr4))

num_vel=16
terr5=[]
tee5=[]
for i in range(0,num_vel):
  tee5+=[np.mean(te5[30*i:30*i+29])]
  terr5+=[np.std(te5[30*i:30*i+29])]
vd5=np.linspace(8.25,12,16) 
#print(len(vd5),len(tee5),len(terr5))

num_vel=5
terr6=[]
tee6=[]
for i in range(0,num_vel):
  tee6+=[np.mean(te6[30*i:30*i+29])]
  terr6+=[np.std(te6[30*i:30*i+29])]
vd6=[6,7,8,10,12]
print(len(vd6),len(tee6),len(terr6))

### ####

for i in range(0,len(terr1)):
	if (i+1)%3 != 0:
		terr1[i]=0

for i in range(0,len(terr2)):
	if (i+1)%3 != 0:
		terr2[i]=0

for i in range(0,len(terr3)):
	if (i+1)%3 != 0:
		terr3[i]=0

for i in range(0,len(terr4)):
  if (i+1)%3 != 0:
    terr4[i]=0


for i in range(0,len(terr5)):
  if (i+1)%3 != 0:
    terr5[i]=0



vd7=data5[:,0]
te7 =data5[:,2]


num_vel7=20   # Cantidad de velocidades del data1
terr7=[]
tee7=[]
for i in range(0,num_vel7):
  tee7+=[np.mean(te7[30*i:30*i+29])]
  terr7+=[np.std(te7[30*i:30*i+29])]
vd7=np.linspace(1,20,20) 

for i in range(0,len(terr7)):
  if (i+1)%3 != 0:
    terr7[i]=0

#for i in range(0,len(terr6)):
#  if (i+1)%3 != 0:
#    terr6[i]=0


### PLOT

pylab.figure(1)
pylab.clf()

plt.plot(vddd1,teee1,'w^',zorder=3,label='Sin comp') 
plt.plot(vddd1,teee1,'k',lw=1.0,zorder=2) 
plt.errorbar(vddd1,teee1,terr1,linestyle='-',fmt='.',color='w',ecolor='k',zorder=1) 

#plt.plot(vddd2,teee2,'wo',zorder=3,label='$d_g$=1~m') 
#plt.plot(vddd2,teee2,'k',lw=1.0,zorder=2) 
#plt.errorbar(vddd2,teee2,terr2,linestyle='-',fmt='.',color='w',ecolor='k',zorder=1) 


plt.plot(vd4,tee4,'w^',zorder=3) 
plt.plot(vd4,tee4,'k',lw=1.0,zorder=2) 
plt.errorbar(vd4,tee4,terr4,linestyle='-',fmt='.',color='w',ecolor='k',zorder=1) 

plt.plot(vd5,tee5,'w^',zorder=3) 
plt.plot(vd5,tee5,'k',lw=1.0,zorder=2) 
plt.errorbar(vd5,tee5,terr5,linestyle='-',fmt='.',color='w',ecolor='k',zorder=1) 


#plt.plot(vd6,tee6,'wo',zorder=3) 
#plt.plot(vd6,tee6,'k',lw=1.0,zorder=2) 
#plt.errorbar(vd6,te6,tee6,linestyle='-',fmt='.',color='w',ecolor='k',zorder=1) 


plt.plot(vd7,tee7,'wo',label='Con comp',zorder=3) 
plt.plot(vd7,tee7,'k',lw=1.0,zorder=2) 
plt.errorbar(vd7,tee7,terr7,linestyle='-',fmt='.',color='w',ecolor='k',zorder=1) 


#pylab.xticks(np.arange(0,14,2))
#pylab.yticks(np.arange(20,80,20))
pylab.xlabel('$v_d$~(m/s)')
pylab.ylabel('evacuation time~(s)')
pylab.legend()
pylab.ylim(10, 40)
#pylab.xlim(0, 8)

lgd=plt.legend(numpoints=1,handlelength=0.8) 
lgd.set_visible(True)
   
pylab.savefig('fis_g_test2.eps', format='eps', dpi=300, bbox_inches='tight')

