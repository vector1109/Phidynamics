import numpy as np
from Bio.PDB import PDBList, PDBParser
from phidynamics.bio.fractal import CrecimientoFractal

# Funciones auxiliares necesarias
def normalizar_coords(coords):
    coords = coords - np.mean(coords, axis=0)
    norma = np.linalg.norm(coords)
    return coords / norma if norma > 0 else coords

def obtener_coords(pdb_id):
    pdbl = PDBList()
    pdbl.retrieve_pdb_file(pdb_id, pdir='.', file_format='pdb')
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(pdb_id, f"pdb{pdb_id.lower()}.ent")
    return np.array([atom.get_coord() for atom in structure.get_atoms() if atom.get_name() in ['CA', 'P']])

# --- Lógica principal ---

# Resonancia 0.3959 encontrada en el escáner previo
h_dna = [(0.5, 0.1, 0.0), (0.2, 0.3959, 0.0)]

# Obtener y procesar datos reales
real_coords = obtener_coords("1BNA")
num_nodos = len(real_coords)
r_norm = normalizar_coords(real_coords)

# Motor con cuantización activada (Snap-to-grid = 0.5A)
engine = CrecimientoFractal(harmonics=h_dna, dual_strand=True, target_dist=20.0, step_size=0.5)
sim_coords = engine.generar_espiral_aurea(num_nodos=num_nodos, cuantizar=True)

# Comparación final
s_norm = normalizar_coords(sim_coords[:num_nodos])
error = np.sqrt(np.mean((s_norm - r_norm)**2))

print(f"--- ANÁLISIS DE ESTRUCTURA DISCRETA ---")
print(f"Error Cuantizado (step=0.5A): {error:.4f}")