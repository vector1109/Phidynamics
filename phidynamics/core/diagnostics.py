from phidynamics.core.analyze_xyz import analizar_material
from phidynamics.core.phase_runner import correr_experimento
from phidynamics.core.phase_memory import medir_memoria
from phidynamics.core.phase_regime import clasificar_regimen


def diagnosticar(ruta, ciclos=8, plot=False):
    """
    Pipeline MVP unificado:
    estructura -> fase -> absorción -> régimen -> diagnóstico
    """

    # 1. Firma estructural
    firma = analizar_material(ruta)

    # 2. Estado inicial sintético desde firma estructural
    phi = [
        int(firma["atomos"] * 3) % 60,
        int(firma["enlaces"] * 2) % 60,
        int(firma["coordinacion_media"] * 10) % 60,
        7,
        51,
        28,
    ]

    # 3. Delta fijo MVP
    delta = [10, 5, 0, -5, 20, 15]

    # 4. Simulación dinámica
    historial = correr_experimento(phi, delta, ciclos=ciclos, plot=plot)

    absorcion_final = historial[-1]["absorcion"]
    regimen = clasificar_regimen(absorcion_final)

    # 5. Memoria local simple (MVP)
    memoria = medir_memoria([{"absorcion_final": absorcion_final}])

    # 6. Diagnóstico unificado
    return {
        "archivo": ruta,
        "firma": firma["tipo"],
        "dimensionalidad": firma["dimensionalidad"],
        "absorcion_final": absorcion_final,
        "regimen": regimen,
        "memoria": memoria["memoria"],
        "conclusion": f"{firma['tipo']} | régimen {regimen} | memoria {memoria['memoria']}"
    }