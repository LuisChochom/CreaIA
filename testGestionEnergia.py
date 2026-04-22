from abc import ABC, abstractmethod

class EnergiaInvalidaError(Exception):
    pass

class Nucleo:
    def __init__(self, id_unico):
        self.id = id_unico

class EntidadBase(ABC):
    def __init__ (self, energia, id_entidad):
        if energia < 0:
            raise EnergiaInvalidaError("La energia inicial no puede ser negativa")
        self.energia = energia
        self.nucleo = Nucleo(id_entidad)
    
    @abstractmethod
    def alimentarse(self, cantidad=10):
        pass
    
    def __add__(self, otra_entidad):
        return self.energia + otra_entidad.energia
    
class Sintetizador(EntidadBase):
    def alimentarse(self, cantidad=10):
        self.energia += cantidad
        print(f"Sintetizador {self.nucleo.id} absorbio luz. Energia actual {self.energia}")
    
class Consumidor(EntidadBase):
    def alimentarse(self, cantidad=10):
        self.energia += cantidad
        print(f"Consumidor {self.nucleo.id} consumio recursos. Energia actual {self.energia}")

class Hibrido(Sintetizador, Consumidor):
    def alimentarse(self, cantidad=10):
        self.energia += (cantidad * 2)
        print(f"Hibrido {self.nucleo.id} uso ambos metodos. Energia actual {self.energia}")

def iniciar_ciclo_vital(lista_entidades):
    print("\n--- Iniciando Ciclo Vital ---")
    for entidad in lista_entidades:
        entidad.alimentarse()

def ejecutar_laboratorio():
    colonia = []
    print("¡Bienvenido al Laboratorio Digital!")
    
    while True:
        print("\n1. Crear Sintetizador")
        print(f"2. Crear Híbrido")
        print("3. Iniciar ciclo vital y ver energía total")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "4":
            break
        
        try:
            if opcion == "1" or opcion == "2":
                try:
                    puntos = int(input("Ingrese nivel de energía inicial: "))
                    id_personalizado = input("Ingrese el ID único: ")
                    
                    if opcion == "1":
                        nueva_entidad = Sintetizador(puntos, id_personalizado)
                        tipo = "Sintetizador"
                    else:
                        nueva_entidad = Hibrido(puntos, id_personalizado)
                        tipo = "Híbrido"
                    
                    colonia.append(nueva_entidad)
                    print(f"Éxito: {tipo} '{id_personalizado}' añadido a la colonia.")
                    
                except ValueError:
                    print("Error: Debes ingresar un número entero para la energía.")
                except EnergiaInvalidaError as e:
                    print(f"Error de sistema: {e}")
            
            elif opcion == "3":
                if not colonia:
                    print("No hay entidades en la colonia.")
                    continue
                
                iniciar_ciclo_vital(colonia)
                
                if len(colonia) >= 2:
                    suma_energia = colonia[0] + colonia[1]
                    print(f"\nSuma de energía de las dos primeras entidades: {suma_energia}")
            
            else:
                print("Opción no válida, intente de nuevo.")
                
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    ejecutar_laboratorio()