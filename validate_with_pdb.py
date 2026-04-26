import numpy as np
from Bio.PDB import PDBList, PDBParser
from phidynamics.bio.fractal import CrecimientoFractal
from scipy.optimize import minimize

def obtener_coordenadas_reales(pdb_id="1MBN"):
    print(f"📥 Cargando datos de PDB {pdb_id}...")
    pdbl = PDBList()
    pdbl.retrieve_pdb_file(pdb_id, pdir='.', file_format='pdb')
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(pdb_id, f"pdb{pdb_id.lower()}.ent")
    
    coords = []
    for model in structure:
        for chain in model:
            for residue in chain:
                if 'CA' in residue:
                    coords.append(residue['CA'].get_coord())
    return np.array(coords)

def comparar_estructuras(phidynamics_puntos, pdb_coordenadas):
    # Aseguramos que solo comparamos la longitud disponible
    n = min(len(phidynamics_puntos), len(pdb_coordenadas))
    return np.sqrt(np.mean((phidynamics_puntos[:n] - pdb_coordenadas[:n])**2))

# --- Configuración ---
coords_reales = obtener_coordenadas_reales("1MBN")
num_nodos = len(coords_reales)

def funcion_objetivo_variable(params):
    amp, freq, phase, offset = params
    n = np.arange(num_nodos)
    
    # Generar onda de torsión
    k_variable = amp * np.sin(freq * n + phase) + offset
    
    # Generar estructura (Retorna numpy array (N,3))
    biogrow = CrecimientoFractal(torsion_intensity=k_variable)
    estructura = biogrow.generar_espiral_aurea(num_puntos=num_nodos)
    
    return comparar_estructuras(estructura, coords_reales)

# --- Optimización ---
print(f"🧬 Iniciando búsqueda de ONDA DE TORSIÓN (Vectorizada) para {num_nodos} nodos...")

resultado = minimize(
    funcion_objetivo_variable, 
    x0=[0.5, 0.1, 0.0, 0.5], 
    method='Nelder-Mead',
    options={'maxiter': 1000}
)

print("-" * 50)
print(f"✅ Optimización completada.")
print(f"   RMSD Final: {resultado.fun:.4f}")
print("-" * 50)