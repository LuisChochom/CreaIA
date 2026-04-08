class CuentaBancaria:
    tasa_interes_global = 0.05  # Tasa de interés global para todas las cuentas
    total_cuentas_creadas = 0  # Contador de cuentas creadas

    def __init__ (self, nombre_titular, titular, saldo):
        self.nombre_titular = nombre_titular
        self.__titular = titular  # Atributo privado
        self.__saldo = 0  # Atributo privado
        CuentaBancaria.total_cuentas_creadas += 1  # Incrementar el contador de cuentas creadas

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular  
    
    @titular.setter
    def titular(self, nuevo_titular):
        if not nuevo_titular:
            print("Error: El nombre del titular no puede estar vacío. Por favor, ingrese un nuevo nombre.")
            return
        else:
            self.__titular = nuevo_titular
            print(f"¡Titular actualizado! El nuevo titular es: {self.__titular}")

    def depositar(self, cantidad):
        if cantidad <= 0:
            print("Error: El cantidad a depositar debe ser mayor a cero. Por favor, ingrese un cantidad válida.")
            return
        else:
            self.__saldo += cantidad
            print(f"¡Depósito exitoso! El nuevo saldo es: Q{self.__saldo}")
    
    def retirar(self, cantidad):
        if cantidad <= 0:
            print("Error: El cantidad a retirar debe ser mayor a cero. Por favor, ingrese un cantidad válido.")
            return
        elif cantidad > self.__saldo:
            print("Error: Fondos insuficientes. No se puede realizar el retiro.")
            return
        else:
            self.__saldo -= cantidad
            print(f"¡Retiro exitoso! El nuevo saldo es: Q{self.__saldo}")
    
    def proyectar_intereses(self, años):
        if años < 0:
            print("Error: El número de años no puede ser negativo. Por favor, ingrese un número válido.")
            return
        else:
            saldo_proyectado = self.__saldo * (1 + CuentaBancaria.tasa_interes_global) ** años
            print(f"El saldo proyectado después de {años} años es: Q{saldo_proyectado:.2f}")
    
    @classmethod
    def actualizar_tasa_interes(cls, nueva_tasa):
        if nueva_tasa < 0:
            print("Error: La tasa de interés no puede ser negativa. Por favor, ingrese una tasa válida.")
            return
        else:
            cls.tasa_interes_global = nueva_tasa
            print(f"¡Tasa de interés actualizada! La nueva tasa de interés global es: {cls.tasa_interes_global:.2%}")
    
cuenta1 = CuentaBancaria("Juan Pérez", "Juan Pérez", 1000)
cuenta2 = CuentaBancaria("María Gómez", "María Gómez", 2000)
print(f"Total de cuentas creadas: {CuentaBancaria.total_cuentas_creadas}")
cuenta1.depositar(10000)
cuenta1.proyectar_intereses(1)
CuentaBancaria.actualizar_tasa_interes(0.10)
cuenta1.proyectar_intereses(1)
cuenta1.titular = ""
    
    