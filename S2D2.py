# class Cuenta:
#     def __init__(self, saldo_inicial):
#         self.nombre = "Pública"
#         self.__saldo = saldo_inicial 


# mi_cuenta = Cuenta(1000)
# print(mi_cuenta.nombre)
# print(mi_cuenta.__saldo) #. ERROR, Python no permite acceder a atributos privados desde fuera de la clase.


class UsuarioBancario:
    def __init__(self, nombre_ingresado, pin_ingresado):
        self.nombre = nombre_ingresado
        # atributo privado
        self.__pin = pin_ingresado


    # get tradicional (ventanilla para consultar)
    def get_pin(self):
        return self.__pin

    def set_pin(self, nuevo_pin):
        # validación
        #       1234 -> "1234"
        if len( str(nuevo_pin) ) == 4:
            self.__pin = nuevo_pin
            print("Operación exitosa. PIN actualizado")
        else:
            print("Error: El PIN debe de tener exactamente 4 dígitos")

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre



# programa principal
print("--- SISTEMA DE SEGURIDAD ---")
cliente = UsuarioBancario("Diego", 1234)

# primer intento de hackeo: intentar acceder directamente al atributo privado
# print(cliente.__pin) # ERROR, no se puede acceder a un atributo privado desde fuera de la clase

# segundo intento de hackeo: intentar acceder al atributo privado usando el método get
print(cliente.get_pin()) # aunque el método get_pin() nos permite acceder al valor del PIN
# o opcion 2 cuardando el valor del PIN en una variable
pin_cliente = cliente.get_pin()
print(pin_cliente)

cliente.set_pin(5544) # operación exitosa

pin_cliente = cliente.get_pin()
print(pin_cliente)
