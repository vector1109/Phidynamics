import torch
from .constants import PHI, KE_ELASTICITY, OMEGA_OAM, C_LUZ

class RiemannCartanEngine:
    """Motor de Geometría de Riemann-Cartan con Tiempo OAM."""
    
    def __init__(self, time_t: float):
        self.t = time_t
        self.dim = 4

    def get_helical_metric(self, scale_a: float):
        """Calcula la métrica con dependencia OAM."""
        # g00 con rotación temporal
        factor_rotacion = 1.0 + (KE_ELASTICITY / (scale_a**2)) * torch.cos(torch.tensor(PHI * OMEGA_OAM * self.t))
        g_00 = - (C_LUZ**2) * factor_rotacion
        
        # Métrica esférica simplificada
        g = torch.diag(torch.tensor([g_00, scale_a**2, scale_a**2, scale_a**2], dtype=torch.double))
        return g

    def calculate_contorsion(self, torsion_tensor, metric):
        """Calcula el tensor de contorsión K."""
        # Simplificación inicial: K es proporcional a la Torsión en este framework
        return 0.5 * torsion_tensor