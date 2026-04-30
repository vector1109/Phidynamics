import statistics


def medir_memoria(resultados):
    """
    Cuantifica dependencia del sistema respecto al estado inicial.
    Entrada:
        resultados = lista de dicts con clave 'absorcion_final'
    """
    finales = [x["absorcion_final"] for x in resultados]

    if len(finales) < 2:
        return {
            "memoria_std": 0.0,
            "memoria_rango": 0.0,
            "memoria": "indeterminada"
        }

    std = statistics.pstdev(finales)
    rango = max(finales) - min(finales)

    if std < 0.15:
        nivel = "débil"
    elif std < 0.4:
        nivel = "moderada"
    else:
        nivel = "fuerte"

    return {
        "memoria_std": round(std, 3),
        "memoria_rango": round(rango, 3),
        "memoria": nivel
    }