import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

""""PRÁCTICA 3.2. Curva B-Spline y Funciones Base."""
"""XIOMARA GERALDINE CÁCERES CHANCAHUANA"""
"""MIÉRCOLES 30/04/2025"""

def curva_bspline(u_vec, opt):
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

    ## B-SPLINE ORIGINAL
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

    ## B-SPLINE MODIFICADA
    if opt == 1:
        q = np.array([ 
            [-5, -5], 
            [0, 0], 
            [0, 8], 
            [5, 5], 
            [5, -2], 
            [0, -3] 
        ]).T

    else:
        q = np.array([ 
            [-5, -5], 
            [-5, 4], 
            [2, -1], 
            [5, 5], 
            [5, -2], 
            [0, -3] 
        ]).T

    step = 0.001
    bs_x, bs_y = [], []					
    for u in np.arange(0, 0.33, step):
        qu = N0(u) * q[:,0] + N1(u) * q[:,1] + N2(u) * q[:,2] + N3(u) * q[:,3]
        bs_x.append(qu[0])
        bs_y.append(qu[1])
    plt.plot(bs_x, bs_y, 'b-')
    bs_x, bs_y = [], []					
    for u in np.arange(0.33, 0.67, step):
        qu = N1(u) * q[:,1] + N2(u) * q[:,2] + N3(u) * q[:,3] + N4(u) * q[:,4]
        bs_x.append(qu[0])
        bs_y.append(qu[1])
    plt.plot(bs_x, bs_y, 'r-')
    bs_x, bs_y = [], []					
    for u in np.arange(0.67, 1, step):
        qu = N2(u) * q[:,2] + N3(u) * q[:,3] + N4(u) * q[:,4] + N5(u) * q[:,5]
        bs_x.append(qu[0])
        bs_y.append(qu[1])
    plt.plot(bs_x, bs_y, 'y-')

    plt.plot(q[0], q[1], 'ko')
    plt.plot(q[0], q[1], 'k--')

    # Mostrar la gráfica
    plt.show()


if __name__ == '__main__':

    while True:
        print("¿Qué punto de control quieres mover de posicion?")
        opt = int(input("1. P1 de (-5,4) a (0,0)\n"
                    "2. P2 de (0,8) a (2,-1)\n"))
        if opt in (1,2):
            #Vector de nodos
            u_vec = [0, 0, 0, 0, 0.33, 0.67, 1, 1, 1, 1]

            curva_bspline(u_vec, opt)
            break
        else:
            print('Opción invalida')
