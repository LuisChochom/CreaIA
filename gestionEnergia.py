from abc import ABC, abstractmethod

# --- 1. Manejo de Errores (Excepción Personalizada) ---
class EnergiaInvalidaError(Exception):
    """Excepción para cuando la energía no cumple los requisitos."""
    pass

# --- 2. Composición ---
class Nucleo:
    def __init__(self, id_unico):
        # El ID ahora es dinámico (letras y números)
        self.id = id_unico

# --- 3. Clase Abstracta EntidadBase ---
class EntidadBase(ABC):
    def __init__(self, energia, id_entidad):
        # Uso de RAISE para validar la energía
        if energia < 0:
            raise EnergiaInvalidaError("La energía inicial no puede ser negativa.")
        
        self.energia = energia
        # Composición: La Entidad TIENE un Nucleo
        self.nucleo = Nucleo(id_entidad)

    @abstractmethod
    def alimentarse(self, cantidad=10):
        """Método abstracto: cada subclase debe definir cómo se alimenta."""
        pass

    # --- 4. Sobrecarga de Operadores ---
    def __add__(self, otra_entidad):
        """Permite sumar la energía de dos objetos usando el símbolo '+'"""
        return self.energia + otra_entidad.energia

# --- 5. Herencia y Herencia Múltiple ---
class Sintetizador(EntidadBase):
    def alimentarse(self, cantidad=10):
        self.energia += cantidad
        print(f"-> Sintetizador [{self.nucleo.id}] absorbió luz. Energía actual: {self.energia}")

class Consumidor(EntidadBase):
    def alimentarse(self, cantidad=10):
        self.energia += cantidad
        print(f"-> Consumidor [{self.nucleo.id}] consumió recursos. Energía actual: {self.energia}")

class Hibrido(Sintetizador, Consumidor):
    """Hereda de Sintetizador y Consumidor (Herencia Múltiple)"""
    def alimentarse(self, cantidad=10):
        self.energia += cantidad
        print(f"-> Híbrido [{self.nucleo.id}] usó alimentación mixta. Energía actual: {self.energia}")

# --- 6. Polimorfismo ---
def iniciar_ciclo_vital(lista_entidades):
    print("\n--- INICIANDO CICLO VITAL (POLIMORFISMO) ---")
    for entidad in lista_entidades:
        # No importa el tipo de entidad, todas saben alimentarse()
        entidad.alimentarse()

# --- Interfaz de Usuario y Simulación ---
def ejecutar_laboratorio():
    colonia = []
    print("=== SISTEMA DE GESTIÓN BIOLÓGICA DIGITAL ===")
    
    while True:
        print("\nMenú de opciones:")
        print("1. Crear Sintetizador")
        print("2. Crear Híbrido")
        print("3. Ejecutar Ciclo Vital")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "4":
            print("Cerrando laboratorio...")
            break
        
        if opcion in ["1", "2"]:
            try:
                # Primero solicitamos la energía
                entrada_energia = input("Ingrese el nivel de energía inicial: ")
                puntos = int(entrada_energia) # Puede lanzar ValueError
                
                # Luego solicitamos el ID (acepta letras y números)
                id_personalizado = input("Ingrese el ID único: ")
                
                # Intentamos instanciar (aquí puede saltar EnergiaInvalidaError)
                if opcion == "1":
                    nueva = Sintetizador(puntos, id_personalizado)
                    tipo = "Sintetizador"
                else:
                    nueva = Hibrido(puntos, id_personalizado)
                    tipo = "Híbrido"
                
                colonia.append(nueva)
                print(f"Éxito: {tipo} '{id_personalizado}' añadido a la colonia.")

            except ValueError:
                print("Error: La energía debe ser un número entero.")
            except EnergiaInvalidaError as e:
                # Capturamos el raise que lanzamos en el __init__
                print(f"Error de validación: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")
        
        elif opcion == "3":
            if not colonia:
                print("La colonia está vacía.")
            else:
                iniciar_ciclo_vital(colonia)
                
                # Ejemplo de sobrecarga de suma (si hay al menos 2)
                if len(colonia) >= 2:
                    suma = colonia[0] + colonia[1]
                    print(f"\n[INFO] Energía combinada de '{colonia[0].nucleo.id}' y '{colonia[1].nucleo.id}': {suma}")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    ejecutar_laboratorio()