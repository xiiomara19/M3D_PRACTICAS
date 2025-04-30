import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

""""PRÁCTICA 3.1. Curva B-Spline y Funciones Base."""
"""XIOMARA GERALDINE CÁCERES CHANCAHUANA"""
"""MIÉRCOLES 30/04/2025"""

def curva_bspline(u_vec):

    #Puntos de control
    p = np.array([ 
        [-5, -5], 
        [-5, 4], 
        [0, 8], 
        [5, 5], 
        [5, -2], 
        [0, -3] 
    ]).T

    N0 = BSpline.basis_element(u_vec[0:3+1+1])	
    N1 = BSpline.basis_element(u_vec[1:4+1+1])
    N2 = BSpline.basis_element(u_vec[2:5+1+1])
    N3 = BSpline.basis_element(u_vec[3:6+1+1])
    N4 = BSpline.basis_element(u_vec[4:7+1+1])
    N5 = BSpline.basis_element(u_vec[5:8+1+1])

    step = 0.001
    bs_x, bs_y = [], []					
    for u in np.arange(0, 0.33, step):
        pu = N0(u) * p[:,0] + N1(u) * p[:,1] + N2(u) * p[:,2] + N3(u) * p[:,3]
        bs_x.append(pu[0])
        bs_y.append(pu[1])
    plt.plot(bs_x, bs_y, 'b-')
    bs_x, bs_y = [], []					
    for u in np.arange(0.33, 0.67, step):
        pu = N1(u) * p[:,1] + N2(u) * p[:,2] + N3(u) * p[:,3] + N4(u) * p[:,4]
        bs_x.append(pu[0])
        bs_y.append(pu[1])
    plt.plot(bs_x, bs_y, 'r-')
    bs_x, bs_y = [], []					
    for u in np.arange(0.67, 1, step):
        pu = N2(u) * p[:,2] + N3(u) * p[:,3] + N4(u) * p[:,4] + N5(u) * p[:,5]
        bs_x.append(pu[0])
        bs_y.append(pu[1])
    plt.plot(bs_x, bs_y, 'y-')

    plt.plot(p[0], p[1], 'ko')
    plt.plot(p[0], p[1], 'k--')

    plt.title("Curva B-spline cúbica")

    # Mostrar la gráfica
    plt.show()


def funciones_base(u):

    #vector de nodos: [0, 0, 0, 0, 0.33, 0.67, 1, 1, 1, 1]
    #print('u', u)
    colors = ['m', 'y', 'r', 'g', 'c', 'b']

    step = 0.002

    for i in range(6):
        #print('i', i)
        vector = u[i:i+5]
        #print('vector', vector)
        N = BSpline.basis_element(vector)
        v = np.arange(vector[0], vector[-1], step)
        plt.plot(v, N(v), colors[i % len(colors)])

    plt.show()



if __name__ == '__main__':

    #Vector de nodos
    u_vec = [0, 0, 0, 0, 0.33, 0.67, 1, 1, 1, 1]

    curva_bspline(u_vec)

    funciones_base(u_vec)