# Bohr Library

## Description

Bohr Library is a compact educational Python package that implements the Bohr model for hydrogen and hydrogen-like atoms. It provides simple, well-documented tools to compute electron energy levels (eV), orbital radii (Å), and properties of electronic transitions (ΔE, photon frequency and wavelength). The package also includes utilities to generate visualizations (PNG) of energy levels and electron orbits for teaching and demonstration purposes.

## Current state

Version: **0.1.0**.

The repository contains readable, pedagogical scripts under `src/`: `energy.py` (energy-level calculator), `radius.py` (Bohr radii), `transition.py` (transition energies and photon properties), and `plot_orbits.py` (visualizer that saves PNG files). A simple `main.py` dispatches those scripts via an interactive menu. Several functions are already usable programmatically (for example `RadiusCalculator.calculate(...)` and `ModeloBohrTransiciones.calcular_energia_nivel(...)`).

Note: the radius module uses `scipy.constants` for physical constants. If you plan to install the package from PyPI or use it as a library, ensure `scipy` is available.

# Objectives

Short-term: keep the code readable and educational, provide a stable programmatic API (non-interactive wrappers), and publish the package on PyPI so users can install it with a single command.

# Usage (primary installation method: PyPI)

The recommended installation path is via PyPI. Install the package with pip and import the library from your Python scripts. This README provides a single, minimal example showing the PyPI installation method and one short usage snippet.

Install from PyPI:

```bash
pip install bohr-library
```

Single example after installing from PyPI (minimal, non-interactive):

```python
# simple_example.py
# After installing via: pip install bohr-library
from src.transition import ModeloBohrTransiciones
from src.radius import RadiusCalculator


Z = 1 # Hydrogen
n = 1 # ground state


trans = ModeloBohrTransiciones()
energy_ev = trans.calcular_energia_nivel(Z, n)


radius_calc = RadiusCalculator()
radius_A = radius_calc.calculate(Z, n)


print(f"Hydrogen n={n} energy: {energy_ev:.4f} eV")
print(f"Hydrogen n={n} Bohr radius: {radius_A:.4f} Å")
```

# Minimal API reference

`RadiusCalculator.calculate(Z, n)` — returns the Bohr radius for a hydrogen-like ion in Angstroms (Å).

`ModeloBohrTransiciones.calcular_energia_nivel(Z, n)` — returns the energy of level `n` in electronvolts (eV).

`AtomVisualizer.plot_energy_levels(energies, transitions=None, filename=None)` — saves an energy-level plot to `filename` if provided.

`AtomVisualizer.plot_orbits(radii, filename=None)` — saves an orbit plot to `filename` if provided.

# Requirements and compatibility

* Python: >= 3.8
* Required packages: `numpy`, `matplotlib`, and `scipy` (for `scipy.constants`) — install these before or while installing the package:

```bash
pip install numpy matplotlib scipy
```

# Known issues and recommendations

* Many scripts use interactive `input()` calls. For automation and testing, call the non-interactive methods directly (e.g., `calculate`, `calcular_energia_nivel`) or add small wrapper functions that accept arguments instead of reading from STDIN.
* Update `pyproject.toml` to include `scipy` in `dependencies` before publishing to PyPI.

# Contributing & License

The project metadata indicates an MIT license. Contributions are welcome via cloning the repository, creating a branch, and opening a pull request. Suggested improvements: add unit tests, provide non-interactive API wrappers, tidy packaging so installed import paths are consistent, and add documentation pages or notebooks.

---
