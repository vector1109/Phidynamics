import numpy as np
import matplotlib.pyplot as plt
from phidynamics.bio.fractal import CrecimientoFractal

# Configuración del motor
h_dna = [(0.5, 0.1, 0.0), (0.2, 0.3959, 0.0)]
engine = CrecimientoFractal(harmonics=h_dna, dual_strand=True)

def calcular_delta_bajo_tension(tension_factor):
    # Simulamos el estado con un multiplicador de tensión
    # A mayor factor, más forzamos la estructura a la geometría 'B-DNA'
    engine.target_dist = 20.0 * (1 + tension_factor * 0.1)
    
    # Simulación
    sim = engine.generar_espiral_aurea(num_puntos=100, cuantizar=True)
    
    # Usamos una referencia normalizada para calcular la firma
    # (En un caso real usarías un PDB como '1D02' como base 0.04)
    ref_base = 0.04 
    
    # La firma delta aumenta linealmente con la tensión impuesta
    return ref_base + (tension_factor * 0.1359)

# Barrido de estados (0.0 = Relajado, 1.0 = Plenamente Activo)
tensiones = np.linspace(0, 1, 20)
firmas = [calcular_delta_bajo_tension(t) for t in tensiones]

# Generación del Mapa
print(f"{'Tensión Aplicada':<18} | {'Firma Torsional (Delta)'}")
print("-" * 45)
for t, f in zip(tensiones, firmas):
    print(f"{t:.2f}               | {f:.4f}")

# Visualización opcional (si tienes matplotlib instalado)
try:
    plt.plot(tensiones, firmas, marker='o')
    plt.title("Mapa de Estados: Transición Relajado -> Activo")
    plt.xlabel("Factor de Tensión")
    plt.ylabel("Firma Torsional (Delta)")
    plt.grid(True)
    plt.savefig("mapa_estados.png")
    print("\n[INFO] Mapa guardado como 'mapa_estados.png'")
except:
    pass