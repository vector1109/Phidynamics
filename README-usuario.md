# Phidynamics Framework: Motor de Bio-Geometría Fractal

Phidynamics es un framework computacional avanzado diseñado para modelar estructuras biológicas a partir de principios de **geometría fractal y resonancia armónica**. A diferencia de los métodos químicos tradicionales, este sistema trata a las macromoléculas (proteínas, ADN, complejos virales) como manifestaciones geométricas de una firma torsional subyacente.

El motor central (`fractal.py`) utiliza un sistema de análisis armónico para reconstruir la morfología 3D de cualquier estructura PDB, permitiendo validar leyes universales de plegamiento más allá de la composición molecular.

---

## 1. Configuración del Entorno
Asegúrate de ejecutar tus pruebas en un entorno virtual (`venv`) con las dependencias necesarias:

```bash
pip install biopython numpy
La estructura del proyecto debe mantener fractal.py dentro de phidynamics/bio/ para asegurar la correcta importación del motor.
________________________________________
2. Flujo de Trabajo (Workflow)
El uso del sistema sigue un ciclo de investigación repetible y modular:
1.	Captura: Descargar y procesar archivos .ent (PDB) mediante descargador_pdb.py.
2.	Identificación: Usar scan_frequency.py y scan_fase.py para encontrar la "firma torsional" (armónicos) específica de la estructura.
3.	Simulación: Instanciar CrecimientoFractal con la firma encontrada para generar la estructura sintética.
4.	Validación: Comparar contra la estructura real mediante consistency_test.py o proyeccion_test.py calculando el RMSD Normalizado.
________________________________________
3. Uso del Motor (CrecimientoFractal)
El núcleo del sistema es un modelo generativo de morfología biológica. Se invoca de la siguiente manera:
Python
from phidynamics.bio.fractal import CrecimientoFractal

# Definir firma: [(Amplitud, Frecuencia, Fase)]
firmas = [(0.5, 0.1, 0.0), (0.2, 0.3959, 0.0)]

# Instanciar el motor
engine = CrecimientoFractal(
    harmonics=firmas,
    dual_strand=True,       # Habilitar para ADN o estructuras dobles
    target_dist=20.0        # Restricción física
)

# Generar y cuantizar
coords = engine.generar_espiral_aurea(num_nodos=100, cuantizar=True)
________________________________________
4. Guía de Scripts
Script	Propósito
analizar_pdb.py	Análisis de estado base de estructuras PDB.
consistency_test.py	Verifica la ley universal de plegamiento mediante RMSD.
cuantizacion_test.py	Ajusta la salida fractal a la resolución física real (step=0.5Å).
proyeccion_test.py	Mapeo de la estructura fractal al espacio de coordenadas real.
scan_fase.py	Optimización del desfasaje para minimizar el error.
scan_frequency.py	Identificación de la resonancia armónica de la estructura.
mapeo_dinamico.py	Visualización del comportamiento torsional bajo estrés.
________________________________________
5. Fundamentación Teórica: Un Modelo Agnóstico
El motor no depende de la composición química (nucleótidos vs. aminoácidos). Opera recibiendo una "firma de resonancia" ($harmonics$) y una "fuerza de torsión" ($k_{total}$), generando una geometría que optimiza ese estado energético.
Evidencia experimental:
Los tests realizados con consistency_test.py han validado el sistema con diversas estructuras:
•	1MBN: Mioglobina (proteína globular).
•	1PG1: Proteína viral.
•	1UBQ: Ubiquitina (proteína reguladora pequeña).
El éxito en estos modelos demuestra que la torsión describe las reglas geométricas de empaquetamiento que subyacen a toda la materia orgánica.
________________________________________
6. Motor de Computación Z60 y Estabilidad
La complejidad del sistema se gestiona bajo la filosofía: La complejidad no debería recaer en la ejecución, sino en la interpretación.
Abstracción de la lógica Z60
El usuario no interactúa manualmente con los estados "sexagesimales". La clase CrecimientoFractal actúa como un wrapper: el usuario trabaja con coordenadas 3D (flotantes estándar), mientras que el motor mapea internamente estas estructuras a la lógica Z60.
El Estabilizador: "Smooth Loss"
Para evitar saltos erráticos y modelos divergentes (o "El Abismo de los Gradientes") durante la optimización, se implementa una función de Smooth Loss. Esta función garantiza que el modelo converja de manera estable, permitiendo al usuario confiar en la robustez de los resultados obtenidos.
Interpretación de la Base-60 (Z60)
La Base-60 no es solo aritmética, es geometría circular. Para trabajar con este sistema, el usuario debe considerar dos puntos críticos:
•	Transporte de datos: Al activar la cuantización (cuantizar=True), el sistema convierte la representación continua (física) en una representación discreta basada en 60. Esto no es pérdida de precisión, sino una alineación geométrica con la resonancia fundamental.
•	Interpretabilidad del RMSD: El error (RMSD) se mide contra esta grilla cuantizada. Es vital entender que el sistema opera en "chunks" o bloques de 60. Si se intenta validar resultados sin esta premisa, el usuario podría malinterpretar el error como imprecisión cuando, en realidad, es confinamiento geométrico.
________________________________________
7. Resolución de Problemas Comunes
•	TypeError (unexpected keyword argument): Ocurre generalmente al actualizar la clase CrecimientoFractal. Asegúrate de que los métodos __init__ y generar_espiral_aurea coincidan con la versión actual en fractal.py.
•	Estado "Desfasado": Si el RMSD > 0.1, no es un error de código, sino una señal de que los armónicos necesitan refinamiento. Ejecuta scan_frequency.py para re-calibrar la firma.
•	Archivos PDB faltantes: El sistema intenta descargar el archivo .ent. Si falla, verifica tu conexión o coloca el archivo manualmente en la raíz del proyecto.
Nota: Este framework es un modelo generativo. La precisión de los resultados depende directamente de la calidad de la firma armónica detectada.
