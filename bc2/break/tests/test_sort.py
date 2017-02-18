import numpy as np
import matplotlib.pyplot as plt
import math
import pylab

data = np.genfromtxt("data_sort.txt", delimiter = ' ')
label=data[:,1]
t = data[:,2]
x = data[:,3]
y = data[:,4]
vect_y=[]
print(data)
data=data[np.argsort(data[:, 4])]
print(data)
#print(mean_dist)
#print(std_dist)
np.savetxt('out_sort.txt', data, fmt='%2.2f', delimiter=' ')