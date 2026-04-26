import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def graficar_estructura(puntos, titulo="Estructura Fractal Phidynamics"):
    """
    Renderiza el Eje de Torsión en 3D.
    """
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    # Extraer coordenadas de los tensores/listas
    # Usamos float(p[i]) para ser compatibles con tensores y números simples
    x = [float(p[0]) for p in puntos]
    y = [float(p[1]) for p in puntos]
    z = [float(p[2]) for p in puntos]
    
    # Graficar la línea y los puntos
    ax.plot(x, y, z, marker='o', linestyle='-', color='gold', label='Eje de Torsión')
    
    # Configuración de etiquetas
    ax.set_xlabel('X (Fractal)')
    ax.set_ylabel('Y (Fractal)')
    ax.set_zlabel('Z (Tiempo OAM)')
    ax.set_title(titulo)
    
    plt.legend()
    print("[VISUALIZADOR] Renderizando ventana 3D...")
    plt.show()