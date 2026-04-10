# Definición de la clase
class AgenteSeguridad:
    
    # Método para evaluar si puede entrar
    def evaluar_entrada(self):
        # Pedir nivel de seguridad de la puerta
        nivel_puerta = int(input("Ingrese el nivel de seguridad de la puerta (1-5): "))
        
        # Comparar niveles
        if self.nivel_acceso >= nivel_puerta:
            print("Acceso concedido para", self.nombre)
        else:
            print("Acceso denegado")


# Programa principal

# Crear objeto
guardia_turno = AgenteSeguridad()

# Asignar atributos manualmente
guardia_turno.nombre = input("Ingrese el nombre del guardia: ")
guardia_turno.nivel_acceso = int(input("Ingrese el nivel de acceso del guardia (1-5): "))

# Llamar al método
guardia_turno.evaluar_entrada()