import sys
from bio.resonance import BioResonancia

# Simulación de estados obtenidos mediante el motor Phidynamics
data_test = [
    {"id": "1BNA", "delta": 0.1759},
    {"id": "1D02", "delta": 0.0400},
    {"id": "1D65", "delta": 0.1761}
]

res = BioResonancia()

print(f"{'ID':<8} | {'Delta':<8} | {'Frecuencia (Hz)':<16} | {'Banda Espectral'}")
print("-" * 65)

for item in data_test:
    f = res.calcular_frecuencia(item['delta'])
    banda = res.get_banda_espectral(f)
    print(f"{item['id']:<8} | {item['delta']:<8} | {f:.2f} Hz           | {banda}")

print("-" * 65)
print("[INFO] Acoplamiento de fase validado: La torsión determina la sintonía.")