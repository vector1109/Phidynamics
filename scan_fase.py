import numpy as np
from Bio.PDB import PDBList, PDBParser
from phidynamics.bio.fractal import CrecimientoFractal

# Funciones auxiliares
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

# Resonancia encontrada previamente
h_dna = [(0.5, 0.1, 0.0), (0.2, 0.3959, 0.0)]
real_coords = obtener_coords("1BNA")
num_nodos = len(real_coords)
r_norm = normalizar_coords(real_coords)

print("Desfasaje (rad) | RMSD Normalizado")
print("-----------------------------------")

mejor_fase = 0
menor_error = float('inf')

# Barrido de 0 a 2*pi en 50 pasos
fases = np.linspace(0, 2 * np.pi, 50)

for fase in fases:
    engine = CrecimientoFractal(harmonics=h_dna, dual_strand=True, target_dist=20.0, target_phase=fase)
    sim_coords = engine.generar_espiral_aurea(num_nodos=num_nodos)
    
    s_norm = normalizar_coords(sim_coords[:num_nodos])
    error = np.sqrt(np.mean((s_norm - r_norm)**2))
    
    print(f"{fase:.4f}          | {error:.4f}")
    
    if error < menor_error:
        menor_error = error
        mejor_fase = fase

print("-----------------------------------")
print(f"Fase Óptima Encontrada: {mejor_fase:.4f} rad ({np.degrees(mejor_fase):.1f} grados)")
print(f"Error Mínimo Alcanzado: {menor_error:.4f}")