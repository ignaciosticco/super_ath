import numpy as np 

data1 = np.genfromtxt("data_sort.txt", delimiter = ' ')
data2 = np.genfromtxt("data_sort2.txt", delimiter = ' ')

def compara(data1,data2):
	missing=[]
	len_bc=[]
	i=0
	while i<len(data1[:,0]):
		j=0
		while j<len(data2[:,0]) and data1[i,1]!=data2[j,1]:
			j+=1
		if j+1>len(data2[:,0]):
			missing+=[i]
			len_bc+=[len(data1[:,0])]
		i+=1
	return missing,len_bc

print(compara(data1,data2))
np.savetxt('saida.txt', np.c_[compara(data1,data2)[0],compara(data1,data2)[1]], fmt='%i', delimiter=' ')
