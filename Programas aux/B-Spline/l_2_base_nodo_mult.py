
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

# nodos 0, 0.2, 0.4, 0.4, 0.6, 0.8, 1
step = 0.002

# grado 1
N_0 = BSpline.basis_element([0, 0.2, 0.4])
u = np.arange(0, 0.4, step)
plt.plot(u, N_0(u), 'm')
N_1 = BSpline.basis_element([0.2, 0.4, 0.4])
u = np.arange(0.2, 0.4, step)
plt.plot(u, N_1(u), 'y')
N_2 = BSpline.basis_element([0.4, 0.4, 0.6])
u = np.arange(0.4, 0.6, step)
plt.plot(u, N_2(u), 'r')
N_3 = BSpline.basis_element([0.4, 0.6, 0.8])
u = np.arange(0.4, 0.8, step)
plt.plot(u, N_3(u), 'g')
N_4 = BSpline.basis_element([0.6, 0.8, 1])
u = np.arange(0.6, 1, step)
plt.plot(u, N_4(u), 'c')

plt.show()

# grado 2
N_0 = BSpline.basis_element([0, 0.2, 0.4, 0.4])
u = np.arange(0, 0.4, step)
plt.plot(u, N_0(u), 'm')
N_1 = BSpline.basis_element([0.2, 0.4, 0.4, 0.6])
u = np.arange(0.2, 0.6, step)
plt.plot(u, N_1(u), 'r')
N_2 = BSpline.basis_element([0.4, 0.4, 0.6, 0.8])
u = np.arange(0.4, 0.8, step)
plt.plot(u, N_2(u), 'g')
N_3 = BSpline.basis_element([0.4, 0.6, 0.8, 1])
u = np.arange(0.4, 1, step)
plt.plot(u, N_3(u), 'y')

plt.show()

