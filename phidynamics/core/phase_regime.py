def clasificar_regimen(absorcion_final):
    """
    Clasifica el régimen dinámico según absorción final.
    """

    if absorcion_final >= 1.41:
        return "estable"

    elif 1.37 <= absorcion_final < 1.41:
        return "saturado"

    return "disipativo"