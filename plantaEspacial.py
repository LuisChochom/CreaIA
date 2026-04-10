#EJERCICIO #1 Dron Vigilancia
class DronVigilancia:
    def __init__(self, nombre, modelo):
        # El constructor recibe nombre y modelo [cite: 5]
        self.nombre = nombre
        self.modelo = modelo
        # Atributos iniciales por defecto [cite: 6]
        self.bateria = 100
        self.estado_vuelo = "En Tierra"

    def despegar(self):
        # Solo despega si tiene al menos 25% de batería [cite: 7]
        if self.bateria >= 25:
            self.estado_vuelo = "En Vuelo"
            print("¡Despegue exitoso! El dron ahora está en el aire.")
        else:
            print(f"[ERROR: Batería insuficiente ({self.bateria}%). Necesita 25%].")

    def patrullar(self):
        # Solo patrulla si está en el aire
        if self.estado_vuelo == "En Vuelo":
            self.bateria -= 30 
            print(f"Patrullaje completado. Consumo: 30%. Batería restante: {self.bateria}%.")
            
            # Aterrizaje automático si la batería es crítica [cite: 11]
            if self.bateria < 10:
                print("¡ALERTA! Batería crítica. Aterrizando automáticamente...")
                self.estado_vuelo = "En Tierra"
        else:
            print("[ERROR: El dron no puede patrullar si aún está en tierra].") 

    def recargar(self):
        # Solo recarga si está en tierra [cite: 12]
        if self.estado_vuelo == "En Tierra":
            self.bateria = 100 
            print("Recarga completa. Batería al 100%.")
        else:
            print("[ERROR: No se puede recargar en pleno vuelo. ¡Peligro!].")

# --- Programa Principal ---
print(">>> INICIANDO SISTEMA SKYWATCH <<<")
nom = input("Ingrese nombre del dron: ") 
mod = input("Ingrese modelo del dron: ") 

mi_dron = DronVigilancia(nom, mod)

opcion = ""
while opcion != "4": 
    print(f"\nESTADO ACTUAL: {mi_dron.nombre} [{mi_dron.modelo}]")
    print(f"Batería: {mi_dron.bateria}% | Estado: {mi_dron.estado_vuelo}") 
    
    print("\n¿Qué acción desea realizar?")
    print("1. Despegar")
    print("2. Patrullar")
    print("3. Recargar")
    print("4. Salir (Apagar Sistema)")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mi_dron.despegar()
    elif opcion == "2":
        mi_dron.patrullar()
    elif opcion == "3":
        mi_dron.recargar()
    elif opcion == "4":
        print("Apagando sistema...")
    else:
        print("Opción no válida.")


#EJERCICIO #2 Planta Espacial
class PlantaEspacial:
    def __init__(self, nombre, especie):
        # Recibe nombre y especie 
        self.nombre = nombre
        self.especie = especie
        # Valores iniciales 
        self.hidratacion = 100
        self.salud = 100
        self.estado = "Saludable"

    def regar(self):
        # Una planta marchita no puede ser regada
        if self.estado == "Marchita":
            print(f"[ERROR: {self.nombre} está marchita y no puede recibir agua].")
            return

        self.hidratacion += 15 
        # No puede superar el 100% 
        if self.hidratacion > 100:
            self.hidratacion = 100
        print(f"Suministrando agua... Hidratación actual: {self.hidratacion}%.")

    def pasar_dia(self):
        if self.estado == "Marchita":
            print("El tiempo pasa, pero la planta ya no tiene vida.")
            return

        self.hidratacion -= 20 
        print(f"Ha pasado un día en Marte. La hidratación bajó a {self.hidratacion}%.")

        # Lógica de estrés hídrico 
        if self.hidratacion < 30:
            self.salud -= 40
            print(f"¡ALERTA! Hidratación crítica. La salud de {self.nombre} ha sufrido daños.")
        
        # Verificar si murió
        if self.salud <= 0:
            self.salud = 0
            self.estado = "Marchita"
            print(f"--- LA PLANTA {self.nombre.upper()} SE HA MARCHITADO ---")

# --- Programa Principal ---
print(">>> INICIANDO SISTEMA DE BIO-INGENIERÍA ARES-1 <<<")
n = input("Nombre de la planta: ")
e = input("Especie de la planta: ")

mi_planta = PlantaEspacial(n, e)

opcion = ""
while opcion != "3":
    print(f"\nREPORTE DE BIO-MONITOR: {mi_planta.nombre}")
    print(f"Estado: {mi_planta.estado} | Hidratación: {mi_planta.hidratacion}% | Salud: {mi_planta.salud}%")
    
    print("\n¿Qué acción desea realizar?")
    print("1. Regar")
    print("2. Dejar pasar día")
    print("3. Salir")
    
    opcion = input("Opción: ")

    if opcion == "1":
        mi_planta.regar()
    elif opcion == "2":
        mi_planta.pasar_dia()
    elif opcion == "3":
        print("Cerrando monitor de laboratorio.")
    else:
        print("Selección incorrecta.")