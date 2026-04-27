import sys
import subprocess
import json
from pathlib import Path

try:
    from phidynamics.bio.fractal import CrecimientoFractal
except ImportError:
    print("[!] Advertencia: No se pudo importar CrecimientoFractal desde el paquete.")

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

        if suffix in [".pdb", ".ent"]:
            return ("archivo", [str(p)])

        if suffix == ".txt":
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

    else:
        print(f"[!] Comando desconocido: {comando}")
        mostrar_ayuda()