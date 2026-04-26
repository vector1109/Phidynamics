import json
import os
from datetime import datetime

ARCHIVO_DB = "data/bitacora_investigacion.json"

def guardar_resultado(pdb_id, delta, frecuencia, banda):
    nuevo_registro = {
        "timestamp": datetime.now().isoformat(),
        "pdb_id": pdb_id,
        "delta": round(delta, 4),
        "frecuencia_hz": round(frecuencia, 2),
        "banda": banda
    }

    data = []
    if os.path.exists(ARCHIVO_DB):
        with open(ARCHIVO_DB, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    data.append(nuevo_registro)

    with open(ARCHIVO_DB, "w") as f:
        json.dump(data, f, indent=4)
        
    print(f"\n[PERSISTENCIA] Registro añadido a: {ARCHIVO_DB}")