import numpy as np
import matplotlib.pyplot as plt
import math
import pylab

# a dos columnas: 3+3/8 (ancho, in)
# a una columna : 6.5   (ancho  in)

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8                             # width  in inches
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


vd=[2,4,6,8,10,12]

fd = [237.67, 528.15, 809.4, 1086.64, 1363.72, 1641.13]
fs = [3843.44, 9777.38, 13238.88, 16244.58, 19530.94, 22590.13]
fg = [551.44, 2098.81, 3063.42, 4089.38, 5226.74, 6381.01]

peso_rel=[]
i=0
while i<len(vd):
     f_total=fd[i]+fs[i]+fg[i]
     peso_rel+=[fg[i]/f_total]
     i+=1



#plt.plot(vd,fd,'w^',label='desired',zorder=3) 
#plt.plot(vd,fd,'k',lw=1.0,zorder=2) 
#plt.errorbar(vd,te1,yerr1,linestyle='-',fmt='.',color='w',ecolor='k',label='N=225',zorder=1) 

#plt.plot(vd,fs,'ws',label='social',zorder=3) 
#plt.plot(vd,fs,'k',lw=1.0,zorder=2)
#plt.errorbar(vd,te2,yerr2,linestyle='-',marker='.',color='k',label='N=583')

plt.plot(vd,peso_rel,'wo',label='granular',zorder=3) 
plt.plot(vd,peso_rel,'k',lw=1.0,zorder=2)     
#plt.errorbar(vd,te3,yerr3,linestyle='-',marker='.',color='k',label='N=961') 

#pylab.xticks(np.arange(0,8,2))
#pylab.yticks(np.arange(20,100,20))
pylab.xlabel('$v_d$~(m/s)')
pylab.ylabel('Relative weight')
#pylab.legend()
#pylab.ylim(20, 80)
#pylab.xlim(0, 6)

plt.legend(loc="upper left", markerscale=0.6,numpoints=1, fontsize=4)

pylab.savefig('peso_relativo_fg.eps', format='eps', dpi=300, bbox_inches='tight')