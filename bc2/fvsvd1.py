import numpy as np
import matplotlib.pyplot as plt
import math
import pylab
print("Analizador de Fuerzas")

mean_desired=[]
mean_social=[]
mean_granular=[]

for v in range(2,13):
    v=str(v)
    data = np.genfromtxt("print_bcdata_225p_1.2m_%s.txt" %v, delimiter = ' ')

    x = data[:,3]
    y = data[:,4]
    f_desired = data[:,5]
    f_social = data[:,6]
    f_granular = data[:,7]

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

np.savetxt('out_forcesvd_bc_1.2m_225p.txt', np.c_[mean_desired,mean_social,mean_granular], fmt='%2.2f', delimiter=' ')
