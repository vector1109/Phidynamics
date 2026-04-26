import sys
from bio.resonance import BioResonancia

def ejecutar_analisis(ruta_archivo):
    """Calcula accesibilidad y retorna los datos para persistencia."""
    # --- AQUÍ VA TU LÓGICA DE CÁLCULO ---
    # He dejado un valor hardcoded para pruebas, reemplázalo con tu fórmula
    delta_calculado = 0.1759 
    # ------------------------------------

    res = BioResonancia()
    frecuencia = res.calcular_frecuencia(delta_calculado)
    banda = res.get_banda_espectral(frecuencia)

    print(f"\n[INFO] Procesado: {ruta_archivo}")
    print(f"Resultados -> Delta: {delta_calculado}, Frecuencia: {frecuencia:.2f} Hz")
    
    return {
        "delta": delta_calculado,
        "frecuencia": frecuencia,
        "banda": banda
    }

if __name__ == "__main__":
    ruta = sys.argv[1] if len(sys.argv) > 1 else input("Ruta PDB: ")
    ejecutar_analisis(ruta)