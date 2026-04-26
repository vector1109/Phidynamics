#  Phidynamics

**Sovereign Biophysics Framework**  
*Motor de Bio-Geometría Fractal basado en Tiempo OAM y Torsión Riemann-Cartan*

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Development Status](https://img.shields.io/badge/Status-Active_Development-orange.svg)]()

> **Phidynamics** propone una transición desde la física lineal hacia una descripción **helicoidal, torsional y fractal** de los sistemas biológicos.

---

##  Visión

La vida no se organiza mediante ecuaciones lineales. Se auto-organiza a través de **curvatura esférica**, **tiempo como Momento Angular Orbital (OAM)** y **torsión fractal** modulada por la proporción áurea (Φ).

Phidynamics es un framework experimental de **biofísica computacional** que modela esta geometría viva mediante geometría de Riemann-Cartan y detecta estados funcionales de moléculas biológicas (especialmente ADN) a través de su **firma torsional**.

<img width="1408" height="768" alt="ADN" src="https://github.com/user-attachments/assets/3c18277e-8387-4b01-aacc-66ef1d9a94ea" />


---

##  Principios Fundamentales

- **Universo Esférico**: Curvatura positiva en lugar de modelo plano
- **Tiempo OAM**: El tiempo como momento angular orbital, no como línea recta
- **Torsión Fractal**: Campo de información modulado por Φ (proporción áurea)
- **Bifurcación Estructural**: Capacidad de distinguir estados del ADN mediante una constante física invariante (Λ_D ≈ 0.1759)

---

##  Características Principales

- Motor Riemann-Cartan con **métrica helicoidal** dependiente de tiempo OAM
- Generador de crecimiento fractal áureo con armónicos múltiples
- Soporte para **doble hebra** con fase asimétrica (modelado de surcos mayor/menor)
- Validación sistemática contra estructuras reales del **Protein Data Bank (PDB)**
- Cálculo de **firma torsional (Delta)** como indicador de estado estructural
- Clasificación bimodal del ADN:
  - **Estado Relajado** (Δ ≈ 0.04) → Banda Alpha (~7.83 Hz)
  - **Estado Activo/Tensionado** (Δ ≈ 0.176) → Banda Gamma (~34.4 Hz)
- Predicción de **accesibilidad genómica** basada en tensión torsional
- Visualización 3D del crecimiento helicoidal y espiral torsional

---

##  Resultados Científicos Destacados

- **Proteínas**: Excelente ajuste torsional (RMSD normalizado ~0.04–0.09)
- **B-DNA (1BNA, 1D65)**: Firma torsional consistente **Δ ≈ 0.1759–0.1761**
- **ADN Relajado (1D02)**: Coincidencia casi perfecta **Δ ≈ 0.0400**
- La constante **0.1759** se interpreta como **Λ_D** (Lambda de ADN): invariante de acoplamiento torsional entre el campo fractal y la estructura discreta del ADN.

---

##  Estructura del Proyecto

```bash
phidynamics/
├── core/
│   ├── constants.py          # Φ, constantes biogemétricas y físicas
│   └── geometry.py           # RiemannCartanEngine
├── bio/
│   ├── fractal.py            # CrecimientoFractal (armónicos + dual strand)
│   ├── visualizer.py         # Visualización 3D
│   └── resonance.py          # Acoplamiento con resonancias ambientales
├── main.py
├── analizar_pdb.py           # Análisis completo de estructuras PDB
├── calculadora_accesibilidad.py
├── validate_with_pdb.py
└── ...

 Instalación
Bashgit clone https://github.com/tu-usuario/phidynamics.git
cd phidynamics

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux / macOS

pip install torch numpy matplotlib biopython scipy
 Uso Rápido
Bash# Simulación básica con visualización
python main.py

# Análisis completo de una estructura PDB
python analizar_pdb.py 1BNA
Ejemplo de salida:
textDelta (Torsión): 0.1759
Frecuencia Sintonía: 34.43 Hz
Estado Espectral: Gamma (Procesamiento/Alta Energía)
Accesibilidad Genómica: 100.00%

⚠️ Estado del Proyecto
Proyecto en desarrollo activo
Se han realizado múltiples verificaciones de datos contra estructuras reales del PDB (proteínas y ADN). El framework ha demostrado ser capaz de detectar de forma consistente estados estructurales y funcionales del ADN mediante su firma torsional.
Próximos pasos principales:

Optimización automática de armónicos
Simulación dinámica de tensión torsional
Mejora de visualizaciones interactivas
Extensión a más conformaciones de ADN (A-DNA, Z-DNA, etc.)


 Licencia
Este proyecto se distribuye bajo la GNU Affero General Public License v3.0 (AGPL-3.0).
Licencia dual: El código fuente es libre según AGPL-3.0. Para uso comercial o integración en productos propietarios, contactar al autor para licencias comerciales específicas.
Ver el archivo LICENSE para más detalles.


Autor: Fabian Dario Farias

"El espacio-tiempo biológico ya no es lineal."
