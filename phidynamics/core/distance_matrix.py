import math

def matriz_distancias(atomos):
    """
    Construye una matriz de distancias euclidianas entre todos los átomos.
    """
    n = len(atomos)
    matriz = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        xi, yi, zi = atomos[i]["x"], atomos[i]["y"], atomos[i]["z"]

        for j in range(i + 1, n):
            xj, yj, zj = atomos[j]["x"], atomos[j]["y"], atomos[j]["z"]

            d = math.sqrt(
                (xi - xj) ** 2 +
                (yi - yj) ** 2 +
                (zi - zj) ** 2
            )

            matriz[i][j] = d
            matriz[j][i] = d

    return matriz