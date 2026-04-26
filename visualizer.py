import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def graficar_estructura(puntos, titulo="Estructura Fractal Phidynamics"):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    # Extraer coordenadas
    x = [p[0].item() for p in puntos]
    y = [p[1].item() for p in puntos]
    z = [p[2].item() for p in puntos]
    
    # Graficar la línea y los puntos
    ax.plot(x, y, z, marker='o', linestyle='-', color='gold', label='Eje de Torsión')
    ax.set_xlabel('X (Fractal)')
    ax.set_ylabel('Y (Fractal)')
    ax.set_zlabel('Z (Tiempo OAM)')
    ax.set_title(titulo)
    plt.legend()
    plt.show()