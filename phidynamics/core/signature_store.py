import json
from pathlib import Path


BASE = Path("data/signatures")
BASE.mkdir(parents=True, exist_ok=True)


def _ruta_firma(nombre_archivo):
    nombre = Path(nombre_archivo).stem
    return BASE / f"{nombre}.signature.json"


def guardar_firma(nombre_archivo, firma):
    ruta = _ruta_firma(nombre_archivo)

    payload = {"archivo": Path(nombre_archivo).name, **firma}

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    return ruta


def cargar_firma(nombre_archivo):
    ruta = _ruta_firma(nombre_archivo)

    if not ruta.exists():
        return None

    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


def listar_firmas():
    firmas = []

    for archivo in BASE.glob("*.signature.json"):
        with open(archivo, "r", encoding="utf-8") as f:
            firmas.append(json.load(f))

    return firmas