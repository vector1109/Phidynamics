import numpy as np
from Bio.PDB import PDBList, PDBParser
from phidynamics.bio.fractal import CrecimientoFractal

# Definición de Firmas Armónicas
# Proteína: Resonancia simple
# ADN: Resonancia acoplada con armónica de pitch (0.5)
harmonics_protein = [(0.5, 0.1, 0.0)]
harmonics_dna = [(0.5, 0.1, 0.0), (0.2, 0.5, 0.0)]

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

test_set = ["1MBN", "1BNA"]

print(f"{'ID':<10} | {'Configuración':<20} | {'RMSD Normalizado'}")
print("-" * 55)

for pdb_id in test_set:
    es_adn = (pdb_id == "1BNA")
    h = harmonics_dna if es_adn else harmonics_protein
    
    real_coords = obtener_coords(pdb_id)
    num_nodos = len(real_coords)
    
    engine = CrecimientoFractal(harmonics=h, dual_strand=es_adn)
    sim_coords = engine.generar_espiral_aurea(num_nodos=num_nodos)
    
    # Comparación
    s_norm = normalizar_coords(sim_coords[:num_nodos])
    r_norm = normalizar_coords(real_coords)
    error = np.sqrt(np.mean((s_norm - r_norm)**2))
    
    print(f"{pdb_id:<10} | {'ADN Armónico' if es_adn else 'Proteína Base':<20} | {error:.4f}")