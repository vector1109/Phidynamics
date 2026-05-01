# Phidynamics

**Local-first computational biophysics for reproducible structural analysis**
*Biomolecular structure treated as geometry under torsion — not as a black box.*

Phidynamics is a local-first computational biophysics framework for structural analysis of biomolecules using explicit geometric observables derived from torsion, curvature, and constrained phase dynamics.

It replaces opaque inference with deterministic, inspectable, and reproducible geometric descriptors that can be computed directly from real structural data on consumer hardware.

---

## What Phidynamics does

Phidynamics provides a reproducible structural analysis pipeline for biomolecular systems.

Given a structural input (`PDB` or `XYZ`), it can:

* analyze structural geometry
* compute normalized geometric signatures
* compare structural similarity
* classify structural regimes
* simulate constrained phase dynamics
* generate integrated structural diagnostics

Phidynamics is designed for:

* local execution
* deterministic outputs
* geometric interpretability
* structural comparison
* falsifiable low-cost experimentation

It does **not** require:

* GPU clusters
* molecular dynamics supercomputing
* proprietary infrastructure
* machine learning training pipelines

All outputs are generated locally, deterministically, and reproducibly from structural input.

---

## Quick Start

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/vector1109/Phidynamics.git
cd Phidynamics

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux / macOS

pip install -r requirements.txt
```

---

## Core Commands

### Analyze a structure

```bash
python main.py analizar 1BNA
python main.py analizar input/xyz/grafeno.xyz
```

Computes structural signature, topology, and geometric classification.

---

### Compare two structures

```bash
python main.py comparar input/xyz/grafeno.xyz input/xyz/tetraedro.xyz
```

Computes normalized structural similarity between two geometries.

---

### Search structural neighbors

```bash
python main.py buscar input/xyz/grafeno.xyz input/xyz/
```

Finds nearest structural neighbors in a local dataset.

---

### Run phase dynamics

```bash
python main.py fase
```

Executes constrained torsion-phase evolution and reports absorption dynamics.

---

### Run phase sweep

```bash
python main.py fase-sweep
python main.py fase-stats
python main.py fase-report
```

Runs multi-condition phase sweeps, summarizes stability, and reports dynamic regimes.

---

### Run integrated diagnosis

```bash
python main.py diagnosticar input/xyz/grafeno.xyz
```

Runs the full MVP pipeline:

**structure → geometry → phase → absorption → regime → diagnosis**

---

## Example Output

Phidynamics produces explicit, inspectable observables such as:

* structural class
* dimensionality
* coordination
* cyclicity
* normalized torsion absorption
* phase regime
* integrated structural diagnosis

Example diagnostic output:

```text
File:           input/xyz/grafeno.xyz
Signature:      graphene / hexagonal lattice
Dimensionality: 2D
Absorption:     1.935
Regime:         stable
Memory:         indeterminate
Conclusion:     graphene / hexagonal lattice | stable regime | indeterminate memory
```

---

## Scientific Scope

Phidynamics is an experimental computational biophysics framework.

It is intended for:

* structural modeling
* geometric comparison
* computational hypothesis generation
* exploratory biophysical analysis

It is **not** intended for:

* medical diagnosis
* clinical interpretation
* treatment decisions
* biomedical intervention

Current outputs should be interpreted as **geometric observables**, not direct biological causality.

---

## Core Hypothesis

Phidynamics investigates whether normalized torsion-derived geometry can act as a stable observable for distinguishing structural regimes in biological systems.

Instead of modeling biomolecular organization as a purely statistical or inferential problem, Phidynamics treats structure as constrained geometric response under torsional organization.

Its working hypothesis is that normalized geometric observables can reproducibly separate:

* globular protein regimes
* canonical B-DNA regimes
* relaxed low-tension conformations

This is currently treated as a computational biophysics hypothesis, not an established physical law.

---

## Current Result

The strongest current result is not the claim of a new physical law.

The strongest result is that Phidynamics produces a normalized torsion-derived observable that appears to separate structural regimes reproducibly under local execution.

Observed Δ ranges currently show stable separation between:

| Structural Class        | Observed Δ Range |
| ----------------------- | ---------------: |
| Globular proteins       |     ~0.04 – 0.09 |
| Relaxed DNA-like states |            ~0.04 |
| Canonical B-DNA         |     ~0.17 – 0.18 |

This suggests Δ may function as a reproducible descriptor of structural regime under normalized geometric comparison.

That is the current central result of the framework.

---

## Why it matters

Phidynamics does not attempt to compete with molecular dynamics by brute force.

Its contribution is different:

it proposes that low-cost geometric observables may capture biologically relevant structural regimes without requiring high-complexity simulation stacks.

This makes the framework:

* inspectable
* reproducible
* portable
* computationally cheap
* scientifically falsifiable

---

## Project Status

Current status: **MVP stable baseline**

Phidynamics is now:

* versioned
* reproducible
* locally executable
* structurally testable
* baseline-stable

Current baseline commit:

```text
4ce778a
MVP estable: pipeline estructural + fase + diagnostico integrado
```

---

## Roadmap

* Procrustes alignment baseline
* RMSD vs Δ benchmark
* batch multi-PDB CLI
* JSON export pipeline
* unit tests for Δ stability
* CI reproducibility validation
* A-DNA / Z-DNA extension
* harmonic parameter sweeps
* publishable validation report
* statistical significance analysis

---

## License

Phidynamics uses a dual-license model.

### Code

All executable source code is released under:

**GNU Affero General Public License v3.0 (AGPL-3.0)**

This includes:

* source code
* execution scripts
* validation
* visualization
* reproducible tooling

---

### Theory and conceptual framework

Conceptual formulation, theoretical interpretation, and methodological framework are released under:

**CC BY-NC-ND 4.0**

This includes:

* theoretical framing
* conceptual methodology
* nomenclature
* explanatory formalism
* interpretive framework

The code is open for audit and extension.
The conceptual framework is open for study and citation.

---

## Citation

```bibtex
@software{phidynamics2026,
  author = {Farias, Fabian Dario},
  title = {Phidynamics: Local-first Computational Biophysics for Reproducible Structural Analysis},
  year = {2026},
  url = {https://github.com/vector1109/Phidynamics}
}
```

---

## Author

**Fabián Darío Farías**
fabianista / Vector Torsion SRL

* [fabiandariofarias@gmail.com](mailto:fabiandariofarias@gmail.com)
* [vector.torsion.srl@gmail.com](mailto:vector.torsion.srl@gmail.com)

Phidynamics does not claim consensus.
It claims reproducibility.
