import numpy as np

PHI = (1 + 5**0.5) / 2

class CrecimientoFractal:
    def __init__(self, harmonics, dual_strand=False, target_dist=20.0, target_phase=0.0, step_size=0.5):
        self.harmonics = harmonics
        self.dual_strand = dual_strand
        self.target_dist = target_dist
        self.target_phase = target_phase
        self.step_size = step_size
        self.LAMBDA_D = 0.1759 

    def generar_espiral_aurea(self, num_nodos, cuantizar=False, aplicar_proyeccion=False):
        n = np.arange(num_nodos)
        k_total = np.zeros(num_nodos)
        
        for amp, freq, phase in self.harmonics:
            k_total += amp * np.sin(freq * n + phase + self.target_phase)
            
        angulo = n * (2 * np.pi / PHI)
        radio = (PHI ** (n / 10.0)) * (k_total + 0.5)
        z = n * 0.1 * (k_total + 0.5)
        
        x1, y1 = radio * np.cos(angulo), radio * np.sin(angulo)
        
        if self.dual_strand:
            x2 = x1 + (self.target_dist * np.cos(angulo + np.pi))
            y2 = y1 + (self.target_dist * np.sin(angulo + np.pi))
            x, y = (x1 + x2) / 2, (y1 + y2) / 2
        else:
            x, y = x1, y1
            
        coords = np.stack([x, y, z], axis=1)
        
        # Aplicar cuantización si se solicita
        if cuantizar:
            coords = np.round(coords / self.step_size) * self.step_size
            
        # Lógica de proyección (placeholder para futura implementación física)
        if aplicar_proyeccion:
            # Aquí inyectarás la lógica de transformación de proyección cuando la necesites
            pass
            
        return coords