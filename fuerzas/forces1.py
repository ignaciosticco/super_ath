import numpy as np
import matplotlib.pyplot as plt
import math
import pylab

# a dos columnas: 3+3/8 (ancho, in)
# a una columna : 6.5   (ancho  in)

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8                            # width  in inches
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


print("Analizador de Fuerzas")

mean_desired=[]
mean_social=[]
mean_granular=[]

for v in range(2,4,2):
    v=str(v)
    data = np.genfromtxt("print_forces_1.2m_v%s.txt" %v, delimiter = ' ')

    x = data[:,0]
    y = data[:,1]
    f_desired = data[:,2]
    f_social = data[:,3]
    f_granular = data[:,4]
    bc = data[:,5] 

    i = 0
    contador = 0.0
    sum_desired = 0
    sum_social = 0
    sum_granular = 0
    while i<len(data[:,0]):
        if bc[i]>0:
            sum_desired+=f_desired[i]
            sum_social+=f_social[i]
            sum_granular+=f_granular[i]
            contador+=1
        i+=1

    mean_desired+=[round(sum_desired/contador,2)]
    mean_social+=[round(sum_social/contador,2)]
    mean_granular+=[round(sum_granular/contador,2)]
    print(mean_desired)
    print(mean_social)
    print(mean_granular)

    #avg = np.asarray(avg)
    #avg_col= avg.reshape(-1,1)
    #out=np.concatenate((out,avg_col),1) 
    #out=np.matrix.round(out,2)
    


#np.savetxt('out.csv',out,fmt='%2.2f',delimiter = ',')
#plt.plot(1,1,'w.',zorder=3) 
#pylab.xticks(np.arange(0,8,2))
#pylab.yticks(np.arange(20,100,20))
#pylab.xlabel('$v_d$~(m/s)')
#pylab.ylabel('Force')
#pylab.legend()
#pylab.ylim(20, 80)
#pylab.xlim(0, 6)
#lgd=plt.legend() 
#lgd.set_visible(False) 
#pylab.savefig('test_fig.eps', format='eps', dpi=300, bbox_inches='tight')