import json
import os
import statistics
from collections import Counter

def mostrar_reporte():
    ruta_db = "data/bitacora_investigacion.json"
    
    if not os.path.exists(ruta_db):
        print("[ERROR] Aún no hay bitácora. Ejecuta un análisis primero.")
        return

    with open(ruta_db, "r") as f:
        data = json.load(f)

    # --- Cálculos Estadísticos ---
    total = len(data)
    if total == 0:
        print("[INFO] La bitácora está vacía.")
        return

    frecuencias = [reg['frecuencia_hz'] for reg in data]
    promedio_f = sum(frecuencias) / total
    
    # Cálculo de desviación estándar (requiere al menos 2 datos)
    stdev_f = statistics.stdev(frecuencias) if total > 1 else 0.0
    
    bandas = Counter([reg['banda'] for reg in data])
    # -----------------------------

    print(f"\n{'='*75}")
    print(f"{'REPORTE ANALÍTICO: PHIDYNAMICS':^75}")
    print(f"{'='*75}")
    print(f"{'ID':<10} | {'Delta':<10} | {'Hz':<10} | {'Banda Espectral'}")
    print(f"{'-'*75}")

    for reg in data:
        print(f"{reg['pdb_id']:<10} | {reg['delta']:<10} | {reg['frecuencia_hz']:<10} | {reg['banda']}")
    
    print(f"{'-'*75}")
    print(f"RESUMEN ESTADÍSTICO:")
    print(f"Total estructuras analizadas: {total}")
    print(f"Frecuencia Promedio:          {promedio_f:.2f} Hz")
    print(f"Desviación Estándar (Estabilidad): {stdev_f:.4f} Hz")
    print(f"Distribución por bandas:      {dict(bandas)}")
    print(f"{'='*75}\n")

if __name__ == "__main__":
    mostrar_reporte()