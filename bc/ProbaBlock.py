import numpy as np
#import matplotlib.pyplot as plt
import math

# Programa que toma los archivos txt para cada gap (archivos con timestep y numero de individuos que forman un blocking cluster en cada puerta (small) y en ambas (big)) y devuelve una tabla con gap, proba big,proba small up, proba small down.  La probabilidad de formar un cluster de bloqueo

print("Datos para obtener g vs numero de clusters de bloqueo/cant_timestep.")

data = np.genfromtxt("in_print_225p_v4_block_door3.6.txt", delimiter = ' ')

bc=data[:,1]
i=0
cant_bc=0
while(i<len(bc)):
    if bc[i]>0:
        cant_bc+=1
    i=i+1

# proba de formar un blocking cluster (cant de timestep con block/cant total de timesteps)
proba_bc=cant_bc/float(len(bc))
print('Proba Bc:',proba_bc)