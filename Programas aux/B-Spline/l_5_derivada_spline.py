import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

u_vec = [0, 0, 0, 0, 0.5, 1, 1, 1, 1]        # clamped B-spline, p=3
N0 = BSpline.basis_element(u_vec[0:3+1+1])	
N1 = BSpline.basis_element(u_vec[1:4+1+1])
N2 = BSpline.basis_element(u_vec[2:5+1+1])
N3 = BSpline.basis_element(u_vec[3:6+1+1])
N4 = BSpline.basis_element(u_vec[4:7+1+1])
p = np.array([ [-70, -76], [-70, 75], [74, 75], [74, -77], [-40, -76] ]).T 

step = 0.001
bs_x, bs_y = [], []					
for u in np.arange(0, 0.5, step):
    pu = N0(u) * p[:,0] + N1(u) * p[:,1] + N2(u) * p[:,2] + N3(u) * p[:,3]
    bs_x.append(pu[0])
    bs_y.append(pu[1])
plt.plot(bs_x, bs_y, 'b-')
bs_x, bs_y = [], []					
for u in np.arange(0.5, 1, step):
    pu = N1(u) * p[:,1] + N2(u) * p[:,2] + N3(u) * p[:,3] + N4(u) * p[:,4]
    bs_x.append(pu[0])
    bs_y.append(pu[1])
plt.plot(bs_x, bs_y, 'r-')
plt.plot(p[0], p[1], 'ko')
plt.plot(p[0], p[1], 'k--')

q = np.column_stack(( \
(p[:,1] - p[:,0]) * 3 / (u_vec[4] - u_vec[1]), \
(p[:,2] - p[:,1]) * 3 / (u_vec[5] - u_vec[2]), \
(p[:,3] - p[:,2]) * 3 / (u_vec[6] - u_vec[3]), \
(p[:,4] - p[:,3]) * 3 / (u_vec[7] - u_vec[4]) ))
u_vec_drv = [0, 0, 0, 0.5, 1, 1, 1]
Nd0 = BSpline.basis_element(u_vec_drv[0:2+1+1])	
Nd1 = BSpline.basis_element(u_vec_drv[1:3+1+1])
Nd2 = BSpline.basis_element(u_vec_drv[2:4+1+1])
Nd3 = BSpline.basis_element(u_vec_drv[3:5+1+1])
u = 0.1        # punto sobre el primer segmento 
pu = N0(u) * p[:,0] + N1(u) * p[:,1] + N2(u) * p[:,2] + N3(u) * p[:,3]
p_x, p_y = pu[0], pu[1]
d = Nd0(u) * q[:,0] + Nd1(u) * q[:,1] + Nd2(u) * q[:,2]
d_x, d_y = d[0]/5, d[1]/5    # escalar para el gráfico
plt.plot(p_x, p_y, 'bo')
plt.plot([p_x - d_x, p_x + d_x], [p_y - d_y, p_y + d_y], 'b-')
u = 0.7        # punto sobre el segundo segmento 
pu = N1(u) * p[:,1] + N2(u) * p[:,2] + N3(u) * p[:,3] + N4(u) * p[:,4]
p_x, p_y = pu[0], pu[1]
d = Nd1(u) * q[:,1] + Nd2(u) * q[:,2] + Nd3(u) * q[:,3]
d_x, d_y = d[0]/5, d[1]/5     # escalar
plt.plot(p_x, p_y, 'ro')
plt.plot([p_x - d_x, p_x + d_x], [p_y - d_y, p_y + d_y], 'r-')

plt.show()






