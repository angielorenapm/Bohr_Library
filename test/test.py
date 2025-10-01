#!/usr/bin/env python3
"""
test.py - simple smoke test for Bohr Library

Usage:
    python test.py

This script expects the package to be installed as `bohr-library` (importable as `bohr_library.*`).
If you prefer to run it against the repository source (no install), uncomment the fallback import block below.
"""

# Primary (PyPI-style) imports:
from bohr_library.transition import ModeloBohrTransiciones
from bohr_library.radius import RadiusCalculator

# --- OPTIONAL: fallback to local src/ if you didn't install the package ---
# Uncomment these lines and comment the above imports if you want to run
# directly from the repository (project root must be current working dir).
#
# try:
#     from bohr_library.transition import ModeloBohrTransiciones
#     from bohr_library.radius import RadiusCalculator
# except Exception:
#     # Fallback to local repo layout
#     from src.transition import ModeloBohrTransiciones
#     from src.radius import RadiusCalculator

def main():
    Z = 1  # Hydrogen
    n = 1  # ground state

    trans = ModeloBohrTransiciones()
    energy_ev = trans.calcular_energia_nivel(Z, n)

    radius_calc = RadiusCalculator()
    radius_A = radius_calc.calculate(Z, n)

    print(f"Hydrogen n={n} energy: {energy_ev:.4f} eV")
    print(f"Hydrogen n={n} Bohr radius: {radius_A:.4f} Å")

if __name__ == "__main__":
    main()
