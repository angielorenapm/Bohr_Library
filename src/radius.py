# scripts/radius.py

import scipy.constants as const

class RadiusCalculator:
    """
    Calculates the orbit radii for a hydrogen-like atom.
    """
    def __init__(self):
        # Physical constants
        self.m_e = const.m_e
        self.e = const.e
        self.epsilon_0 = const.epsilon_0
        self.hbar = const.hbar
        self._bohr_radius_m = (4 * const.pi * self.epsilon_0 * self.hbar**2) / (self.m_e * self.e**2)

    def get_positive_integer(self, message):
        """Requests and validates a positive integer."""
        while True:
            try:
                value = int(input(message))
                if value < 1:
                    print("Error: The value must be a positive integer (>= 1).")
                else:
                    return value
            except ValueError:
                print("Error: Invalid input. Please enter an integer.")

    def calculate(self, Z, n):
        """Calculates the orbit radius for a given 'n' level and Z."""
        if n < 1 or Z < 1:
            raise ValueError("n and Z must be positive integers.")
        
        radius_in_meters = self._bohr_radius_m * (n**2 / Z)
        return radius_in_meters * 1e10 # Convert to Angstroms

    def menu(self):
        """Displays the menu for radius calculation."""
        while True:
            print("\n--- Orbit Radius Calculation Menu ---")
            print("1. Calculate Orbit Radius")
            print("0. Exit")
            option = input("Select an option: ")

            if option == "1":
                print("\n--- Orbit Radius Calculation ---")
                Z = self.get_positive_integer("Enter the Atomic Number (Z): ")
                n = self.get_positive_integer("Enter the Energy Level (n): ")
                
                radius = self.calculate(Z, n)
                
                print("\n" + "="*25)
                print(f"  RESULT:")
                print(f"  The orbit radius n={n} for Z={Z} is: {radius:.4f} Å")
                print("="*25)

            elif option == "0":
                print("Exiting the radius menu.")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    radius_calculator = RadiusCalculator()
    radius_calculator.menu()