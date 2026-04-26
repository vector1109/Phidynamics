import numpy as np
import matplotlib.pyplot as plt
from phidynamics.bio.fractal import CrecimientoFractal

# Usamos los parámetros que acabamos de optimizar (aproximación visual de tu resultado)
# Ajusta estos valores según lo que te dio el optimizador en tu terminal
amp, freq, phase, offset = [0.5, 0.1, 0.0, 0.5] 
num_nodos = 153
n = np.arange(num_nodos)

# Generar la onda encontrada
k_variable = amp * np.sin(freq * n + phase) + offset

plt.figure(figsize=(12, 5))
plt.plot(n, k_variable, label='Intensidad de Torsión (K)', color='red', linewidth=2)
plt.title("Firma de Torsión Optimizada para 1MBN")
plt.xlabel("Nodo (Residuo de Proteína)")
plt.ylabel("Factor de Torsión")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()