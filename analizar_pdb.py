import sys
import os

# Intentamos importar torch para la generación de tensores
try:
    import torch
except ImportError:
    print("[ERROR] PyTorch no detectado. Instálalo con: pip install torch")
    sys.exit(1)

# Importaciones de los módulos en la raíz
from descargador_pdb import descargar_pdb
from calculadora_accesibilidad import ejecutar_analisis
from persistence.logger import guardar_resultado

# Importación corregida para tu estructura de carpetas
try:
    from phidynamics.bio.visualizer import graficar_estructura
except ImportError as e:
    print(f"[ERROR] No se pudo encontrar el visualizador: {e}")
    print("Asegúrate de que la carpeta 'phidynamics' tenga un archivo __init__.py")
    sys.exit(1)

# PASO 1 - Nuevos imports
from pathlib import Path
from phidynamics.core.xyz_parser import cargar_xyz
from phidynamics.core.distance_matrix import matriz_distancias
from phidynamics.core.bond_detector import detectar_enlaces
from phidynamics.core.structure_signature import clasificar_estructura
from phidynamics.core.analyze_xyz import analizar_material

def generar_puntos_fractales(delta, pasos=60):
    """
    Genera la estructura de puntos basada en la torsión Delta.
    Representa la expansión en el eje Z (Tiempo OAM).
    """
    puntos = []
    # Usamos base-60 implícita en la resolución de pasos para consistencia
    for i in range(pasos):
        t = i / 10.0
        # La torsión modula el radio del fractal en X e Y
        angulo = t * 2.0
        radio = t * delta * 15.0 # Factor de escala para visibilidad
        
        x = radio * torch.cos(torch.tensor(angulo))
        y = radio * torch.sin(torch.tensor(angulo))
        z = torch.tensor(t) # Eje de Tiempo OAM
        
        puntos.append([x, y, z])
    return puntos

def orquestar(pdb_id, mostrar=True):
    # Interceptar .xyz
    ruta = Path(pdb_id)
    
    if ruta.exists() and ruta.suffix.lower() == ".xyz":
        print(f"\n{'='*60}")
        print(f"CICLO DE ANÁLISIS MATERIAL: {ruta.name}")
        print(f"{'='*60}")
        
        analizar_material(str(ruta))
        print(f"\n--- Ciclo finalizado para {ruta.name} ---\n")
        return None, None
    
    print(f"\n{'='*60}")
    print(f"CICLO DE ANÁLISIS SOBERANO: {pdb_id}")
    print(f"{'='*60}")
    
    # 1. Resolver entrada (archivo local o descarga)
    if os.path.isfile(pdb_id):
        ruta_archivo = pdb_id
        print(f"[INFO] Usando archivo local: {ruta_archivo}")
    else:
        ruta_archivo = descargar_pdb(pdb_id)
    
    if ruta_archivo:
        # 2. Motor de cálculo (Resonancia y Accesibilidad)
        resultados = ejecutar_analisis(ruta_archivo)
        
        if resultados:
            # 3. Persistencia en bitácora local
            guardar_resultado(
                pdb_id, 
                resultados['delta'], 
                resultados['frecuencia'], 
                resultados['banda']
            )
            
            # 4. Generación y Visualización de la Estructura Fractal
            print(f"\n[SISTEMA] Generando Eje de Torsión (Delta: {resultados['delta']:.4f})...")
            puntos = generar_puntos_fractales(resultados['delta'])
            
            titulo_grafico = f"Phidynamics: {pdb_id} | Banda: {resultados['banda']}"
            
            # Llamada a tu visualizador nativo
            fig = graficar_estructura(puntos, titulo=titulo_grafico, mostrar=mostrar)
            return resultados, fig
            
        print(f"\n--- Ciclo finalizado para {pdb_id} ---\n")
    else:
        print(f"[FALLO] No se pudo obtener la estructura {pdb_id}")
    
    return None, None

if __name__ == "__main__":
    # Soporte para argumento de consola o input manual
    id_input = sys.argv[1] if len(sys.argv) > 1 else input("Introduce ID PDB para análisis: ")
    orquestar(id_input.upper(), mostrar=True)