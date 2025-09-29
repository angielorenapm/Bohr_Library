import math

class ModeloBohr:
    """
    Clase para calcular la energía de un electrón en el nivel 'n' de un átomo hidrogenoide
    usando el modelo de Bohr.
    """
    # Constante de energía de Rydberg, E_0 = 13.6 eV
    # E_n = - (E_0 * Z^2) / n^2
    CONSTANTE_ENERGIA_RYDBERG_EV = 13.6

    def menu(self):
        """
        Muestra el menú principal y gestiona las opciones de cálculo.
        """
        while True:
            print("\n--- Menú Modelo de Bohr (Átomo Hidrogenoide) ---")
            print("1. Calcular Energía de Electrón (E_n) en eV")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                resultado = self.calcular_energia_bohr()
                # Verifica si el resultado es un error antes de imprimir
                if isinstance(resultado, str):
                    print(resultado) # Imprime el mensaje de error
                else:
                    # Formatea el resultado para mostrarlo con 4 decimales
                    print(f"\nResultado: La energía del electrón en el nivel 'n' es: {resultado:.4f} eV")
            elif opcion == "0":
                print("Saliendo del menú de Modelo de Bohr.")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

    def obtener_entero_positivo(self, mensaje):
        """
        Solicita y valida un número entero positivo para Z o n.
        """
        while True:
            try:
                valor = int(input(mensaje))
                if valor < 1:
                    print("Error: El valor debe ser un entero positivo (mayor o igual a 1).")
                else:
                    return valor
            except ValueError:
                print("Error: Entrada no válida. Por favor, ingrese un número entero.")

    def calcular_energia_bohr(self):
        """
        Calcula la energía de un electrón en el n-ésimo nivel de energía
        de un átomo hidrogenoide usando la fórmula de Bohr.
        E_n = - (E_0 * Z^2) / n^2
        """
        print("\n--- Cálculo de Energía de Electrón (E_n) ---")
        
        # Z: Número atómico (carga nuclear). Ej: H=1, He+=2, Li2+=3
        Z = self.obtener_entero_positivo("Ingrese el Número Atómico (Z): ")

        # n: Nivel principal de energía (n=1, 2, 3, ...)
        n = self.obtener_entero_positivo("Ingrese el Nivel de Energía (n): ")
        
        # Fórmula de Bohr para la energía en eV
        # El signo negativo indica que es un estado ligado (se requiere energía para liberarlo).
        try:
            energia_n = -1 * (self.CONSTANTE_ENERGIA_RYDBERG_EV * (Z**2)) / (n**2)
            return energia_n
        except ZeroDivisionError:
            # Esto no debería ocurrir con la validación de 'n', pero es una buena práctica.
            return "Error: División por cero (El nivel de energía 'n' no puede ser cero)."

# --- Ejemplo de uso ---
if __name__ == "__main__":
    bohr_calculator = ModeloBohr()
    bohr_calculator.menu()
