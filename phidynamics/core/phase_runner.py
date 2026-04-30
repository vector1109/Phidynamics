from phidynamics.core.phase_engine import ejecutar_ciclo, exportar_ciclo
from phidynamics.core.phase_plot import graficar_historial_fase


def correr_experimento(phi, delta, ciclos=10, plot=True):
    """
    Ejecuta experimento completo de fase:
    evolución -> persistencia -> visualización -> resumen
    """
    historial = ejecutar_ciclo(phi, delta, ciclos=ciclos)
    ruta = exportar_ciclo(historial)

    print(f"[PHASE] Historial guardado en: {ruta}")

    absorciones = [x["absorcion"] for x in historial]
    inicial = absorciones[0]
    final = absorciones[-1]
    mejora = round(final - inicial, 3)
    media = round(sum(absorciones) / len(absorciones), 3)

    print("[PHASE] Resumen experimental")
    print(f"  Ciclos:               {ciclos}")
    print(f"  Absorción inicial:    {inicial}")
    print(f"  Absorción final:      {final}")
    print(f"  Mejora neta:          {mejora}")
    print(f"  Convergencia media:   {media}")

    if plot:
        graficar_historial_fase(ruta)

    return historial