
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

# grado de las funciones base p = 4
bf = BSpline.basis_element([0, 1, 2, 3, 4, 5])    # función base N_0,4 definida en [0, 5)

# n = 7 y 8 puntos de control 
p = np.array([ [1, 0], [3, 0], [4, 1], [4, 3], [3, 4], [1, 4], [0, 3], [0, 1] ]).T
plt.plot(p[0], p[1], 'k--')
plt.plot([p[0,7], p[0,0]], [p[1,7], p[1,0]], 'y--')
plt.plot(p[0], p[1], 'ko')

# n+1 intervalos [u_i, u_i+1) desde el nodo u_0 hasta u_n, parámetro u en [u_0, u_n+1)

seg_x, seg_y = [], []
for u in np.arange(0, 1, 0.01):   	
    pu = p[:,4]*bf(u+4) + p[:,5]*bf(u+3) + p[:,6]*bf(u+2) + p[:,7]*bf(u+1) + p[:,0]*bf(u)
    seg_x.append(pu[0])
    seg_y.append(pu[1])
plt.plot(seg_x[0], seg_y[0], 'bs')   
plt.plot(seg_x, seg_y, 'b-')

seg_x, seg_y = [], []
for u in np.arange(1, 2, 0.01):   	
    pu = p[:,5]*bf(u+3) + p[:,6]*bf(u+2) + p[:,7]*bf(u+1) + p[:,0]*bf(u) + p[:,1]*bf(u-1)
    seg_x.append(pu[0])
    seg_y.append(pu[1])
plt.plot(seg_x[0], seg_y[0], 'bo')
plt.plot(seg_x, seg_y, 'b-')

seg_x, seg_y = [], []
for u in np.arange(2, 3, 0.01):   	
    pu = p[:,6]*bf(u+2) + p[:,7]*bf(u+1) + p[:,0]*bf(u) + p[:,1]*bf(u-1) + p[:,2]*bf(u-2)
    seg_x.append(pu[0])
    seg_y.append(pu[1])
plt.plot(seg_x[0], seg_y[0], 'bo')
plt.plot(seg_x, seg_y, 'b-')

seg_x, seg_y = [], []
for u in np.arange(3, 4, 0.01):   	
    pu = p[:,7]*bf(u+1) + p[:,0]*bf(u) + p[:,1]*bf(u-1) + p[:,2]*bf(u-2) + p[:,3]*bf(u-3)
    seg_x.append(pu[0])
    seg_y.append(pu[1])
plt.plot(seg_x[0], seg_y[0], 'bo')
plt.plot(seg_x, seg_y, 'b-')

seg_x, seg_y = [], []
for u in np.arange(4, 5, 0.01):   	
    pu = p[:,0]*bf(u) + p[:,1]*bf(u-1) + p[:,2]*bf(u-2) + p[:,3]*bf(u-3) + p[:,4]*bf(u-4)
    seg_x.append(pu[0])
    seg_y.append(pu[1])
plt.plot(seg_x[0], seg_y[0], 'bo')
plt.plot(seg_x, seg_y, 'b-')

seg_x, seg_y = [], []
for u in np.arange(5, 6, 0.01):   	
    pu = p[:,1]*bf(u-1) + p[:,2]*bf(u-2) + p[:,3]*bf(u-3) + p[:,4]*bf(u-4) + p[:,5]*bf(u-5)
    seg_x.append(pu[0])
    seg_y.append(pu[1])
plt.plot(seg_x[0], seg_y[0], 'bo')
plt.plot(seg_x, seg_y, 'b-')

seg_x, seg_y = [], []
for u in np.arange(6, 7, 0.01):   	
    pu = p[:,2]*bf(u-2) + p[:,3]*bf(u-3) + p[:,4]*bf(u-4) + p[:,5]*bf(u-5) + p[:,6]*bf(u-6)
    seg_x.append(pu[0])
    seg_y.append(pu[1])
plt.plot(seg_x[0], seg_y[0], 'bo')
plt.plot(seg_x, seg_y, 'b-')

seg_x, seg_y = [], []
for u in np.arange(7, 8, 0.01):   	
    pu = p[:,3]*bf(u-3) + p[:,4]*bf(u-4) + p[:,5]*bf(u-5) + p[:,6]*bf(u-6) + p[:,7]*bf(u-7)
    seg_x.append(pu[0])
    seg_y.append(pu[1])
plt.plot(seg_x[0], seg_y[0], 'bo')
plt.plot(seg_x, seg_y, 'b-')

plt.show()


