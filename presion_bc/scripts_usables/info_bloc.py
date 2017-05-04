import numpy as np
import matplotlib.pyplot as plt
import math

data = np.genfromtxt('in.bloc_info_225p_v7.5_g0', delimiter = ' ')


speed = data[:,2]
pressure = data[:,3]

def variables_promedio(data):
	#i=250*10  # num_indiv*cantidad de iter hasta 5000 (para sacar los primeros 5s)
	p = []
	v = []	
	i=0																																												
	while i<len(pressure):
		if speed[i]!=0:
			p+=[pressure[i]]
			v+=[speed[i]]
		i+=1

	avg_v = np.mean(v)
	std_v = np.std(v)
	avg_v = "%.2f" % avg_v
	avg_v = float(avg_v)	
	std_v = "%.2f" % std_v
	std_v = float(std_v)	

	
	avg_p = np.mean(p)
	std_p = np.std(p)
	avg_p = "%.2f" % avg_p
	avg_p = float(avg_p)
	std_p = "%.2f" % std_p
	std_p = float(std_p)

	out = [avg_v,std_v,avg_p,std_p]
	return out

print(variables_promedio(data))

	
