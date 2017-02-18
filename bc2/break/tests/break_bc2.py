import numpy as np
import matplotlib.pyplot as plt
import math
import pylab


def compara(data1,data2):
	missing=[]
	len_bc=[]
	i=0
	while i<len(data1[:,0]):
		j=0
		while j<len(data2[:,0]) and data1[i,1]!=data2[j,1]:
			j+=1
		if j+1>len(data2[:,0]):
			missing+=[i+1]
			len_bc+=[len(data1[:,0])]
		i+=1
	return missing,len_bc

vd=[]
mean_y=[]
std_y=[]
median_y=[]
I=[]

for v in range(2,4):
	v_missing=[]
	v_lenbc=[] 
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
	t_present = t[0]
	while t[i]==t_present:
		i+=1
	bc_i=data[0:i,:]
	bc_i=bc_i[np.argsort(bc_i[:,4])]
	####################
	
	while i<len(t):
		t_present = t[i]
		j=0
		while i+j<len(t) and t[i+j]==t_present:
			j+=1
		bc_f=data[i:i+j,:]
		bc_f=bc_f[np.argsort(bc_f[:, 4])]

		v_missing+=compara(bc_i,bc_f)[0]
		v_lenbc+=compara(bc_i,bc_f)[1]
		bc_i=bc_f
		i=i+j

	np.savetxt('out_ubicbreakbc_1.2_225p_v%s.txt' %v, np.c_[v_missing,v_lenbc], fmt='%i', delimiter=' ')

