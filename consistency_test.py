import numpy as np
from Bio.PDB import PDBList, PDBParser
from phidynamics.bio.fractal import CrecimientoFractal

# Parámetros base (La "firma" que descubrimos en 1MBN)
AMP, FREQ, PHASE, OFFSET = [0.5, 0.1, 0.0, 0.5]

def normalizar_coords(coords):
    """
    Normalización topológica:
    1. Centra en el origen (0,0,0).
    2. Escala a norma unitaria (mantiene la forma pero fija el tamaño).
    """
    coords = coords - np.mean(coords, axis=0)
    norma = np.linalg.norm(coords)
    return coords / norma if norma > 0 else coords

def procesar_pdb(pdb_id):
    pdbl = PDBList()
    # Descarga el archivo si no existe
    pdbl.retrieve_pdb_file(pdb_id, pdir='.', file_format='pdb')
    parser = PDBParser(QUIET=True)
    # Ajuste: el nombre de archivo descargado suele ser pdb1mbn.ent
    structure = parser.get_structure(pdb_id, f"pdb{pdb_id.lower()}.ent")
    
    # Extraer carbonos alfa
    coords = [res['CA'].get_coord() for model in structure for chain in model for res in chain if 'CA' in res]
    return np.array(coords)

def comparar_normalizado(sim_coords, real_coords):
    # Aseguramos que comparamos el mismo número de puntos
    n = min(len(sim_coords), len(real_coords))
    
    # Normalizamos ambos sets de puntos antes de restar
    sim_norm = normalizar_coords(sim_coords[:n])
    real_coords_norm = normalizar_coords(real_coords[:n])
    
    # Error cuadrático medio de las formas
    return np.sqrt(np.mean((sim_norm - real_coords_norm)**2))

test_set = ["1MBN", "1PG1", "1UBQ"]

print(f"{'PDB ID':<10} | {'Estructura':<20} | {'RMSD (Forma Normalizada)'}")
print("-" * 60)

for pdb_id in test_set:
    try:
        real_coords = procesar_pdb(pdb_id)
        num_nodos = len(real_coords)
        
        # El motor ahora usa una lista de armónicos.
        # Pasamos AMP, FREQ y PHASE definidos arriba.
        engine = CrecimientoFractal(harmonics=[(AMP, FREQ, PHASE)])
        
        # Corrección: El método espera 'num_nodos' y no 'num_puntos'
        sim_coords = engine.generar_espiral_aurea(num_nodos=num_nodos)
        
        error = comparar_normalizado(sim_coords, real_coords)
        print(f"{pdb_id:<10} | {'Test':<20} | {error:.4f}")
    except Exception as e:
        print(f"{pdb_id:<10} | {'Error':<20} | {str(e)}")

print("-" * 60)
print("Interpretación: Si los RMSD son similares (ej: todos en el rango 0.1-0.5),")
