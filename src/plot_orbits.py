# scripts/plot_orbits.py

import matplotlib.pyplot as plt
import os
import sys
import subprocess

# Import the real classes from the other files
from energy import ModeloBohr
from radius import RadiusCalculator

# NEW: Function to open a file with the system's default application
def open_file(file_path):
    """
    Opens a file using the system's default command.
    Compatible with Windows, macOS, and Linux.
    """
    try:
        if sys.platform == "win32":
            os.startfile(os.path.realpath(file_path))
        elif sys.platform == "darwin":  # macOS
            subprocess.run(["open", file_path], check=True)
        else:  # Linux and other Unix systems
            subprocess.run(["xdg-open", file_path], check=True)
    except Exception as e:
        print(f"\nWARNING: Could not open '{file_path}' automatically.")
        print(f"Reason: {e}")
        print("This is normal if you are not in a graphical environment.")

class AtomVisualizer:
    def __init__(self, z: int = 1):
        self.z = z
        names = {1: "Hydrogen", 2: "Helium+", 3: "Lithium++"}
        self.element_name = names.get(self.z, f"Atom (Z={self.z})")

    def plot_energy_levels(self, energies: list, transitions: list = None, filename: str = None):
        fig, ax = plt.subplots(figsize=(6, 8))
        for i, energy in enumerate(energies):
            n = i + 1
            ax.axhline(y=energy, color='gray', linestyle='--')
            ax.text(1.05, energy, f'n={n}, E={energy:.2f} eV', va='center')
        if transitions:
            for start_n, end_n in transitions:
                if start_n <= len(energies) and end_n <= len(energies):
                    start_energy = energies[start_n - 1]
                    end_energy = energies[end_n - 1]
                    ax.annotate("", xy=(0.5, end_energy), xytext=(0.5, start_energy),
                                arrowprops=dict(arrowstyle="->", color="purple", lw=1.5))
        ax.set_title(f'Energy Levels for {self.element_name}')
        ax.set_ylabel('Energy (eV)')
        ax.set_xlim(0, 2)
        ax.set_xticks([])
        plt.tight_layout()
        if filename:
            plt.savefig(filename, dpi=300)
            print(f" ✅ Energy levels plot saved to '{filename}'")

    def plot_orbits(self, radii: list, filename: str = None):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.plot(0, 0, 'o', markersize=10, color='red', label='Nucleus')

        for i, r in enumerate(radii):
            n = i + 1
            circle = plt.Circle((0, 0), r, fill=False, linestyle='--')
            ax.add_patch(circle)

            # --- NEW: show explicit radius value ---
            ax.text(r, 0, f' n={n}\n r={r:.2f} Å', va='bottom', ha='left',
                    fontsize=9, bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

        max_radius = max(radii) * 1.1 if radii else 1
        ax.set_xlim(-max_radius, max_radius)
        ax.set_ylim(-max_radius, max_radius)
        ax.set_aspect('equal', adjustable='box')
        ax.set_title(f'Electron Orbits for {self.element_name}')
        ax.set_xlabel('Distance (Å)')
        ax.set_ylabel('Distance (Å)')
        ax.grid(True, linestyle=':')
        plt.tight_layout()
        if filename:
            plt.savefig(filename, dpi=300)
            print(f" ✅ Orbits plot saved to '{filename}'")


# --- Main Execution Block ---
if __name__ == "__main__":
    print("\n--- Bohr Atom Graphical Visualizer ---")
    
    energy_calculator = ModeloBohr()
    radius_calculator = RadiusCalculator()
    
    try:
        Z = energy_calculator.obtener_entero_positivo("Enter the Atomic Number (Z) to plot: ")
        max_n = energy_calculator.obtener_entero_positivo(f"Enter the maximum number of levels to plot for Z={Z}: ")

        radii = [radius_calculator.calculate(Z, n) for n in range(1, max_n + 1)]
        energies = [-1 * (energy_calculator.CONSTANTE_ENERGIA_RYDBERG_EV * Z**2) / (n**2) for n in range(1, max_n + 1)]
        transitions = [(n, 1) for n in range(2, max_n + 1)]

        script_dir = os.path.dirname(__file__)
        output_dir = os.path.join(script_dir, '..', 'src')
        os.makedirs(output_dir, exist_ok=True)
        
        filename_orbits = os.path.join(output_dir, "orbits_plot.png")
        filename_energy = os.path.join(output_dir, "energy_levels_plot.png")
        
        visualizer = AtomVisualizer(z=Z)
        visualizer.plot_energy_levels(energies, transitions, filename=filename_energy)
        visualizer.plot_orbits(radii, filename=filename_orbits)

        # NEW: Try to open the images after creation
        print("\nAttempting to open the generated image files...")
        open_file(filename_energy)
        open_file(filename_orbits)

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

    print(f"\nVisualization program finished.")
    input("\nPress Enter to exit...")
