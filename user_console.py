import sys
import shutil
import subprocess
from pathlib import Path

BASE = Path(__file__).parent
INPUT_PDB = BASE / "input" / "pdb"
INPUT_LISTS = BASE / "input" / "lists"
INPUT_BATCH = BASE / "input" / "batch"


def run(cmd):
    subprocess.run([sys.executable] + cmd)


def preparar():
    INPUT_PDB.mkdir(parents=True, exist_ok=True)
    INPUT_LISTS.mkdir(parents=True, exist_ok=True)
    INPUT_BATCH.mkdir(parents=True, exist_ok=True)


def copiar_archivo(origen, destino_dir):
    origen = Path(origen)
    if not origen.exists():
        print(f"[ERROR] No existe: {origen}")
        return None

    destino = destino_dir / origen.name
    shutil.copy2(origen, destino)
    return destino


def menu():
    print("\n" + "=" * 60)
    print("PHIDYNAMICS — CONSOLA DE USUARIO".center(60))
    print("=" * 60)
    print("1. Analizar ID PDB")
    print("2. Analizar archivo PDB")
    print("3. Analizar lista de IDs")
    print("4. Analizar carpeta de estructuras")
    print("5. Ejecutar simulación fractal")
    print("6. Ejecutar validación")
    print("7. Ver reporte")
    print("0. Salir")
    print("=" * 60)


def analizar_id():
    valor = input("Ingrese ID PDB: ").strip()
    run(["main.py", "analizar", valor])


def analizar_archivo():
    ruta = input("Ruta del archivo (.pdb / .ent): ").strip()
    destino = copiar_archivo(ruta, INPUT_PDB)
    if destino:
        run(["main.py", "analizar", str(destino)])


def analizar_lista():
    ruta = input("Ruta del archivo lista (.txt): ").strip()
    destino = copiar_archivo(ruta, INPUT_LISTS)
    if destino:
        run(["main.py", "analizar", str(destino)])


def analizar_carpeta():
    ruta = input("Ruta de carpeta con estructuras: ").strip()
    carpeta = Path(ruta)

    if not carpeta.exists() or not carpeta.is_dir():
        print("[ERROR] Carpeta inválida.")
        return

    destino = INPUT_BATCH / carpeta.name
    destino.mkdir(parents=True, exist_ok=True)

    for archivo in carpeta.glob("*"):
        if archivo.suffix.lower() in [".pdb", ".ent"]:
            shutil.copy2(archivo, destino / archivo.name)

    run(["main.py", "analizar", str(destino)])


def loop():
    preparar()

    while True:
        menu()
        op = input("Seleccione opción: ").strip()

        if op == "1":
            analizar_id()
        elif op == "2":
            analizar_archivo()
        elif op == "3":
            analizar_lista()
        elif op == "4":
            analizar_carpeta()
        elif op == "5":
            run(["main.py", "simular"])
        elif op == "6":
            run(["main.py", "validar"])
        elif op == "7":
            run(["reporte.py"])
        elif op == "0":
            print("Saliendo...")
            break
        else:
            print("[ERROR] Opción inválida.")


if __name__ == "__main__":
    loop()