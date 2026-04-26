import numpy as np

PHI = (1 + np.sqrt(5)) / 2

class CrecimientoFractal:
    def __init__(self, harmonics, dual_strand=False):
        """
        harmonics: Lista de tuplas [(amp, freq, phase), ...]
        """
        self.harmonics = harmonics
        self.dual_strand = dual_strand

    def generar_espiral_aurea(self, num_nodos):
        n = np.arange(num_nodos)
        
        # Calcular torsión total sumando armónicos (Serie de Fourier)
        k_total = np.zeros(num_nodos)
        for amp, freq, phase in self.harmonics:
            k_total += amp * np.sin(freq * n + phase)
            
        angulo = n * (2 * np.pi / PHI)
        radio = (PHI ** (n / 10.0)) * (k_total + 0.5) # +0.5 para offset base
        z = n * 0.1 * (k_total + 0.5)
        
        x1 = radio * np.cos(angulo)
        y1 = radio * np.sin(angulo)
        
        if self.dual_strand:
            x2 = radio * np.cos(angulo + np.pi)
            y2 = radio * np.sin(angulo + np.pi)
            x, y = (x1 + x2) / 2, (y1 + y2) / 2
        else:
            x, y = x1, y1
            
        return np.stack([x, y, z], axis=1)