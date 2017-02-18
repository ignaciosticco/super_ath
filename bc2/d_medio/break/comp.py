import numpy as np 

a=[3,4,5,10]
b=[5,1,4]

vect_y=[]

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

print(compara(a,b))

indice=compara(a,b)
for x in indice:
	vect_y+=[x+3]
print(vect_y)
