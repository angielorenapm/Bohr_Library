import math
import matplotlib.pyplot as plt

# Definimos la clase BohrAtom
class BohrAtom:
    def __init__(self, Z=1):
        # Constantes físicas
        self.m_e = 9.11e-31  # Masa del electrón en kg
        self.e = 1.602e-19  # Carga del electrón en C
        self.h = 6.626e-34  # Constante de Planck en J·s
        self.epsilon_0 = 8.854e-12  # Permitividad en vacío en F/m
        self.Z = Z  # Carga nuclear (para el hidrógeno Z = 1)

import subprocess
import os

# Carpeta donde están los scripts
SCRIPTS_DIR = "scripts"  # Cambia esto si tus archivos están en otra ruta

def run_script(script_name):
    """Ejecuta un script .py ubicado en la carpeta SCRIPTS_DIR"""
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    if os.path.exists(script_path):
        subprocess.run(["python", script_path])
    else:
        print(f"Error: No se encontró el archivo {script_name} en {SCRIPTS_DIR}.")

def main():
    while True:
        print("\nSeleccione una opción:")
        print("1. Calcular niveles de energía (energy.py)")
        print("2. Calcular radios de órbita (radius.py)")
        print("3. Calcular transiciones electrónicas (transition.py)")
        print("4. Graficar niveles y órbitas (plot_orbits.py)")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción deseada (1-5): ")

        if opcion == '1':
            run_script("energy.py")

        elif opcion == '2':
            run_script("radius.py")

        elif opcion == '3':
            run_script("transition.py")

        elif opcion == '4':
            run_script("plot_orbits.py")

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
