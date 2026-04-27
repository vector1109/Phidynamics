import numpy as np

# Constante Áurea Soberana
PHI = (1 + 5**0.5) / 2

class CrecimientoFractal:
    """
    Motor de generación fractal basado en armónicos y la proporción áurea.
    Ajustado para compatibilidad total con la suite de validación y PDB.
    """
    def __init__(self, torsion_intensity=1.0, harmonics=None, dual_strand=False, 
                 target_dist=20.0, target_phase=0.0, step_size=0.5):
        
        # Parámetro de escalado para optimización (minimize)
        self.torsion_intensity = torsion_intensity
        
        # Si harmonics es None (como en la validación), iniciamos lista vacía
        self.harmonics = harmonics if harmonics is not None else []
        self.dual_strand = dual_strand
        self.target_dist = target_dist
        self.target_phase = target_phase
        self.step_size = step_size
        self.LAMBDA_D = 0.1759 

    def generar_espiral_aurea(self, num_puntos, cuantizar=False, aplicar_proyeccion=False):
        """
        Genera la geometría fractal. 
        Nota: 'num_puntos' sincronizado con validate_with_pdb.py
        """
        n = np.arange(num_puntos)
        k_total = np.zeros(num_puntos)
        
        # Inyectar la intensidad de torsión en la sumatoria de armónicos
        # Si no hay armónicos (fase de búsqueda inicial), k_total permanece en 0
        for amp, freq, phase in self.harmonics:
            k_total += (amp * self.torsion_intensity) * np.sin(freq * n + phase + self.target_phase)
            
        # Geometría fundamental
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
        
        # Cuantización para estabilidad en rejilla (sexagesimal transport)
        if cuantizar:
            coords = np.round(coords / self.step_size) * self.step_size
            
        return coords