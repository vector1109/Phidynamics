import json
import os

from phidynamics.core.phase_runner import correr_experimento


def barrer_fase(phi_base, deltas, ciclos=8, salida="data/phase_sweep.json"):
    """
    Ejecuta múltiples corridas con distintas perturbaciones
    y guarda resultados experimentales.
    """
    resultados = []

    for i, delta in enumerate(deltas, start=1):
        print(f"\n[SWEEP] Corrida {i}/{len(deltas)}")
        historial = correr_experimento(phi_base, delta, ciclos=ciclos, plot=False)

        absorciones = [x["absorcion"] for x in historial]

        resultados.append({
            "corrida": i,
            "delta": delta,
            "absorcion_final": absorciones[-1],
            "absorcion_media": round(sum(absorciones) / len(absorciones), 3)
        })

    os.makedirs(os.path.dirname(salida), exist_ok=True)

    with open(salida, "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False)

    print(f"\n[SWEEP] Resultados guardados en: {salida}")
    return resultados