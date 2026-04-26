import numpy as np
from Bio.PDB import PDBList, PDBParser
from phidynamics.bio.fractal import CrecimientoFractal

# Parámetros validados
AMP, FREQ, PHASE, OFFSET = [0.5, 0.1, 0.0, 0.5]

def normalizar_coords(coords):
    coords = coords - np.mean(coords, axis=0)
    norma = np.linalg.norm(coords)
    return coords / norma if norma > 0 else coords

def obtener_coords(pdb_id):
    pdbl = PDBList()
    pdbl.retrieve_pdb_file(pdb_id, pdir='.', file_format='pdb')
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(pdb_id, f"pdb{pdb_id.lower()}.ent")
    
    # Extraer átomos (C-alfa en proteínas, Fosfatos en ADN)
    atoms = [atom.get_coord() for atom in structure.get_atoms() if atom.get_name() in ['CA', 'P']]
    return np.array(atoms)

# Test set: Proteínas (MBN, POR) y ADN (BNA)
test_set = ["1MBN", "2POR", "1BNA"]

print(f"{'ID':<10} | {'Tipo':<15} | {'RMSD Normalizado'}")
print("-" * 50)

for pdb_id in test_set:
    real_coords = obtener_coords(pdb_id)
    num_nodos = len(real_coords)
    
    # Lógica de sincronización: El ADN exige torsión acoplada
    es_adn = (pdb_id == "1BNA")
    
    n = np.arange(num_nodos)
    k_variable = AMP * np.sin(FREQ * n + PHASE) + OFFSET
    
    # Inicializamos con modo dual activo para ADN
    engine = CrecimientoFractal(torsion_intensity=k_variable, dual_strand=es_adn)
    sim_coords = engine.generar_espiral_aurea(num_puntos=num_nodos)
    
    # Comparar formas normalizadas
    s_norm = normalizar_coords(sim_coords[:num_nodos])
    r_norm = normalizar_coords(real_coords)
    error = np.sqrt(np.mean((s_norm - r_norm)**2))
    
    tipo = "ADN Acoplado" if es_adn else "Proteína"
    print(f"{pdb_id:<10} | {tipo:<15} | {error:.4f}")