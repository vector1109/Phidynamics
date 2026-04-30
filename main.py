import sys
import subprocess
import json
from pathlib import Path

try:
    from phidynamics.bio.fractal import CrecimientoFractal
except ImportError:
    print("[!] Advertencia: No se pudo importar CrecimientoFractal desde el paquete.")

# PASO 1 - Nuevos imports para comparación, búsqueda y análisis estructural
from phidynamics.core.similarity import similitud_firmas
from phidynamics.core.xyz_parser import cargar_xyz
from phidynamics.core.distance_matrix import matriz_distancias
from phidynamics.core.structure_signature import clasificar_estructura
from phidynamics.core.neighborhood_search import buscar_vecinos
from phidynamics.core.compare_structures import comparar_estructuras
from phidynamics.core.phase_report import imprimir_reporte_fase
from phidynamics.core.phase_sweep import barrer_fase
from phidynamics.core.diagnostics import diagnosticar

def preparar_entorno():
    """Garantiza la estructura pública de carpetas."""
    carpetas = [
        "input/pdb",
        "input/lists",
        "input/batch",
        "data",
        "data/reportes",
        "persistence",
    ]
    for folder in carpetas:
        Path(folder).mkdir(parents=True, exist_ok=True)

def resolver_entrada(valor):
    """
    Clasifica la entrada del usuario:
    - ID remoto (1BNA)
    - archivo .pdb / .ent
    - lista .txt
    - carpeta con múltiples estructuras
    """
    p = Path(valor)

    if not p.exists():
        rutas_posibles = [
            Path("input/pdb") / valor,
            Path("input/lists") / valor,
            Path("input/batch") / valor,
        ]
        for ruta in rutas_posibles:
            if ruta.exists():
                p = ruta
                break

    if p.is_file():
        suffix = p.suffix.lower()

        if suffix in [".pdb", ".ent", ".xyz"]:
            return ("archivo", [str(p)])

        elif suffix == ".txt":
            items = [x.strip() for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
            return ("lista", items)

    if p.is_dir():
        archivos = list(p.glob("*.pdb")) + list(p.glob("*.ent"))
        return ("carpeta", [str(x) for x in archivos])

    return ("id", [valor])

def run_script(cmd):
    """Ejecuta sub-scripts internos con el mismo intérprete."""
    try:
        subprocess.run([sys.executable] + cmd, check=True)
    except Exception as e:
        print(f"[!] Error ejecutando {' '.join(cmd)}: {e}")

def manejar_analisis(args):
    """Comando oficial: analizar"""
    if len(args) > 2:
        entrada = args[2]
    else:
        print("\n[?] Modo interactivo activado.")
        entrada = input("Ingrese ID, archivo, lista o carpeta: ").strip()

    tipo, items = resolver_entrada(entrada)
    print(f"[*] Modo detectado: {tipo.upper()} | Objetivos: {len(items)}")

    for item in items:
        print(f"--> Procesando: {item}")
        run_script(["analizar_pdb.py", item])

def ejecutar_simulacion_fractal():
    """Comando oficial: simular"""
    print("[*] Iniciando motor de simulación fractal...")

    num_nodos = 1000
    motor = CrecimientoFractal(
        torsion_intensity=1.618,
        harmonics=[(1.0, 0.2, 0.0), (0.5, 0.4, 1.5)],
        step_size=0.1
    )

    print(f"[*] Generando {num_nodos} nodos bio-geométricos...")
    coords = motor.generar_espiral_aurea(num_puntos=num_nodos, cuantizar=True)

    ruta_salida = Path("data/simulacion_fractal.json")
    datos_export = {
        "metadata": {
            "nodos": num_nodos,
            "phi_referencia": 1.618033988749895,
            "metodo": "torsion_wave_v6"
        },
        "geometria": coords.tolist()
    }

    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(datos_export, f, indent=4)

    print(f"✅ Datos exportados con éxito a: {ruta_salida}")

    try:
        from phidynamics.bio.visualizer import graficar_estructura
        print("[VISUALIZADOR] Renderizando simulación fractal...")
        graficar_estructura(coords, titulo="Simulación Fractal Phidynamics")
    except Exception as e:
        print(f"[!] No se pudo renderizar la simulación: {e}")

# PASO 3 - Actualizar mostrar_ayuda
def mostrar_ayuda():
    print("""
Phidynamics — Consola de Usuario

Comandos oficiales:
  python main.py analizar <OBJ>
      Ejemplos:
      python main.py analizar 1BNA
      python main.py analizar proteina.pdb
      python main.py analizar lista.txt
      python main.py analizar input/pdb/

  python main.py simular
      Ejecuta simulación fractal + JSON + visualización

  python main.py validar
      Ejecuta suite de validación científica

  python main.py reporte
      Muestra bitácora analítica acumulada

  python main.py comparar A.xyz B.xyz   (Compara similitud estructural)

  python main.py buscar objetivo.xyz carpeta/ (Busca vecinos estructurales)

  python main.py fase   (Ejecuta simulación de evolución de fase B60)

  python main.py fase-stats   (Muestra estadísticas de barrido de fase)

  python main.py fase-report   (Genera reporte formateado del análisis de fase)

  python main.py fase-sweep   (Ejecuta barrido de fase con múltiples perturbaciones)

  python main.py diagnosticar archivo.xyz   (Diagnóstico integrado de estructura)
""")

if __name__ == "__main__":
    preparar_entorno()

    if len(sys.argv) < 2:
        mostrar_ayuda()
        sys.exit(0)

    comando = sys.argv[1].lower()

    if comando == "analizar":
        manejar_analisis(sys.argv)

    elif comando == "simular":
        ejecutar_simulacion_fractal()

    elif comando == "validar":
        print("[*] Lanzando suite de validación científica...")
        run_script(["validate_with_pdb.py"])

    elif comando == "reporte":
        run_script(["reporte.py"])

    elif comando == "comparar":
        if len(sys.argv) < 4:
            print("[!] Uso: python main.py comparar A.xyz B.xyz")
            sys.exit(1)

        comparar_estructuras(sys.argv[2], sys.argv[3])

    elif comando == "buscar":
        if len(sys.argv) < 4:
            print("[!] Uso: python main.py buscar objetivo.xyz carpeta/")
            sys.exit(1)

        objetivo = sys.argv[2]
        carpeta = sys.argv[3]
        buscar_vecinos(objetivo, carpeta)

    # NUEVO COMANDO: fase
    elif comando == "fase":
        from phidynamics.core.phase_runner import correr_experimento

        phi = [45, 12, 33, 7, 51, 28]
        delta = [10, 5, 0, -5, 20, 15]

        correr_experimento(phi, delta, ciclos=8)

    # NUEVO COMANDO: fase-stats
    elif comando == "fase-stats":
        from phidynamics.core.phase_stats import analizar_sweep
        print(analizar_sweep())

    # NUEVO COMANDO: fase-report
    elif comando == "fase-report":
        imprimir_reporte_fase()

    # NUEVO COMANDO: fase-sweep
    elif comando == "fase-sweep":
        phi = [45, 12, 33, 7, 51, 28]
        deltas = [
            [10, 5, 0, -5, 20, 15],
            [5, 2, 0, -2, 10, 8],
            [20, 10, 5, -10, 25, 18],
        ]
        barrer_fase(phi, deltas, ciclos=8)

    elif comando == "diagnosticar":
        if len(sys.argv) < 3:
            print("[!] Uso: python main.py diagnosticar archivo.xyz")
            sys.exit(1)

        resultado = diagnosticar(sys.argv[2], ciclos=8, plot=False)

        print("\n" + "=" * 60)
        print("DIAGNÓSTICO INTEGRADO")
        print("=" * 60)
        print(f"Archivo:         {resultado['archivo']}")
        print(f"Firma:           {resultado['firma']}")
        print(f"Dimensionalidad: {resultado['dimensionalidad']}")
        print(f"Absorción:       {resultado['absorcion_final']}")
        print(f"Régimen:         {resultado['regimen']}")
        print(f"Memoria:         {resultado['memoria']}")
        print(f"Conclusión:      {resultado['conclusion']}")
        print("=" * 60)

    else:
        print(f"[!] Comando desconocido: {comando}")
        mostrar_ayuda()