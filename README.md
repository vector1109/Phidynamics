# Phidynamics

### Marco Soberano de Biofísica Computacional

**Biofísica computacional derivada de torsión para análisis estructural reproducible**

> *“La estructura biológica no se trata aquí como una caja negra, sino como geometría bajo torsión.”*

---

## Descripción general

Phidynamics es un marco experimental de biofísica computacional orientado al análisis estructural de biomoléculas mediante torsión, curvatura y organización geométrica.

Basado en un formalismo geométrico inspirado en Riemann–Cartan, el sistema reemplaza inferencia opaca tipo “caja negra” por observables geométricos explícitos, auditables y reproducibles, aplicables al estudio estructural de proteínas, ADN y sistemas helicoidales complejos.

El objetivo del proyecto es explorar si ciertos regímenes estructurales biológicos pueden distinguirse de forma estable mediante observables geométricos normalizados derivados de torsión.

Phidynamics fue diseñado para:

* ejecución local,
* interpretabilidad física,
* comparación estructural reproducible,
* y experimentación falsable de bajo costo sobre hardware de consumo.

Phidynamics no requiere:

* clústeres GPU,
* supercómputo de dinámica molecular,
* infraestructura propietaria,
* ni pipelines de entrenamiento de machine learning.

Corre localmente, de forma determinista, y produce observables geométricos repetibles a partir de datos estructurales reales.

---

## Hipótesis central

Phidynamics investiga si una geometría normalizada derivada de torsión puede actuar como observable estable para distinguir regímenes estructurales en sistemas biológicos.

En lugar de tratar la organización biomolecular como un problema puramente estadístico o inferencial, el sistema modela la estructura como respuesta geométrica restringida bajo organización torsional.

La hipótesis de trabajo es que un observable geométrico normalizado (`Δ`) puede separar de forma reproducible:

* regímenes proteicos globulares,
* regímenes de ADN B canónico,
* y conformaciones relajadas o de baja tensión.

Actualmente esto se trata como una **hipótesis de biofísica computacional**, no como una ley física establecida.

---

## Qué es Phidynamics

Phidynamics es:

* un marco de biofísica computacional,
* un motor de análisis estructural derivado de torsión,
* una tubería reproducible de descriptores geométricos,
* una alternativa basada en hipótesis frente a inferencia biológica opaca,
* una herramienta científica local-first.

---

## Qué no es Phidynamics

Phidynamics **no** es:

* un reemplazo de dinámica molecular,
* un predictor de machine learning,
* un sistema clínico o diagnóstico,
* un dispositivo biomédico,
* un instrumento médico validado,
* un sustituto de biología experimental húmeda (wet-lab).

Es un marco experimental de análisis estructural, modelado falsable y generación de hipótesis.

---

## Alcance científico y limitaciones

Phidynamics es un sistema de investigación experimental.

Está orientado a:

* modelado estructural,
* comparación geométrica,
* generación de hipótesis,
* y biofísica computacional exploratoria.

No está destinado a:

* diagnóstico,
* tratamiento,
* interpretación clínica,
* ni toma de decisiones biomédicas.

Las salidas actuales deben interpretarse como **observables geométricos**, no como causalidad biológica directa.

En particular:

* `Δ` es actualmente un descriptor estructural,
* no una constante física universal demostrada,
* y no una variable causal biológica validada.

Las interpretaciones sobre resonancia, estado espectral o accesibilidad genómica son actualmente **hipótesis de trabajo** y deben tratarse como exploratorias hasta validación independiente.

---

## Resultado principal (estado actual)

El resultado más sólido del proyecto no es la afirmación de una nueva ley física.

El resultado más sólido es que Phidynamics produce un **observable normalizado derivado de torsión (`Δ`) que parece separar regímenes estructurales de forma reproducible** bajo ejecución local.

En las pruebas actuales, `Δ` muestra separación estable entre:

| Clase estructural         | Rango observado de `Δ` |
| ------------------------- | ---------------------: |
| Proteínas globulares      |           ~0.04 – 0.09 |
| Estados tipo ADN relajado |                  ~0.04 |
| ADN B canónico            |           ~0.17 – 0.18 |

Esto sugiere que `Δ` puede funcionar como descriptor reproducible de régimen estructural bajo comparación geométrica normalizada.

Este es, actualmente, el resultado central del marco.

---

## Por qué importa

Phidynamics no intenta competir con dinámica molecular por fuerza bruta.

Su aporte es otro:

propone que observables geométricos de bajo costo pueden capturar regímenes estructurales biológicamente relevantes sin requerir pilas de simulación de alta complejidad.

La implicancia práctica es directa:

un descriptor estructural falsable y reproducible puede calcularse localmente sobre hardware de consumo sin depender de sistemas opacos de inferencia.

Eso vuelve al marco:

* inspeccionable,
* reproducible,
* portable,
* y científicamente falsable.

---

## Características principales

* motor geométrico inspirado en Riemann–Cartan,
* métrica helicoidal modulada por OAM,
* observable estructural derivado de torsión (`Δ`),
* generador de crecimiento fractal / helicoidal,
* modelado de ADN de doble hebra,
* comparación estructural normalizada,
* flujo reproducible basado en PDB,
* ejecución local determinista,
* visualización geométrica 3D,
* análisis compatible con CPU de bajo costo.

---

## Instalación

```bash
git clone https://github.com/fabianista/Phidynamics.git
cd Phidynamics

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux / macOS

pip install torch numpy matplotlib biopython scipy
```

---

## Inicio rápido

### Ejecutar simulación geométrica local

```bash
python main.py
```

### Analizar una estructura PDB real

```bash
python analizar_pdb.py 1BNA
```

Salida esperada (ejemplo):

```text
Delta (Torsión): 0.1759
Frecuencia de Resonancia: 34.43 Hz
Estado Espectral: Gamma (Alta Energía / Procesamiento)
Accesibilidad Genómica: 100.00%
```

---

## Reproducibilidad

Todas las comparaciones estructurales reportadas en este repositorio están diseñadas para reproducirse en hardware de consumo estándar.

No se requiere clúster GPU, infraestructura propietaria ni entrenamiento de modelos.

Scripts principales de reproducibilidad:

```bash
python validate_with_pdb.py
python consistency_test.py
python universal_test.py
python verificacion_constante.py
python calculadora_accesibilidad.py
```

Estos scripts reproducen el flujo de comparación estructural utilizado para derivar las observaciones actuales sobre regímenes `Δ`.

---

## Resumen de validación

La validación actual sugiere que el observable normalizado derivado de torsión (`Δ`) se comporta como un descriptor estable de régimen bajo normalización geométrica.

Comportamiento observado:

* los modelos iniciales en coordenadas crudas divergen,
* la comparación geométrica normalizada estabiliza,
* las proteínas agrupan en un régimen de `Δ` bajo,
* el ADN B canónico ocupa una banda estable superior de `Δ`,
* los estados relajados tipo ADN colapsan hacia el régimen adyacente a proteínas.

Esto **no** establece todavía una ley física universal.

Sí establece una separación computacional reproducible que justifica investigación adicional.

---

## Hoja de ruta

* [ ] Agregar baseline de alineamiento Procrustes
* [ ] Agregar benchmark RMSD / `Δ`
* [ ] Agregar CLI batch multi-PDB
* [ ] Agregar exportación JSON de resultados
* [ ] Agregar tests unitarios para estabilidad de `Δ`
* [ ] Agregar validación reproducible en CI
* [ ] Extender clases conformacionales de ADN (A-DNA / Z-DNA)
* [ ] Agregar barridos de parámetros armónicos
* [ ] Agregar informe de validación publicable
* [ ] Agregar análisis de significancia estadística

---

## Licencia (Esquema Dual)

Phidynamics se distribuye bajo un esquema de **licencia dual**, separando explícitamente la capa de implementación del marco conceptual.

### 1. Código fuente (Open Source)

Todo el código contenido en:

* `src/`
* `tests/`
* `scripts/`
* utilidades de ejecución
* visualización
* validación reproducible

se distribuye bajo:

**GNU Affero General Public License v3.0 (AGPL-3.0)**

Esto permite:

* uso,
* auditoría,
* modificación,
* redistribución,
* despliegue local o remoto,

con la obligación de mantener apertura del código derivado y de cualquier servicio expuesto sobre él.

Esto protege al sistema contra apropiación cerrada de su implementación.

### 2. Marco teórico y formulación conceptual

Todo el contenido contenido en:

* `docs/`
* formulación teórica,
* hipótesis,
* taxonomía conceptual,
* documentación metodológica,
* nomenclatura original,
* interpretación estructural,
* formalismo explicativo,

se distribuye bajo:

**CC BY-NC-ND 4.0**
(Atribución – No Comercial – Sin Derivadas)

Esto permite:

* lectura,
* cita,
* discusión,
* difusión académica,

pero **no permite**:

* uso comercial del marco conceptual,
* reformulación derivada como teoría propia,
* relicenciamiento conceptual,
* redistribución modificada,
* apropiación metodológica sin autorización.

### ¿Por qué licencia dual?

Porque este repositorio contiene dos capas distintas:

1. una implementación computacional auditable,
2. una formulación conceptual original.

Ambas conviven, pero no cumplen la misma función.

El código puede auditarse y extenderse.
La formulación puede estudiarse y citarse.
La apropiación conceptual no es libre.

### Resumen práctico

| Componente                 | Licencia        | Uso permitido                                  |
| -------------------------- | --------------- | ---------------------------------------------- |
| Código fuente              | AGPL-3.0        | uso, modificación, despliegue con reciprocidad |
| Scripts y validación       | AGPL-3.0        | reproducible, auditable, extensible            |
| Documentación metodológica | CC BY-NC-ND 4.0 | lectura, cita, difusión                        |
| Marco conceptual           | CC BY-NC-ND 4.0 | no comercial, no derivado                      |

### Licenciamiento comercial

Si desea:

* integrar el marco en software propietario,
* relicenciar componentes,
* usar el formalismo en productos cerrados,
* incorporar la metodología en entornos comerciales,
* o negociar excepciones de copyleft,

debe solicitar licencia comercial o autorización expresa al autor.

---

## Cita

Si utiliza Phidynamics en investigación, cite:

```bibtex
@software{phidynamics2026,
  author = {Farias, Fabian Dario},
  title = {Phidynamics: Marco Soberano de Biofísica Computacional},
  year = {2026},
  url = {https://github.com/fabianista/Phidynamics}
}
```

---

## Autor

**Fabián Darío Farías**
fabianista / Vector Torsion SRL

* [fabiandariofarias@gmail.com](mailto:fabiandariofarias@gmail.com)
* [vector.torsion.srl@gmail.com](mailto:vector.torsion.srl@gmail.com)

---

> *Phidynamics no reclama consenso. Reclama reproducibilidad.*
