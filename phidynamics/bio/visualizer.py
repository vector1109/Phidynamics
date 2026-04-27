import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def graficar_estructura(puntos, titulo="Estructura Fractal Phidynamics", mostrar=True):
    """
    Renderiza el Eje de Torsión en 3D.
    Devuelve la figura para exportación externa.
    """
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    x = [float(p[0]) for p in puntos]
    y = [float(p[1]) for p in puntos]
    z = [float(p[2]) for p in puntos]

    ax.plot(x, y, z, marker='o', linestyle='-', color='gold', label='Eje de Torsión')

    ax.set_xlabel('X (Fractal)')
    ax.set_ylabel('Y (Fractal)')
    ax.set_zlabel('Z (Tiempo OAM)')
    ax.set_title(titulo)

    plt.legend()

    if mostrar:
        print("[VISUALIZADOR] Renderizando ventana 3D...")
        plt.show()

    return fig