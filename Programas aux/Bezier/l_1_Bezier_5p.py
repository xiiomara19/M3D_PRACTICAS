
import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb    # atención: exact=True

fig = plt.figure()
ax = fig.gca(projection='3d')

# ndarray de 4+1 puntos de control
kpuntuak = np.array([ [2, 1, 0], [2.5, 2.5, 0.5], [0.5, 2, 1], [0, 1, 1.5], [1, 0, 2.5] ])

ax.plot(kpuntuak[:,0], kpuntuak[:,1], kpuntuak[:,2], color='k', linestyle='dashed')

n = kpuntuak.shape[0] - 1    # índices de los puntos de control 0,1...n donde n=4

u1d = np.linspace(0, 1, 1001)    # discretizar u en el intervalo [0, 1] con escalón 0.001
pu_Bezier = np.zeros((3, len(u1d)))    # iniciar con ceros

Bu_basis = []
for i in range(n+1):
    Bu_basis.append( comb(n, i, exact=True) * u1d**i * (1-u1d)**(n-i) )
    kp, Bu = np.ix_(kpuntuak[i], Bu_basis[i])    # kp.ndim y Bu.ndim valen 2
    pu_Bezier += kp * Bu    # kp.shape (3, 1) Bu.shape (1, 1001)

ax.plot(pu_Bezier[0], pu_Bezier[1], pu_Bezier[2], color='b', linestyle='solid')

ax.set_xlim(0, 2.5)      
ax.set_ylim(0, 2.5)
ax.set_zlim(0, 2.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

for i in range(n+1):
    plt.plot(u1d, Bu_basis[i])

plt.show()

