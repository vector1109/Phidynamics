import numpy as np
from Bio.PDB import PDBList, PDBParser
from phidynamics.bio.fractal import CrecimientoFractal

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

# Definición de la firma del ADN con frecuencia de resonancia 0.3959
h_dna = [(0.5, 0.1, 0.0), (0.2, 0.3959, 0.0)] 

real_coords = obtener_coords("1BNA")
num_nodos = len(real_coords)
r_norm = normalizar_coords(real_coords)

# Inicializamos el motor con la Restricción de Distancia (20.0 Angstroms)
engine = CrecimientoFractal(harmonics=h_dna, dual_strand=True, target_dist=20.0)
sim_coords = engine.generar_espiral_aurea(num_nodos=num_nodos)

# Comparación final
s_norm = normalizar_coords(sim_coords[:num_nodos])
error = np.sqrt(np.mean((s_norm - r_norm)**2))

print(f"ID: 1BNA (ADN)")
print(f"Configuración: Armónica (f=0.3959) + Restricción Física (20A)")
print(f"RMSD Normalizado: {error:.4f}")