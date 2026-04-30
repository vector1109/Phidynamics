import json
import matplotlib.pyplot as plt


def graficar_historial_fase(path="data/phase_history.json"):
    """
    Grafica estabilidad por ciclo.
    """
    with open(path, "r", encoding="utf-8") as f:
        historial = json.load(f)

    ciclos = [x["ciclo"] for x in historial]
    absorcion = [x["absorcion"] for x in historial]

    plt.figure(figsize=(8, 4))
    plt.plot(ciclos, absorcion, marker="o")
    plt.title("Evolución de Absorción de Fase")
    plt.xlabel("Ciclo")
    plt.ylabel("Absorción")
    plt.grid(True)
    plt.tight_layout()
    plt.show()