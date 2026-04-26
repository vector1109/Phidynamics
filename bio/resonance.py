# Phidynamics - Módulo de Resonancia Electromagnética
class BioResonancia:
    def __init__(self):
        self.SCHUMANN_BASE = 7.83  # Hz
        self.DELTA_BASE = 0.0400   # Firma de reposo

    def calcular_frecuencia(self, delta_actual):
        if delta_actual <= 0: return 0.0
        ratio = delta_actual / self.DELTA_BASE
        return self.SCHUMANN_BASE * ratio

    def get_banda_espectral(self, f):
        if f < 13: return "Alfa (Base/Storage)"
        if f < 30: return "Beta (Actividad Codificante)"
        return "Gamma (Procesamiento/Alta Energía)"