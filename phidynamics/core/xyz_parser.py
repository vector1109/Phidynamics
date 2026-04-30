from pathlib import Path

def cargar_xyz(ruta):
    """
    Lee un archivo XYZ y devuelve una lista de átomos con coordenadas.
    """
    ruta = Path(ruta)

    if not ruta.exists():
        raise FileNotFoundError(f"No existe el archivo: {ruta}")

    lineas = ruta.read_text(encoding="utf-8").splitlines()

    if len(lineas) < 3:
        raise ValueError("Archivo XYZ inválido o incompleto.")

    atomos = []

    for linea in lineas[2:]:  # saltamos cabecera XYZ
        partes = linea.split()
        if len(partes) < 4:
            continue

        atomos.append({
            "atom": partes[0],
            "x": float(partes[1]),
            "y": float(partes[2]),
            "z": float(partes[3]),
        })

    return atomos