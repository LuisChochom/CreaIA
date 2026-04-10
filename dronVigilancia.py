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