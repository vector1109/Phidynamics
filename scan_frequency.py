import numpy as np
from Bio.PDB import PDBList, PDBParser
from phidynamics.bio.fractal import CrecimientoFractal

# Funciones de utilidad (mantenemos la estructura de normalización)
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

# Escaneo de Espectro
real_coords = obtener_coords("1BNA")
num_nodos = len(real_coords)
r_norm = normalizar_coords(real_coords)

best_rmsd = float('inf')
best_freq = 0

print(f"{'Frecuencia':<15} | {'RMSD Normalizado'}")
print("-" * 35)

# Barrido de frecuencias: de 0.1 a 3.0 con 50 pasos
for f in np.linspace(0.1, 3.0, 50):
    # Armónico base + Frecuencia variable
    h = [(0.5, 0.1, 0.0), (0.2, f, 0.0)]
    
    engine = CrecimientoFractal(harmonics=h, dual_strand=True)
    sim_coords = engine.generar_espiral_aurea(num_nodos=num_nodos)
    
    s_norm = normalizar_coords(sim_coords[:num_nodos])
    error = np.sqrt(np.mean((s_norm - r_norm)**2))
    
    if error < best_rmsd:
        best_rmsd = error
        best_freq = f
        
    print(f"{f:.4f}          | {error:.4f}")

print("-" * 35)
print(f"Resonancia Encontrada: {best_freq:.4f} con un error de {best_rmsd:.4f}")