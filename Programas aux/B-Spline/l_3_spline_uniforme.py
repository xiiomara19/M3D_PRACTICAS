
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

bf = BSpline.basis_element([0, 1, 2, 3])    # función base N_0,2 definida en [0, 3)

p = np.array([ [1, 2], [2, 4], [3, 2], [4, 1], [5, 3] ]).T    # n=4 y 5 puntos
plt.plot(p[0], p[1], 'k--')
plt.plot(p[0], p[1], 'ko')

# intervalos [u_i, u_i+1) desde el nodo u_p hasta u_n, parámetro u en [u_p, u_n+1)
seg_x, seg_y = [], []
for u in np.arange(2, 3, 0.01):    # translación de la función bf según el nodo		
    pu = p[:,0] * bf(u) + p[:,1] * bf(u-1) + p[:,2] * bf(u-2)
    seg_x.append(pu[0])
    seg_y.append(pu[1])
plt.plot(seg_x[0], seg_y[0], 'bs')    # punto cuadrado inicio primer segmento  
plt.plot(seg_x, seg_y, 'b-')

seg_x, seg_y = [], []					
for u in np.arange(3, 4, 0.01): 	
    pu = p[:,1] * bf(u-1) + p[:,2] * bf(u-2) + p[:,3] * bf(u-3)
    seg_x.append(pu[0])
    seg_y.append(pu[1])
plt.plot(seg_x[0], seg_y[0], 'bo')  
plt.plot(seg_x, seg_y, 'b-')

seg_x, seg_y = [], []					
for u in np.arange(4, 5, 0.01): 		
    pu = p[:,2] * bf(u-2) + p[:,3] * bf(u-3) + p[:,4] * bf(u-4)
    seg_x.append(pu[0])
    seg_y.append(pu[1])
plt.plot(seg_x[0], seg_y[0], 'bo')  
plt.plot(seg_x, seg_y, 'b-')


plt.show()


