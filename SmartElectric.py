from abc import ABC, abstractmethod
import json

# ==========================================================
# A. EL MODELO (modelo.py - Lógica de Negocio)
# ==========================================================

class FuenteEnergia(ABC):
    def __init__(self, id_generador, capacidad_maxima):
        self._id_generador = id_generador
        self._capacidad_maxima = capacidad_maxima
        self._produccion_actual = 0.0

    @property
    def id_generador(self):
        return self._id_generador

    @property
    def capacidad_maxima(self):
        return self._capacidad_maxima

    @property
    def produccion_actual(self):
        return self._produccion_actual

    @produccion_actual.setter
    def produccion_actual(self, valor):
        if valor <= self._capacidad_maxima:
            self._produccion_actual = valor
        else:
            self._produccion_actual = self._capacidad_maxima

    @abstractmethod
    def generar(self, datos_clima):
        pass

class PanelSolar(FuenteEnergia):
    def generar(self, datos_clima):
        # Solo genera si el clima es "Soleado"
        if datos_clima.get("clima") == "Soleado":
            self.produccion_actual = self.capacidad_maxima
        else:
            self.produccion_actual = 0.0


class TurbinaEolica(FuenteEnergia):
    def generar(self, datos_clima):
        # Genera basado en la velocidad del viento (ejemplo simple)
        viento = datos_clima.get("viento", 0)
        if viento > 10:
            self.produccion_actual = self.capacidad_maxima
        else:
            self.produccion_actual = viento * 5 


class GeneradorDiesel(FuenteEnergia):
    def __init__(self, id_generador, capacidad_maxima, combustible):
        super().__init__(id_generador, capacidad_maxima)
        self._combustible = combustible

    @property
    def combustible(self):
        return self._combustible

    def generar(self, datos_clima):
        # Consume combustible cada vez que genera
        if self._combustible >= 10:
            self._combustible -= 10
            self.produccion_actual = self.capacidad_maxima
        else:
            self.produccion_actual = 0.0

# ==========================================================
# B. LA FÁBRICA (fabrica.py - Creación de Objetos)
# ==========================================================

class FabricaEnergia:
    # Diccionario de mapeo para registro dinámico
    _mapeo = {
        "solar": PanelSolar,
        "eolica": TurbinaEolica,
        "diesel": GeneradorDiesel
    }

    @staticmethod
    def crear_fuente(datos):
        tipo = datos.get("tipo")
        clase = FabricaEnergia._mapeo.get(tipo)
        
        if not clase:
            return None
        
        # Si es diesel, necesita el parámetro extra de combustible
        if tipo == "diesel":
            return clase(datos["id_generador"], datos["capacidad_maxima"], datos["combustible"])
        
        return clase(datos["id_generador"], datos["capacidad_maxima"])

# ==========================================================
# C. LA VISTA (vista.py - Interfaz de Usuario)
# ==========================================================

class InterfazRed:
    def mostrar_tablero(self, fuentes):
        print("\n" + "="*40)
        print("   ESTADO DE LA RED ELÉCTRICA SMART")
        print("="*40)
        for f in fuentes:
            print(f"ID: {f.id_generador} | Tipo: {type(f).__name__}")
            print(f"Producción Actual: {f.produccion_actual} kW / Máx: {f.capacidad_maxima} kW")
            if hasattr(f, 'combustible'):
                print(f"Combustible restante: {f.combustible} L")
            print("-" * 20)

    def solicitar_datos_entorno(self):
        print("\n--- Configuración de condiciones ---")
        clima = input("Ingrese el clima (Soleado/Nublado): ")
        viento = float(input("Ingrese velocidad del viento (km/h): "))
        return {"clima": clima, "viento": viento}

    def mostrar_error(self, mensaje):
        print(f"\n*** ERROR: {mensaje} ***\n")

# ==========================================================
# D. EL CONTROLADOR (controlador.py - Orquestación)
# ==========================================================

class ControladorRed:
    def __init__(self):
        self.vista = InterfazRed()
        self.fuentes = []

    def cargar_datos_iniciales(self):
        # Datos "quemados" simulando el JSON
        contenido_json = """
        [
            {"tipo": "solar", "id_generador": "SOL-01", "capacidad_maxima": 100.0},
            {"tipo": "eolica", "id_generador": "EOL-99", "capacidad_maxima": 250.0},
            {"tipo": "diesel", "id_generador": "DSL-05", "capacidad_maxima": 500.0, "combustible": 1000.0}
        ]
        """
        datos = json.loads(contenido_json)
        for item in datos:
            objeto = FabricaEnergia.crear_fuente(item)
            if objeto:
                self.fuentes.append(objeto)

    def ejecutar(self):
        self.cargar_datos_iniciales()
        
        # Ciclo simple de control
        try:
            # 1. Leer datos de la Vista
            entorno = self.vista.solicitar_datos_entorno()
            
            # 2. Pasar datos al Modelo y procesar
            for fuente in self.fuentes:
                fuente.generar(entorno)
            
            # 3. Enviar resultados de vuelta a la Vista
            self.vista.mostrar_tablero(self.fuentes)
            
        except Exception as e:
            print(f"Error durante la ejecución: {e}")

# ==========================================================
# INICIO DEL PROGRAMA
# ==========================================================
if __name__ == "__main__":
    app = ControladorRed()
    app.ejecutar()