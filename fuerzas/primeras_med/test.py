import numpy as np
import matplotlib.pyplot as plt
import math


out=[5,6,7,8]
out = np.asarray(out)
out= out.reshape(-1,1)
a = [1,2,3,4]
a = np.asarray(a)
a= a.reshape(-1,1)
out=np.concatenate((out,a),1)	
out=np.matrix.round(out,2)
np.savetxt('out.csv',out,fmt='%2.2f',delimiter = ',')
#print(out)