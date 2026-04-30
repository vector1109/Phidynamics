import math


def vector_firma(firma):
    """
    Convierte firma estructural en vector normalizado.
    Se prioriza geometría sobre tamaño bruto.
    """
    dim_map = {
        "1D": 0.0,
        "2D": 1.0,
        "3D": 2.0
    }

    r1, r2 = firma.get("anisotropia", (0.0, 0.0))
    
    # PASO 1 - Obtener ciclicidad
    cic = float(firma.get("ciclicidad", 0.0))

    atomos = float(firma.get("atomos", 0))
    enlaces = float(firma.get("enlaces", 0))
    coord = float(firma.get("coordinacion_media", 0.0))
    dim = float(dim_map.get(firma.get("dimensionalidad", "0D"), 0.0))

    # Normalización (tamaño pesa poco)
    atomos_n = min(atomos / 50.0, 1.0)
    enlaces_n = min(enlaces / 100.0, 1.0)
    coord_n = min(coord / 8.0, 1.0)

    # PASO 2 - Vector con ciclicidad
    return [
        atomos_n * 0.05,   # tamaño (muy bajo peso)
        enlaces_n * 0.10,  # conectividad bruta
        coord_n * 0.20,    # coordinación
        dim * 0.30,        # régimen geométrico
        float(r1) * 0.10,  # anisotropía eje 2
        float(r2) * 0.10,  # anisotropía eje 3
        cic * 0.15,        # topología local (ciclos)
    ]


def distancia_firmas(f1, f2):
    """
    Distancia euclídea entre firmas estructurales normalizadas.
    """
    v1 = vector_firma(f1)
    v2 = vector_firma(f2)

    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))


def similitud_firmas(f1, f2):
    """
    Similaridad estructural con penalización topológica.
    """
    d = distancia_firmas(f1, f2)
    score = max(0.0, 1.0 - d)

    dim1 = f1.get("dimensionalidad", "0D")
    dim2 = f2.get("dimensionalidad", "0D")

    # Penalización topológica discreta
    if dim1 != dim2:
        score *= 0.55

    return max(0.0, score)