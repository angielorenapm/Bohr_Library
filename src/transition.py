import math

class ModeloBohrTransiciones:
    """
    Clase para calcular la diferencia de energía, frecuencia y longitud de onda
    de un fotón asociado a una transición electrónica en un átomo hidrogenoide.
    """
    # Constantes Físicas
    CONSTANTE_RYDBERG_EV = 13.6057  # E_0 en eV
    CTE_PLANK = 6.626e-34           # h en J*s
    VELOCIDAD_LUZ = 2.998e8         # c en m/s
    EV_TO_JOULES = 1.602e-19        # Factor de conversión 1 eV a Joules

    def obtener_entero_positivo(self, mensaje):
        """
        Solicita y valida un número entero positivo para Z, n_inicial o n_final.
        """
        while True:
            try:
                valor = int(input(mensaje))
                if valor < 1:
                    print("Error: El valor debe ser un entero positivo (>= 1).")
                else:
                    return valor
            except ValueError:
                print("Error: Entrada no válida. Por favor, ingrese un número entero.")

    def calcular_energia_nivel(self, Z, n):
        """
        Calcula la energía de un electrón en el nivel 'n' en eV.
        E_n = - (E_0 * Z^2) / n^2
        """
        if n == 0:
            return float('inf') # Debería ser evitado por la validación
        
        energia_n_ev = -1 * (self.CONSTANTE_RYDBERG_EV * (Z**2)) / (n**2)
        return energia_n_ev

    def calcular_transicion(self):
        """
        Gestiona la entrada de datos, calcula la diferencia de energía, frecuencia y longitud de onda.
        """
        print("\n--- Transición Electrónica (Modelo de Bohr) ---")
        
        # Obtener entradas con validación
        Z = self.obtener_entero_positivo("Ingrese el Número Atómico (Z): ")
        n_inicial = self.obtener_entero_positivo("Ingrese el Nivel Inicial (n_i): ")
        n_final = self.obtener_entero_positivo("Ingrese el Nivel Final (n_f): ")
        
        if n_inicial == n_final:
            return "Error: Los niveles inicial y final deben ser diferentes para una transición."

        # 1. CÁLCULO DE ENERGÍAS
        E_inicial_eV = self.calcular_energia_nivel(Z, n_inicial)
        E_final_eV = self.calcular_energia_nivel(Z, n_final)

        # 2. DIFERENCIA DE ENERGÍA
        # Delta E en eV (usado para saber si es emisión o absorción)
        delta_E_eV = E_final_eV - E_inicial_eV
        
        # Delta E en Joules (necesario para las fórmulas de Planck)
        delta_E_J = abs(delta_E_eV) * self.EV_TO_JOULES
        
        # 3. FRECUENCIA DEL FOTÓN
        # |Delta E| = h * nu  => nu = |Delta E| / h
        frecuencia_nu = delta_E_J / self.CTE_PLANK
        
        # 4. LONGITUD DE ONDA
        # c = lambda * nu => lambda = c / nu
        longitud_onda_m = self.VELOCIDAD_LUZ / frecuencia_nu
        
        # Determine si es emisión o absorción
        tipo_transicion = "EMITIDO" if delta_E_eV < 0 else "ABSORBIDO"
        proceso = "Emisión" if delta_E_eV < 0 else "Absorción"

        # --- Presentación de Resultados ---
        print("\n--- RESULTADOS DE LA TRANSICIÓN ---")
        print(f"Tipo de Proceso: {proceso}")
        print(f"Número Atómico (Z): {Z}")
        print(f"Transición: n={n_inicial} -> n={n_final}")
        
        print("\n--- Datos de Energía ---")
        print(f"E_inicial: {E_inicial_eV:.4f} eV")
        print(f"E_final: {E_final_eV:.4f} eV")
        print(f"Diferencia de Energía (ΔE): {abs(delta_E_eV):.4f} eV")
        print(f"Energía del Fotón: {delta_E_J:.4e} J")
        
        print("\n--- Datos del Fotón ---")
        print(f"El fotón fue {tipo_transicion}.")
        print(f"Frecuencia (ν): {frecuencia_nu:.4e} Hz")
        print(f"Longitud de Onda (λ): {longitud_onda_m:.4e} m")

        return f"Cálculo completado para la transición n={n_inicial} a n={n_final} del átomo con Z={Z}."


    def menu(self):
        """
        Muestra el menú principal y gestiona las opciones de cálculo.
        """
        while True:
            print("\n--- Menú Modelo de Bohr (Transiciones) ---")
            print("1. Calcular Transición de Energía, Frecuencia y Longitud de Onda")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                resultado = self.calcular_transicion()
                print(resultado)
            elif opcion == "0":
                print("Saliendo del menú de Modelo de Bohr.")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

# --- Ejemplo de uso ---
if __name__ == "__main__":
    transiciones_calculator = ModeloBohrTransiciones()
    transiciones_calculator.menu()
