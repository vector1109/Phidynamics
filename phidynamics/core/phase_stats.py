import json
import statistics

from phidynamics.core.phase_regime import clasificar_regimen


def analizar_sweep(path="data/phase_sweep.json"):
    """
    Analiza resultados agregados del barrido experimental.
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    finales = [x["absorcion_final"] for x in data]
    medias = [x["absorcion_media"] for x in data]

    for row in data:
        row["regimen"] = clasificar_regimen(row["absorcion_final"])

    resumen = {
        "corridas": len(data),
        "absorcion_final_media": round(statistics.mean(finales), 3),
        "absorcion_final_std": round(statistics.pstdev(finales), 3),
        "absorcion_media_global": round(statistics.mean(medias), 3),
        "mejor_corrida": max(data, key=lambda x: x["absorcion_final"]),
        "robustez": "alta" if statistics.pstdev(finales) < 0.05 else "media",
        "regimenes": {
            "estable": sum(1 for x in data if x["regimen"] == "estable"),
            "saturado": sum(1 for x in data if x["regimen"] == "saturado"),
            "disipativo": sum(1 for x in data if x["regimen"] == "disipativo"),
        }
    }

    with open("data/phase_stats.json", "w", encoding="utf-8") as f:
        json.dump(resumen, f, indent=2)

    return resumen