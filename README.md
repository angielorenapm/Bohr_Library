# BohrAJJP

## Description

BohrAJJP is an educational Python project that demonstrates the Bohr model for hydrogen‑like (hydrogenoid) atoms. The code provides three focused utilities: an energy-level calculator for a single electron, a transition calculator that returns ΔE, photon energy, frequency and wavelength, and a visualizer that draws energy levels and classical circular orbits and writes them to image files. The implementation is intentionally simple and readable so it can be used as a teaching aid or a base for further extensions.

## Current state

The repository contains a working `src/` package with three main modules that can each be executed as standalone scripts. `energy.py` offers an interactive menu for computing the energy of an electron in level `n` using the Bohr formula. `transition.py` computes initial and final level energies, the energy difference, the photon frequency and wavelength for a given transition. `plot_orbits.py` generates and saves two PNG images (`energy_levels_plot.png` and `orbits_plot.png`) with a simple attempt to open them in the system default image viewer; in headless environments the viewer call fails gracefully and the image files remain saved.

Basic input validation (positive integers for `Z` and `n`) and simple exception handling are implemented. Physical constants are included directly in the modules with sufficient precision for pedagogical purposes.

## Objectives

The primary goal of this project is pedagogical: to show how the Bohr model predicts bound-state energies and spectral lines and to provide a visual intuition for how energy and orbital radius scale with principal quantum number `n` and nuclear charge `Z`. 

## Installation

A Python 3.8+ environment is recommended. Create and activate a virtual environment and install the plotting dependency:

```
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```
The package has been uploaded to PiPy;:
The instalation process is as simple as this:
```
pip install BohrAJJP
```

## Usage and examples

Pending...
---
Authors: Angie Lorena Pineda, Juan Sebastián Acuña, Jose Luis Zamora
