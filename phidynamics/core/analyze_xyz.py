from phidynamics.core.xyz_parser import cargar_xyz
from phidynamics.core.distance_matrix import matriz_distancias
from phidynamics.core.structure_signature import clasificar_estructura
from phidynamics.core.bond_detector import detectar_enlaces
from phidynamics.core.signature_store import guardar_firma


def analizar_material(ruta_archivo):
    """
    Pipeline físico para materiales .xyz
    """
    print(f"\n[INFO] Analizando material estructural: {ruta_archivo}")

    atomos = cargar_xyz(ruta_archivo)
    distancias = matriz_distancias(atomos)
    enlaces, coordinacion = detectar_enlaces(atomos, distancias)
    firma = clasificar_estructura(atomos, enlaces, coordinacion)

    print("\n" + "=" * 60)
    print("FIRMA ESTRUCTURAL DEL MATERIAL")
    print("=" * 60)
    print(f"Átomos:               {firma['atomos']}")
    print(f"Enlaces detectados:   {firma['enlaces']}")
    print(f"Coordinación media:   {firma['coordinacion_media']}")
    print(f"Dimensionalidad:      {firma['dimensionalidad']}")
    print(f"Ciclicidad:           {firma['ciclicidad']}")
    print(f"Clasificación:        {firma['tipo']}")
    print("=" * 60 + "\n")

    guardar_firma(ruta_archivo, firma)
    return firma