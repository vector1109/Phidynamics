from pathlib import Path

from phidynamics.core.xyz_parser import cargar_xyz
from phidynamics.core.distance_matrix import matriz_distancias
from phidynamics.core.structure_signature import clasificar_estructura
from phidynamics.core.similarity import similitud_firmas
from phidynamics.core.bond_detector import detectar_enlaces
from phidynamics.core.signature_store import cargar_firma


def firma_desde_xyz(path):
    firma = cargar_firma(path)

    if firma is not None:
        return firma

    atomos = cargar_xyz(path)
    dist = matriz_distancias(atomos)
    enlaces, coord = detectar_enlaces(atomos, dist)
    return clasificar_estructura(atomos, enlaces, coord)


def comparar_estructuras(a_path, b_path):
    a = Path(a_path)
    b = Path(b_path)

    if not a.exists():
        print(f"[!] No existe archivo A: {a}")
        return

    if not b.exists():
        print(f"[!] No existe archivo B: {b}")
        return

    firma_a = firma_desde_xyz(a)
    firma_b = firma_desde_xyz(b)

    score = similitud_firmas(firma_a, firma_b)

    print(f"\n{'='*60}")
    print("COMPARACIÓN ESTRUCTURAL")
    print(f"{'='*60}\n")

    print(f"A: {a.name}")
    print(f"   Tipo: {firma_a['tipo']}")
    print(f"   Dim:  {firma_a['dimensionalidad']}")
    print(f"   Coord:{firma_a['coordinacion_media']}\n")

    print(f"B: {b.name}")
    print(f"   Tipo: {firma_b['tipo']}")
    print(f"   Dim:  {firma_b['dimensionalidad']}")
    print(f"   Coord:{firma_b['coordinacion_media']}\n")

    print(f"Similitud estructural: {score:.4f}")

    if score >= 0.85:
        conclusion = "estructuras casi equivalentes"
    elif score >= 0.65:
        conclusion = "misma familia estructural"
    elif score >= 0.45:
        conclusion = "similitud parcial"
    else:
        conclusion = "estructuras diferentes"

    print(f"Conclusión: {conclusion}")
    print(f"{'='*60}\n")