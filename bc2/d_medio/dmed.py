import numpy as np
import matplotlib.pyplot as plt
import math
import pylab

vd=[]
mean_dist=[]
std_dist=[]


def dist(x1,y1,x2,y2):
	dist=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
	return dist


for v in range(2,4):
	vd+=[v]
	v=str(v)
	data = np.genfromtxt("print_bcdata_225p_1.2m_%s.txt" %v, delimiter = ' ')
	t = data[:,2]
	x = data[:,3]
	y = data[:,4]

	tocados=[]

	i=0
	while i<len(t):
		t_present = t[i]
		j=1
		while i+j<len(t) and t[i+j]==t_present:
			d=dist(x[i],y[i],x[i+j],y[i+j])
			if d<0.6:
				tocados+=[d]
			j+=1
		i+=1

	mean_dist+=[np.mean(tocados)]
	std_dist+=[np.std(tocados)]


#print(mean_dist)
#print(std_dist)
np.savetxt('out_distbc_225p_1.2m.txt', np.c_[vd,mean_dist,std_dist], fmt='%2.3f', delimiter=' ')

