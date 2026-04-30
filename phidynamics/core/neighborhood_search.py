from pathlib import Path
from collections import Counter

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


def buscar_vecinos(objetivo, carpeta):
    """
    Busca vecinos estructurales y calcula familia dominante.
    """
    objetivo = Path(objetivo)
    carpeta = Path(carpeta)

    if not objetivo.exists():
        print(f"[!] No existe archivo objetivo: {objetivo}")
        return

    if not carpeta.exists() or not carpeta.is_dir():
        print(f"[!] Carpeta inválida: {carpeta}")
        return

    firma_obj = firma_desde_xyz(objetivo)
    resultados = []

    for archivo in carpeta.glob("*.xyz"):
        if archivo.resolve() == objetivo.resolve():
            continue

        firma_ref = firma_desde_xyz(archivo)
        score = similitud_firmas(firma_obj, firma_ref)

        resultados.append({
            "archivo": archivo.name,
            "tipo": firma_ref["tipo"],
            "score": score
        })

    resultados.sort(key=lambda x: x["score"], reverse=True)

    print(f"\n{'='*60}")
    print("BÚSQUEDA DE VECINDAD ESTRUCTURAL")
    print(f"{'='*60}")
    print(f"\nObjetivo: {objetivo.name}")
    print(f"Tipo:     {firma_obj['tipo']}")
    print(f"{'-'*60}")

    for i, r in enumerate(resultados, 1):
        print(f"{i:>2}. {r['archivo']:<20} {r['score']:.4f}   {r['tipo']}")

    if resultados:
        mejor = resultados[0]
        print(f"\nVecino más cercano: {mejor['archivo']} ({mejor['score']:.4f})")

        top_n = resultados[:3]
        familias = [r["tipo"] for r in top_n]
        votos = Counter(familias)

        familia_dominante, frecuencia = votos.most_common(1)[0]
        confianza = frecuencia / len(top_n)

        print(f"Familia dominante:  {familia_dominante}")
        print(f"Confianza local:    {confianza:.2f}")

    print(f"{'='*60}\n")