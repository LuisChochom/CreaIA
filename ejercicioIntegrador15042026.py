from abc import ABC, abstractmethod

# --- Definición de Clases ---

class VehiculoTerrestre(ABC):
    @abstractmethod
    def conducir_ruedas(self):
        pass

class VehiculoAcuatico(ABC):
    @abstractmethod
    def encender_helices(self):
        pass

class VehiculoAnfibio(VehiculoTerrestre, VehiculoAcuatico):
    def conducir_ruedas(self):
        print("Activando tracción 4x4 en terreno rocoso.")
    
    def encender_helices(self):
        print("Retrayendo ruedas y activando propulsión acuática.")

class AutoComun(VehiculoTerrestre):
    def conducir_ruedas(self):
        print("El auto avanza por la carretera.")

class Lancha(VehiculoAcuatico):
    def encender_helices(self):
        print("La lancha navega por el río.")

# --- Ejecución con Try / Except ---

try:
    # Creamos los objetos
    mi_auto = AutoComun()
    mi_lancha = Lancha()
    mi_anfibio = VehiculoAnfibio()

    # Recorremos la ruta terrestre
    print("--- Ruta Terrestre ---")
    ruta_terrestre = [mi_auto, mi_anfibio]
    for v in ruta_terrestre:
        v.conducir_ruedas()

    # Recorremos la ruta acuática
    print("\n--- Ruta Acuática ---")
    ruta_acuatica = [mi_lancha, mi_anfibio]
    for v in ruta_acuatica:
        v.encender_helices()

except:
    # Si algo falla (como olvidar un método), se ejecuta esto
    print("Algo salió mal al crear o usar los vehículos.")