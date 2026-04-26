import requests
import os
import sys

def descargar_pdb(pdb_id, directorio_destino="data"):
    """
    Descarga una estructura PDB desde el repositorio oficial de RCSB.
    Mantiene la soberanía sobre el archivo descargado.
    """
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)
        print(f"[INFO] Creado directorio: {directorio_destino}")

    url = f"https://files.rcsb.org/download/{pdb_id.lower()}.pdb"
    ruta_archivo = os.path.join(directorio_destino, f"{pdb_id.lower()}.pdb")

    print(f"[INFO] Iniciando adquisición de: {pdb_id}...")
    
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(ruta_archivo, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                
        print(f"[OK] Archivo guardado en: {ruta_archivo}")
        return ruta_archivo

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Fallo en la adquisición: {e}")
        return None

if __name__ == "__main__":
    # Permite pasar el ID desde la línea de comandos
    if len(sys.argv) > 1:
        id_estructura = sys.argv[1]
    else:
        id_estructura = input("Introduce el ID PDB (ej. 1BNA): ")
        
    descargar_pdb(id_estructura)