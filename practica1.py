import numpy as np
import matplotlib.pyplot as plt

""""PRÁCTICA 1.1. Computa el gráfico de una hélice con la recta tangente en un punto de la curva."""
"""XIOMARA GERALDINE CÁCERES CHANCAHUANA"""
"""JUEVES 24/01/2025"""


def main_program(a, b, c):

    #HELICE CIRCULAR
    u_values = np.linspace(0, 50, 1000)
    x = a *  np.cos(u_values)
    y = b * np.sin(u_values)
    z = b * u_values
    #print("Punto en el espacio en el momento ", u,": ", x, y, z)

    #PUNTO MÁS CERCANO A LA HELICE
    # Encontrar el índice del punto más cercano en la hélice
    distances = np.sqrt((x - a)**2 + (y - b)**2 + (z - c)**2)
    closest_index = np.argmin(distances)

    # Coordenadas del punto más cercano
    x_closest = x[closest_index]
    y_closest = y[closest_index]
    z_closest = z[closest_index]

    #VECTOR TANGENTE EN EL PUNTO A,B CON LA HELICE CIRCULAR
    #Derivadas de x, y, z
    dx = -a * np.sin(u_values[closest_index])
    dy = b * np.cos(u_values[closest_index])
    dz = b

    #Punto final del vector tangente
    tangent_end_x = x_closest + dx
    tangent_end_y = y_closest + dy
    tangent_end_z = z_closest + dz

    #Creación de la figura y los ejes 3D
    flg = plt.figure()
    ax = flg.add_subplot(111, projection='3d')

    # Graficar la hélice
    ax.plot(x, y, z, label='Hélice circular', color='blue')
    ax.scatter(x_closest, y_closest, z_closest, color='red', label='Punto más cercano')
    ax.plot([x_closest, tangent_end_x], [y_closest, tangent_end_y], [z_closest, tangent_end_z], color='green', label='Vector tangente')

    # Información ejes + titulo de la gráfica
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title('Hélice circular con vector tangente en el punto ('+str(a)+','+str(b)+','+str(c)+')')
    ax.legend()

    # Mostrar la gráfica
    plt.show()
    

if __name__ == '__main__':
    while True:
        a = input("Introduce la coordenada en el eje x de tu punto:")
        b = input("Introduce la coordenada en el eje y de tu punto:")
        c = input("Introduce la coordenada en el eje z de tu punto:")

        if not a.isdigit() or not b.isdigit() or not c.isdigit():
            print("Los puntos deben ser enteros")
        else:
            a = int(a)
            b = int(b)
            c = int(c)
            if a not in range(0, 26) or b not in range(0, 26) or c not in range(0, 25):
                print("Los puntos deben estar entre 1 y 50")
            else:
                print("Creando la gráfica...")
                main_program(a, b, c)
                print("Programa finalizado")
                break