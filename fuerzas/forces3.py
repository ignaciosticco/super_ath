import numpy as np
import matplotlib.pyplot as plt
import math

print("Analizador de Fuerzas")

mean_desired=[]
mean_social=[]
mean_granular=[]

for v in range(2,18):
    v=str(v)
    data = np.genfromtxt("print_bcdata_225p_1.2m_bis_vd%s.txt" %v, delimiter = ' ')

    dijkstra = data[:,0]
    label = data[:,1]
    t = data[:,2]
    x = data[:,3]
    y = data[:,4]
    fd = data[:,5] # Desired force
    fs = data[:,6] # Social force
    fg = data[:,7] # Granular force

    i = 0
    contador = 0.0
    sum_desired = 0
    sum_social = 0
    sum_granular = 0
    while i<len(t):
        sum_desired+=fd[i]
        sum_social+=fs[i]
        sum_granular+=fg[i]
        contador+=1
        i+=1

    mean_desired+=[round(sum_desired/contador,2)]
    mean_social+=[round(sum_social/contador,2)]
    mean_granular+=[round(sum_granular/contador,2)]

np.savetxt('out_forces_225p_1.2m_bcok.txt', np.c_[mean_desired,mean_social,mean_granular], fmt='%2.2f')
print(mean_desired)
print(mean_social)
print(mean_granular)

