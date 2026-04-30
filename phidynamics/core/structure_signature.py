import math


def _centroide(atomos):
    n = len(atomos)
    if n == 0:
        return (0.0, 0.0, 0.0)

    sx = sum(a["x"] for a in atomos)
    sy = sum(a["y"] for a in atomos)
    sz = sum(a["z"] for a in atomos)
    return (sx / n, sy / n, sz / n)


def _dispersión_por_eje(atomos):
    """
    Calcula dispersión espacial en X/Y/Z respecto al centroide.
    """
    cx, cy, cz = _centroide(atomos)
    n = len(atomos)

    if n == 0:
        return (0.0, 0.0, 0.0)

    dx = sum((a["x"] - cx) ** 2 for a in atomos) / n
    dy = sum((a["y"] - cy) ** 2 for a in atomos) / n
    dz = sum((a["z"] - cz) ** 2 for a in atomos) / n

    return (dx, dy, dz)


def _anisotropia(atomos):
    """
    Mide cuán elongada / plana / balanceada es la nube.
    """
    dx, dy, dz = _dispersión_por_eje(atomos)
    vals = sorted([dx, dy, dz], reverse=True)

    if vals[0] <= 1e-9:
        return (0.0, 0.0)

    ratio_1 = vals[1] / vals[0]   # segunda dimensión relativa
    ratio_2 = vals[2] / vals[0]   # tercera dimensión relativa
    return (ratio_1, ratio_2)


def _dimensionalidad(atomos):
    """
    Estima dimensionalidad efectiva:
    1D = lineal
    2D = plano
    3D = volumétrico
    """
    r1, r2 = _anisotropia(atomos)

    if r1 < 0.20:
        return "1D"

    if r1 >= 0.20 and r2 < 0.20:
        return "2D"

    return "3D"


# PASO 1 - Nueva función _ciclicidad
def _ciclicidad(enlaces, n):
    """
    Estima ciclicidad local:
    proporción de nodos involucrados en al menos un ciclo simple.
    """
    vecinos = {i: set() for i in range(n)}

    for i, j, _ in enlaces:
        vecinos[i].add(j)
        vecinos[j].add(i)

    en_ciclo = set()

    for nodo in range(n):
        vn = list(vecinos[nodo])

        for i in range(len(vn)):
            for j in range(i + 1, len(vn)):
                a = vn[i]
                b = vn[j]

                # si dos vecinos de un nodo también se conectan,
                # hay un ciclo local
                if b in vecinos[a]:
                    en_ciclo.add(nodo)
                    en_ciclo.add(a)
                    en_ciclo.add(b)

    if n == 0:
        return 0.0

    return len(en_ciclo) / n


def clasificar_estructura(atomos, enlaces, coordinacion):
    """
    Clasificación estructural por:
    - conectividad
    - anisotropía espacial
    - dimensionalidad efectiva
    - ciclicidad local
    """
    n = len(atomos)
    total_enlaces = len(enlaces)
    coord_media = sum(coordinacion) / n if n else 0.0

    r1, r2 = _anisotropia(atomos)
    dim = _dimensionalidad(atomos)
    
    # PASO 2 - Calcular ciclicidad
    cic = _ciclicidad(enlaces, n)

    # PASO 3 - Diccionario firma con ciclicidad
    firma = {
        "atomos": n,
        "enlaces": total_enlaces,
        "coordinacion_media": round(coord_media, 3),
        "dimensionalidad": dim,
        "anisotropia": (round(r1, 3), round(r2, 3)),
        "ciclicidad": round(cic, 3),
        "tipo": "indeterminado"
    }

    # --- Clasificación topológica real ---

    if dim == "1D":
        if coord_media <= 2.2:
            firma["tipo"] = "cadena / lineal"
        else:
            firma["tipo"] = "fibra / red lineal"

    elif dim == "2D":
        if 2.3 <= coord_media <= 3.3:
            firma["tipo"] = "grafeno / red hexagonal"
        else:
            firma["tipo"] = "lámina / red plana"

    elif dim == "3D":
        if coord_media <= 2.0:
            firma["tipo"] = "amorfo / red irregular"
        elif 2.0 < coord_media < 4.0:
            firma["tipo"] = "cluster / tetraédrico"
        elif 4.0 <= coord_media < 5.5:
            firma["tipo"] = "red tetraédrica / cristal"
        else:
            firma["tipo"] = "cristal compacto"

    return firma