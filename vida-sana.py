from abc import ABC, abstractmethod

class PersonalMedico(ABC):
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
    
    @abstractmethod
    def realizar_labor(self):
        pass

class Doctor(PersonalMedico):
    def realizar_labor(self):
        print(f"[SISTEMA] El Dr. {self.nombre} está realizando un diagnóstico especializado.")

    def atender_paciente(self, paciente):
        print(f"Atendiendo al paciente {paciente.nombre}.")
        self.realizar_labor()

        nota = input("Ingrese nota para el historial: ")
        paciente.historial.agregar_observacion(nota)

        while True:
            try:
                dosis = float(input("Ingrese dosis de recuperación (1-50): "))
                paciente.recibir_tratamiento(dosis)
                print(f"¡Tratamiento Exitoso! La salud de {paciente.nombre} ha subido a {paciente.salud}%.")
                break
            except ValueError:
                print("[ERROR]: Solo se permiten valores numéricos para la dosis. Intente de nuevo.")

class Enfermero(PersonalMedico):
    def realizar_labor(self):
        print(f"[SISTEMA] El enfermero/a {self.nombre} está aplicando cuidados y revisando signos vitales.")

class HistorialClinico:
    def __init__(self):
        self.observaciones = [] 
    
    def agregar_observacion(self, observacion):
        self.observaciones.append(observacion)
    
    def mostrar_notas(self):
        if not self.observaciones:
            print("No hay notas en el historial clínico.")
        else:
            print("Notas del Historial Clínico:")
            for idx, nota in enumerate(self.observaciones, 1):
                print(f"{idx}. {nota}")

class Paciente:
    def __init__ (self, nombre, edad, salud_inicial):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud_inicial

        self.historial = HistorialClinico()
    
    def recibir_tratamiento(self, cantidad):
        self.salud += cantidad
        if self.salud > 100:
            self.salud = 100

    def obtener_estado(self):
        if self.salud < 20:
            return f"{self.salud}% [CRÍTICO]"
        return f"{self.salud}%"

class Hospital:
    def __init__(self):
        self.lista_pacientes = []
        self.lista_personal = []
    
    def registrar_paciente(self):
        nombre = input("Nombre del paciente: ")
        try:
            edad = int(input("Edad: "))
            salud = float(input("Salud inicial (0-100): "))
            nuevo = Paciente(nombre, edad, salud)
            self.lista_pacientes.append(nuevo)
        except ValueError:
            print("[ERROR] Entrada inválida. Use números para edad y salud.")

    def contratar_personal(self):
        print("1. Doctor / 2. Enfermero")
        tipo = input("Tipo: ")
        nom = input("Nombre: ")
        esp = input("Especialidad: ")
        if tipo == "1":
            self.lista_personal.append(Doctor(nom, esp))
        else:
            self.lista_personal.append(Enfermero(nom, esp))

    def mostrar_reporte(self):
        print("\n" + "="*45)
        print(f"{'PACIENTE':<15} | {'EDAD':<5} | {'ESTADO':<15}")
        print("-" * 45)
        for p in self.lista_pacientes:
            print(f"{p.nombre:<15} | {p.edad:<5} | {p.obtener_estado():<15}")
        print("="*45)
    

def menu_hospital():
    mi_hospital = Hospital()
    
    mi_hospital.lista_personal.append(Doctor("House", "Especialista"))
    mi_hospital.lista_pacientes.append(Paciente("Rodrigo", 45, 15))

    while True:
        print("\n>>> SISTEMA HOSPITALARIO VIDA-SANA <<<<<<")
        print("1. Registrar Paciente\n2. Contratar Personal\n3. Realizar Consulta Médica\n4. Ver Reporte\n5. Salir") 
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                mi_hospital.registrar_paciente()
            elif opcion == 2:
                mi_hospital.contratar_personal()
            elif opcion == 3:
                if not mi_hospital.lista_personal or not mi_hospital.lista_pacientes:
                    print("[AVISO] Debe haber personal y pacientes registrados.")
                    continue

                print("\nPersonal Disponible")
                for i in range(len(mi_hospital.lista_personal)):
                    pers = mi_hospital.lista_personal[i]
                    print(f"{i}. {pers.nombre} ({pers.especialidad})")
                med_idx = int(input("Elija el médico: "))

                print("\nPacientes en Espera")
                for i in range(len(mi_hospital.lista_pacientes)):
                    pac = mi_hospital.lista_pacientes[i]
                    print(f"{i}. {pac.nombre} (Edad: {pac.edad} | Salud: {pac.obtener_estado()})")
                pac_idx = int(input("Elija el paciente: "))

                doctor = mi_hospital.lista_personal[med_idx]
                paciente = mi_hospital.lista_pacientes[pac_idx]
                
                if isinstance(doctor, Doctor):
                    doctor.atender_paciente(paciente)
                else:
                    doctor.realizar_labor()
                    
            elif opcion == 4:
                mi_hospital.mostrar_reporte()
            elif opcion == 5:
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida.")
        except (ValueError, IndexError):
            print("[ERROR]: Selección inválida o dato no numérico.")


menu_hospital()