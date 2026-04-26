import math

# --- Proporción Áurea ---
PHI = (1.0 + math.sqrt(5.0)) / 2.0 

# --- Constantes Biogemétricas ---
# Rigidez Torsional (k_S): Define la resistencia del espacio-tiempo local
KS_BIOLOGICAL = 1e30  

# Elasticidad Geométrica (k_E): Amplitud de la oscilación temporal OAM
KE_ELASTICITY = 1e-10

# Frecuencia OAM (ω): Velocidad de rotación del eje temporal
OMEGA_OAM = 1.0 

# Constantes Físicas estándar
C_LUZ = 299792458.0
HBAR = 1.0545718e-34