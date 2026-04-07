class RegistroAcademico:
    def __init__(self, nombre_alumno, nota_inicial):
        self.nombre = nombre_alumno #publico
        self.__nota = nota_inicial #privado
        self.cuenta_activa = True # atributo para controlar el estado de la cuenta (activa o bloqueada)
    
    def get_nota(self):
        return self.__nota
    
    def set_nota(self, nueva_nota):
        if self.cuenta_activa == False:
            return -2
        elif 0 <= nueva_nota <= 100:
            return 1
        else:
            return -1

    def bloquear_cuenta(self):
        self.cuenta_activa = False
        print("----------------------------------------------")
        print(f"La cuenta de {self.nombre} ha sido bloqueada.")

alumna = RegistroAcademico("Laura", 85)
intentos_permitidos = 3

while intentos_permitidos > 0:
    nueva_nota = float(input(f"Intentos restantes ({intentos_permitidos}). Ingrese la nueva nota para {alumna.nombre}: "))
    resultado = alumna.set_nota(nueva_nota)

    if resultado == 1:
            print(f"¡Felicidades! La nota de {alumna.nombre} ha sido actualizada a {nueva_nota}.")
            break  
    elif resultado == -1:
        intentos_permitidos -= 1
        print(f"Error: La nota debe estar entre 0 y 100. Te quedan {intentos_permitidos} intentos.")

if intentos_permitidos == 0:
    alumna.bloquear_cuenta()
    print("--- SISTEMA BLOQUEADO ---")
    print(f"La cuenta de {alumna.nombre} ha sido bloqueada por demasiados intentos fallidos.")


