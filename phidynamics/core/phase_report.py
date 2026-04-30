import json


def imprimir_reporte_fase(path="data/phase_stats.json"):
    with open(path, "r", encoding="utf-8") as f:
        s = json.load(f)

    print("\n" + "=" * 60)
    print("REPORTE DINÁMICO DE FASE")
    print("=" * 60)
    print(f"Corridas analizadas:      {s['corridas']}")
    print(f"Absorción final media:    {s['absorcion_final_media']}")
    print(f"Dispersión final:         {s['absorcion_final_std']}")
    print(f"Absorción media global:   {s['absorcion_media_global']}")
    print(f"Robustez:                 {s['robustez']}")
    print()
    print("Distribución de régimen:")
    print(f"  Estable:                {s['regimenes']['estable']}")
    print(f"  Saturado:               {s['regimenes']['saturado']}")
    print(f"  Disipativo:             {s['regimenes']['disipativo']}")
    print()
    print("Mejor corrida:")
    print(f"  ID:                     {s['mejor_corrida']['corrida']}")
    print(f"  ΔΦ:                     {s['mejor_corrida']['delta']}")
    print(f"  Absorción final:        {s['mejor_corrida']['absorcion_final']}")
    print("=" * 60)