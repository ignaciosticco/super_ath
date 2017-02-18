import numpy as np
import matplotlib.pyplot as plt
import math
import pylab


def compara(vi,vf):
	index=[]
	i=0
	while i<len(vi):
		j=0
		while j<len(vf) and vi[i]!=vf[j]:
			j+=1
		if j+1>len(vf):
			index+=[i]
		i+=1
	return index

vd=[]
mean_y=[]
std_y=[]
median_y=[]

for v in range(2,4):
	vd+=[v]
	v=str(v)
	data = np.genfromtxt("print_bcdata_225p_1.2m_%s.txt" %v, delimiter = ' ')
	label=data[:,1]
	t = data[:,2]
	x = data[:,3]
	y = data[:,4]
	vect_y=[]

	#### Inicializo ####
	i=0
	bc_i=[]
	t_present = t[0]
	while t[i]==t_present:
		bc_i+=[label[i]]
		i+=1
	####################

	while i<len(t):
		bc_f=[]
		t_present = t[i]
		j=0
		while i+j<len(t) and t[i+j]==t_present:
			bc_f+=[label[i+j]]
			j+=1
		indice=compara(bc_i,bc_f)   # Vector de labels de los indiv que faltan en bc_f
		for x in indice:
			vect_y+=[y[i-len(bc_i)+x]]
		bc_i=bc_f
		i=i+j

	np.savetxt('out_positiony_v%s.txt' %v, vect_y, fmt='%2.2f', delimiter=' ')
	mean_y+=[np.mean(vect_y)]
	std_y+=[np.std(vect_y)]
	median_y+=[np.median(vect_y)]



#print(mean_dist)
#print(std_dist)
np.savetxt('out.txt', np.c_[vd,mean_y,std_y,median_y], fmt='%2.2f', delimiter=' ')


