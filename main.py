import torch
import math
from phidynamics.core.constants import PHI, KS_BIOLOGICAL
from phidynamics.core.geometry import RiemannCartanEngine
from phidynamics.bio.fractal import CrecimientoFractal
from phidynamics.bio.visualizer import graficar_estructura

def imprimir_encabezado():
    print("=" * 60)
    print("🧬 PHIDYNAMICS v1.1 - Motor de Bio-Geometría Fractal")
    print("=" * 60)
    print(f"[*] Proporción Áurea (Phi): {PHI:.4f}")
    print(f"[*] Rigidez Torsional (k_S): {KS_BIOLOGICAL:.1e}")
    print("-" * 60)

def ejecutar_simulacion():
    # 1. Configuración del Tiempo OAM (Momento Angular Orbital del Tiempo)
    # Evaluamos en t = 1.0 para ver la rotación inicial
    tiempo_evaluacion = 1.0
    engine = RiemannCartanEngine(time_t=tiempo_evaluacion)
    
    # 2. Generación de la Métrica Helicoidal
    # 'scale_a' representa la expansión local (en biología, densidad de empaquetamiento)
    scale_a = 1.0
    g = engine.get_helical_metric(scale_a=scale_a)
    
    # 3. Simulación de Torsión Quiral
    # Creamos un tensor de torsión asimétrico inspirado en el spin coherente
    torsion_demo = torch.zeros((4, 4, 4), dtype=torch.double)
    torsion_demo[1, 2, 3] = 0.7 * PHI  # Componente quiral amplificada por Phi
    torsion_demo[1, 3, 2] = -0.7 * PHI
    
    # Calculamos la Contorsión K (la huella geométrica de la torsión)
    K_tensor = engine.calculate_contorsion(torsion_demo, g)
    intensidad_k = torch.norm(K_tensor).item()

    # 4. Resultados Numéricos en Consola
    print(f"[+] Tiempo OAM: {tiempo_evaluacion}s")
    print(f"[+] Métrica g00 (Elasticidad Temporal): {g[0,0].item():.4e}")
    print(f"[+] Intensidad Torsional K: {intensidad_k:.4f}")
    print("\n[!] El espacio-tiempo se ha 'retorcido' siguiendo a Phi.")
    print("-" * 60)

    # 5. Generación de Estructura Biológica Fractal
    # Usamos 100 puntos para una espiral definida (ADN/Proteína)
    print("🌱 Generando arquitectura fractal basada en la torsión...")
    generador = CrecimientoFractal(torsion_intensity=intensidad_k)
    puntos_bio = generador.generar_espiral_aurea(num_puntos=100)
    
    # 6. Visualización 3D
    print("🎨 Abriendo visualizador 3D...")
    graficar_estructura(
        puntos_bio, 
        titulo=f"Estructura Phidynamics (K={intensidad_k:.2f}, t={tiempo_evaluacion})"
    )

if __name__ == "__main__":
    try:
        imprimir_encabezado()
        ejecutar_simulacion()
        print("\n✅ Simulación finalizada con éxito.")
    except Exception as e:
        print(f"\n❌ Error durante la ejecución: {e}")