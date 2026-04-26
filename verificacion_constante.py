import numpy as np
from Bio.PDB import PDBList, PDBParser
from phidynamics.bio.fractal import CrecimientoFractal

# --- Motor de Diagnóstico ---
def clasificar_estado(delta):
    # Umbral de decisión basado en tus hallazgos empíricos
    if abs(delta - 0.1759) < 0.05:
        return "B-DNA (Fase Biológica Activa / Tensión Codificante)"
    elif abs(delta - 0.0400) < 0.05:
        return "ADN Estructural (Fase Geométrica Relajada)"
    else:
        return "Estado Indeterminado / Transicional"

def obtener_coords(pdb_id):
    pdbl = PDBList()
    pdbl.retrieve_pdb_file(pdb_id, pdir='.', file_format='pdb')
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(pdb_id, f"pdb{pdb_id.lower()}.ent")
    return np.array([atom.get_coord() for atom in structure.get_atoms() if atom.get_name() in ['CA', 'P']])

# --- Lógica Principal ---
h_dna = [(0.5, 0.1, 0.0), (0.2, 0.3959, 0.0)]
engine = CrecimientoFractal(harmonics=h_dna, dual_strand=True)

# Lista de validación expandida
targets = ["1BNA", "1D02", "1D65"] 

print(f"{'Estructura':<10} | {'Firma (Delta)':<15} | {'Diagnóstico de Estado'}")
print("-" * 65)

for target in targets:
    try:
        real = obtener_coords(target)
        sim = engine.generar_espiral_aurea(num_nodos=len(real))
        delta = engine.validar_estructura(real, sim)
        estado = clasificar_estado(delta)
        print(f"{target:<10} | {delta:.4f}          | {estado}")
    except Exception as e:
        print(f"{target:<10} | Error: {e}")

print("-" * 65)
print("Análisis de Estados Finalizado.")