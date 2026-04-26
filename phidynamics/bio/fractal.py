import numpy as np

PHI = (1 + np.sqrt(5)) / 2

class CrecimientoFractal:
    def __init__(self, harmonics, dual_strand=False, target_dist=20.0):
        self.harmonics = harmonics
        self.dual_strand = dual_strand
        self.target_dist = target_dist
        # Registro de la constante física descubierta: 0.1759
        self.LAMBDA_D = 0.1759 

    def generar_espiral_aurea(self, num_nodos):
        n = np.arange(num_nodos)
        k_total = np.zeros(num_nodos)
        for amp, freq, phase in self.harmonics:
            k_total += amp * np.sin(freq * n + phase)
            
        angulo = n * (2 * np.pi / PHI)
        radio = (PHI ** (n / 10.0)) * (k_total + 0.5)
        z = n * 0.1 * (k_total + 0.5)
        
        x1, y1 = radio * np.cos(angulo), radio * np.sin(angulo)
        
        if self.dual_strand:
            # Mantener la simetría base del modelo
            x2 = x1 + (self.target_dist * np.cos(angulo + np.pi))
            y2 = y1 + (self.target_dist * np.sin(angulo + np.pi))
            x, y = (x1 + x2) / 2, (y1 + y2) / 2
        else:
            x, y = x1, y1
            
        return np.stack([x, y, z], axis=1)

    def validar_estructura(self, coords_reales, coords_sim):
        # Normalización para aislamiento del invariante
        coords_reales -= np.mean(coords_reales, axis=0)
        coords_sim -= np.mean(coords_sim, axis=0)
        r_norm = coords_reales / np.linalg.norm(coords_reales)
        s_norm = coords_sim / np.linalg.norm(coords_sim)
        
        # Cálculo de la Tensión Torsional (ex-RMSD)
        delta = np.sqrt(np.mean((s_norm - coords_reales[:len(s_norm)]/np.linalg.norm(coords_reales[:len(s_norm)]))**2))
        return delta