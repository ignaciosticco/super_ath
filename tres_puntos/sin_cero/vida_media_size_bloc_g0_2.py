import matplotlib.pyplot as plt
import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import arange,pi,sin,cos,sqrt,savefig

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8 			 			    # width  in inches
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

print("Calcula la vida media de los blocking clusters y el tamano de los BC")

data = np.genfromtxt("in_print_225p_g0_v2.5_block.txt",  delimiter = ' ')

time = data[:,0]
bc = data[:,1]
print('block:',data[:,1])

def t_medio(bc):
	acumulador=0
	tiempos_bloc=[]
	i=0
	while i<len(bc):
		if bc[i]!=0:
			acumulador+=1
		elif acumulador!=0:
			tiempos_bloc+=[acumulador]
			acumulador=0
		else:
			pass
		i+=1
	tiempo_bloc_medio=np.mean(tiempos_bloc)
	error = np.std(tiempos_bloc)
	tiempos_bloc = [i*0.05 for i in tiempos_bloc] 
	return tiempo_bloc_medio, error, tiempos_bloc 

## Crea un vector con la cantidad de peatones en cada BC (excluyendo los casos nulos) ##
bc2=[]
i=0
while i <len(bc):
	if bc[i]>0:
		bc2+=[bc[i]]
	i+=1


print('Tiempo de vida medio: ',t_medio(bc)[0]*0.05)
print('Desvio standard: ',t_medio(bc)[1]*0.05)

print('     ')

print('Size medio de BC: ',np.mean(bc2))
print('Error size BC: ',np.std(bc2))

### PLOT  ###

### Histograma de size ###
pylab.figure(1)
pylab.clf()
plt.hist(bc2,bins=40) 
pylab.xlim(0,40)
plt.xlabel('BC size (number of pedestrians)')
plt.ylabel('Ocurrence')
plt.savefig('bc_size_225p_v2.5_g0_s0_bis.eps', format='eps', dpi=300, bbox_inches='tight')


### Histograma de tiempo de vida medio ###
pylab.figure(2)
pylab.clf()
#plt.hist(t_medio(bc)[2], range=(0.01,max(t_medio(bc)[2])), bins='auto') 
pylab.xlim(0,2)
plt.xlabel('BC life (s)')
plt.ylabel('Ocurrence')
#plt.savefig('bc_time_225p_v10_g0_s0.eps', format='eps', dpi=300, bbox_inches='tight')