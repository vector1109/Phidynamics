RADIOS = {
    "H": 0.31,
    "C": 0.76,
    "N": 0.71,
    "O": 0.66,
    "P": 1.07,
    "S": 1.05,
    "SI": 1.11,
}


def detectar_enlaces(atomos, matriz, tolerancia=0.45):
    """
    Detecta enlaces probables usando radios covalentes aproximados.
    """
    enlaces = []
    coordinacion = [0] * len(atomos)

    for i in range(len(atomos)):
        ai = atomos[i]["atom"].upper()
        ri = RADIOS.get(ai, 0.8)

        for j in range(i + 1, len(atomos)):
            aj = atomos[j]["atom"].upper()
            rj = RADIOS.get(aj, 0.8)

            d = matriz[i][j]
            limite = ri + rj + tolerancia

            if 0.0 < d <= limite:
                enlaces.append((i, j, d))
                coordinacion[i] += 1
                coordinacion[j] += 1

    return enlaces, coordinacion