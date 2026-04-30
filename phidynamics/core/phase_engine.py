def reduce_phase(valor, base=60):
    """
    Reduce un valor al espacio discreto modular B60.
    """
    return int(valor) % base


def reduce_vector(vector, base=60):
    """
    Reduce un vector completo al espacio B60.
    """
    return [reduce_phase(v, base=base) for v in vector]


def phase_add(a, b, base=60):
    """
    Suma modular de fase.
    """
    return reduce_phase(a + b, base=base)


def phase_diff(a, b, base=60):
    """
    Diferencia modular de fase.
    """
    return reduce_phase(a - b, base=base)


def phase_update(phi_actual, delta_phi, momentum=0.9, lr=0.01, base=60):
    """
    Regla discreta de actualización:

        REDUCE_PHASE(0.9 * Φ + 0.01 * ΔΦ)
    """
    salida = []

    for a, d in zip(phi_actual, delta_phi):
        nuevo = (momentum * a) + (lr * d)
        salida.append(reduce_phase(nuevo, base=base))

    return salida


def phase_absorption(phi):
    """
    Métrica simple de absorción:
    menor dispersión = mayor absorción
    """
    if not phi:
        return 0.0

    media = sum(phi) / len(phi)
    dispersion = sum(abs(x - media) for x in phi) / len(phi)

    return round(10.0 / (1.0 + dispersion), 3)


def ejecutar_ciclo(phi_inicial, delta_phi, ciclos=5, momentum=0.9, lr=0.01, base=60):
    """
    Ejecuta evolución iterativa del estado de fase.
    """
    historial = []
    phi = list(phi_inicial)

    for i in range(ciclos):
        phi = phase_update(phi, delta_phi, momentum=momentum, lr=lr, base=base)
        absorcion = phase_absorption(phi)

        historial.append({
            "ciclo": i + 1,
            "phi": phi[:],
            "absorcion": absorcion
        })

    return historial


def exportar_ciclo(historial, salida="data/phase_history.json"):
    """
    Guarda historial de evolución de fase en JSON.
    """
    import json
    import os

    os.makedirs(os.path.dirname(salida), exist_ok=True)

    with open(salida, "w", encoding="utf-8") as f:
        json.dump(historial, f, indent=2, ensure_ascii=False)

    return salida