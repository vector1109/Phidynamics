# Phidynamics

**Sovereign Biophysics Framework**  
*Motor de Bio-Geometría Fractal basado en Tiempo OAM y Torsión Riemann-Cartan*

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Development Status](https://img.shields.io/badge/Status-Active_Development-orange.svg)]()

> Framework de física computacional para análisis estructural biológico.  
> Sustituye modelos "caja negra" con leyes de torsión fractal (Ley de Torsión Bimodal).  
> Diseñado para auditoría, precisión física y ejecución local.

![Phidynamics - Sovereign Biophysics Framework](https://github.com/fabianista/Phidynamics/blob/main/imagenes/ADN_torsional.png)

---

## Visión

La vida no se organiza mediante ecuaciones lineales. Se autoorganiza a través de **curvatura esférica**, **tiempo como Momento Angular Orbital (OAM)** y **torsión fractal** modulada por la proporción áurea (Φ).

Phidynamics es un marco experimental de **biofísica computacional** que modela esta geometría viva mediante geometría de Riemann-Cartan y detecta estados funcionales de moléculas biológicas (especialmente ADN) a través de su **firma torsional**.

---

## Principios Fundamentales

- **Universo Esférico**: Curvatura positiva en lugar de modelo plano
- **Tiempo OAM**: El tiempo como momento angular orbital, no como línea recta
- **Torsión Fractal**: Campo de información modulado por Φ (proporción áurea)
- **Bifurcación Estructural**: Capacidad de distinguir estados del ADN mediante una constante física invariante (**Λ_D ≈ 0.1759**)

---

## Características Principales

- Motor Riemann-Cartan con **métrica helicoidal** dependiente de tiempo OAM
- Generador de crecimiento fractal áureo con armónicos múltiples
- Soporte para **doble hebra** con fase asimétrica (modelado de surcos mayor/menor)
- Validación sistemática contra estructuras reales del **Protein Data Bank (PDB)**
- Cálculo de **firma torsional (Delta)** como indicador de estado estructural
- Clasificación bimodal del ADN:
  - **Estado Relajado** (Δ ≈ 0.04) → Banda Alfa (~7.83 Hz)
  - **Estado Activo/Tensionado** (Δ ≈ 0.176) → Banda Gamma (~34.4 Hz)
- Predicción de **accesibilidad genómica** basada en tensión torsional
- Visualización 3D del crecimiento helicoidal y espiral torsional

---

## Resultados Científicos Destacados

- **Proteínas**: Excelente ajuste torsional (RMSD normalizado ~0.04–0.09)
- **B-DNA** (1BNA, 1D65): Firma torsional consistente **Δ ≈ 0.1759 – 0.1761**
- **ADN Relajado** (1D02): Coincidencia casi perfecta **Δ ≈ 0.0400**
- La constante **0.1759** se interpreta como **Λ_D** (Lambda de ADN): invariante de acoplamiento torsional entre el campo fractal y la estructura discreta del ADN.

---

## Estructura del Proyecto

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
Bashgit clone https://github.com/fabianista/Phidynamics.git
cd Phidynamics

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

Estado del Proyecto
Proyecto en desarrollo activo
Se han realizado múltiples verificaciones de datos contra estructuras reales del PDB (proteínas y ADN). El framework ha demostrado consistencia en la detección de estados estructurales y funcionales del ADN mediante su firma torsional.
Próximos pasos:

Optimización automática de armónicos
Simulación dinámica de tensión torsional
Mejora de visualizaciones interactivas
Extensión a más conformaciones de ADN (A-DNA, Z-DNA, etc.)


📄 Licencia
Este proyecto se distribuye principalmente bajo la GNU Affero General Public License v3.0 (AGPL-3.0).
Ver el archivo LICENSE para el texto completo.
Licencia Dual / Comercial
Además de la licencia AGPL-3.0, se ofrece licencia dual comercial.
Esto permite el uso del software en proyectos propietarios o entornos cerrados sin estar obligado a cumplir con las condiciones copyleft de la AGPL (como compartir modificaciones del código fuente).
Si estás interesado en una licencia comercial, por favor contacta al autor para discutir los términos.


Autor: fabiandariofarias@gmail.com
       vector.torsion.srl@gmail.com
"El espacio-tiempo biológico ya no es lineal."
