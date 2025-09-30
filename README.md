# Bohr Library

## Description

Bohr Library is an educational Python project that demonstrates the Bohr model for hydrogen‑like (hydrogenoid) atoms. The code provides three focused utilities: an energy-level calculator for a single electron, a transition calculator that returns ΔE, photon energy, frequency and wavelength, and a visualizer that draws energy levels and classical circular orbits and writes them to image files. The implementation is intentionally simple and readable so it can be used as a teaching aid or a base for further extensions.

## Current state

The repository contains a working `src/` package with three main modules that can each be executed as standalone scripts. `energy.py` offers an interactive menu for computing the energy of an electron in level `n` using the Bohr formula. `transition.py` computes initial and final level energies, the energy difference, the photon frequency and wavelength for a given transition. `plot_orbits.py` generates and saves two PNG images (`energy_levels_plot.png` and `orbits_plot.png`) with a simple attempt to open them in the system default image viewer; in headless environments the viewer call fails gracefully and the image files remain saved.

Basic input validation (positive integers for `Z` and `n`) and simple exception handling are implemented. Physical constants are included directly in the modules with sufficient precision for pedagogical purposes.

## Objectives

The primary goal of this project is pedagogical: to show how the Bohr model predicts bound-state energies and spectral lines and to provide a visual intuition for how energy and orbital radius scale with principal quantum number `n` and nuclear charge `Z`. Secondary goals for future development include exporting computed data (CSV/JSON), centralizing physical constants in a dedicated module, converting interactive scripts into importable functions for testing and reuse, and optionally building a small GUI or web front-end.

## Usage and examples

### Quick example — how the package is called

Short examples of how users typically invoke the project after installing or cloning it. The project is published on PyPI (package name used in the example below comes from the project metadata).

A Python 3.8+ environment is recommended. You can use a virtual environment, or install directly via pip from PyPI.

Create and activate a virtual environment (optional):

```
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

1. Install from PyPI (example):

```bash
pip install bohr-library
```

2. Run the unified menu (from the repository root):

```bash
python main.py
```

3. Run the package as a module (works if the package provides `__main__.py` or is installed as an importable package):

```bash
python -m bohr_library
```

4. Import and use programmatically (some classes provide non-interactive methods; others expose interactive `menu()`):

```py
from bohr_library import ModeloBohr, ModeloBohrTransiciones, RadiusCalculator, AtomVisualizer

# Interactive menu (will prompt):
ModeloBohr().menu()

# Programmatic radius calculation (non-interactive):
rc = RadiusCalculator()
r = rc.calculate(1, 1)  # returns radius in Å
print(f"Bohr radius (Z=1, n=1): {r:.4f} Å")
```

Notes: if you installed the package and a console script was registered (e.g. `bohr-library` or `bohr_library`), you may be able to run it directly from the shell; otherwise use `python -m` or call `main.py` from the repository root. The PDF in the repository contains the build and PyPI upload logs and confirms the package metadata and the test/release process. A typical interaction for the energy calculator for hydrogen ground state looks like this:

```
Select an option:
1. Calcular niveles de energía (energy.py)
2. Calcular radios de órbita (radius.py)
3. Calcular transiciones electrónicas (transition.py)
4. Graficar niveles y órbitas (plot_orbits.py)
5. Salir

# choose 1
Enter the Atomic Number (Z): 1
Enter the Energy Level (n): 1

Resultado: La energía del electrón en el nivel 'n' es: -13.6000 eV
```

If you prefer to run a single tool directly, run the corresponding script inside `src/`. For example, the radius calculator can be executed with `python src/radius.py`; entering `Z = 1` and `n = 1` will print the Bohr radius for hydrogen (approximately `0.5290 Å`):

```
--- Orbit Radius Calculation ---
Enter the Atomic Number (Z): 1
Enter the Energy Level (n): 1

RESULT:
The orbit radius n=1 for Z=1 is: 0.5290 Å
```

The transition calculator provides ΔE (in eV), the photon energy in joules, the photon frequency and the wavelength. Running `python src/transition.py` and entering `Z = 1`, `n_i = 2`, `n_f = 1` yields the Lyman-α example (values shown approximate):

```
Tipo de Proceso: Emisión
Número Atómico (Z): 1
Transición: n=2 -> n=1

E_inicial: -3.4000 eV
E_final: -13.6000 eV
Diferencia de Energía (ΔE): 10.2000 eV
Energía del Fotón: 1.6340e-18 J
Frecuencia (ν): 2.4660e+15 Hz
Longitud de Onda (λ): 1.2160e-07 m
```

The plotting tool `src/plot_orbits.py` generates two PNG files with energy-level lines and classical circular orbits. Run `python src/plot_orbits.py`, supply the requested `Z` and maximum `n`, and the script will save images into the repository `src/` folder by default (files named `energy_levels_plot.png` and `orbits_plot.png`). The script attempts to open the images with the system default image viewer; in headless environments this will fail with a warning but the image files remain saved.

When running the package as a user (for example after installing via pip), the same scripts and the top-level launcher exist in the installed package layout; however, `main.py` uses subprocess calls relative to the repository layout, so if you install the package and want the launcher behavior it is recommended to run `python -m` on a package-provided module or keep running `main.py` from the project root. In short: for local development run `python main.py` from the project root; to call a single tool directly run `python src/<script>.py`.

Examples summary: use `python main.py` to open the unified menu, `python src/energy.py` to compute a single energy level, `python src/radius.py` to compute an orbital radius (returns Angstroms), `python src/transition.py` to compute photon properties for a transition, and `python src/plot_orbits.py` to save `energy_levels_plot.png` and `orbits_plot.png` into the `src/` folder.

Constants are currently defined inside the modules for clarity. If you plan to extend the project, create a `src/constants.py` and import values from there (optionally using `scipy.constants` for higher precision). The interactive scripts rely on `input()`; to make the code easier to test and reuse, refactor the computation logic into functions or methods that accept parameters rather than reading from `stdin`.

Authors: Angie Lorena Pineda, Sebastián Acuña, Jose Luis Zamora, Pablo Patiño Bonilla

---
