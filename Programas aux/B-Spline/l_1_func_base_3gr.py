
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

# Funciones base de grado p=3 y n=4 luego 5 funciones base 
# m = n+p+1 luego 9 nodos, parámetro u en [0, 8)

step = 0.01    # el parámetro u se discretiza 
sum_N = np.zeros(int(8 / step))   # suma para u discreto desde 0 hasta 8/step - 1

N_0 = BSpline.basis_element(np.arange(0, 4+1, 1))    # nodos array([0, 1, 2, 3, 4])
u = np.arange(0, 4, step)
sum_N[0:int(4 / step)] += N_0(u)
plt.plot(u, N_0(u), 'm-')

N_1 = BSpline.basis_element(np.arange(1, 5+1, 1))
u = np.arange(1, 5, step)
sum_N[int(1 / step):int(5 / step)] += N_1(u)
plt.plot(u, N_1(u), 'r-')

N_2 = BSpline.basis_element(np.arange(2, 6+1, 1))
u = np.arange(2, 6, step)
sum_N[int(2 / step):int(6 / step)] += N_2(u)
plt.plot(u, N_2(u), 'g-')

N_3 = BSpline.basis_element(np.arange(3, 7+1, 1))
u = np.arange(3, 7, step)
sum_N[int(3 / step):int(7 / step)] += N_3(u)
plt.plot(u, N_3(u), 'y-')

N_4 = BSpline.basis_element(np.arange(4, 8+1, 1))
u = np.arange(4, 8, step)
sum_N[int(4 / step):int(8 / step)] += N_4(u)
plt.plot(u, N_4(u), 'c-')

u = np.arange(0, 8, step)
plt.plot(u, sum_N, 'k--')

plt.show()

