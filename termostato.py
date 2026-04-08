class Termostato:
    def __init__(self, temperatura_inicial):
        #atributo privado, acceso solo a traves de los metodos getter y setter
        self.__temperatura = temperatura_inicial

    @property
    def temperatura(self):
        return self.__temperatura

    #El proceso de modificacion de la temperatura se realiza a traves del metodo setter, el cual valida que la nueva temperatura este dentro del rango permitido antes de actualizar el valor del atributo privado
    @temperatura.setter
    def temperatura(self, nueva_temperatura):
        #Dentro del While se valida que la nueva temperatura ingresada por el usuario final este dentro del rango permitido (segun la marca y modelo de aire acondicionado), si no es asi, se muestra un mensaje de error y se solicita ingresar de nuevo la temperatura, hasta que se ingrese un valor valido
        while nueva_temperatura < 16 or nueva_temperatura > 24:
            print("Error: La temperatura debe estar entre 16°C y 24°C. Por favor, ingrese una nueva temperatura.")
            print(f"Temperatura actual: {self.__temperatura}°C")
            nueva_temperatura = float(input("Ingrese la nueva temperatura: "))
        self.__temperatura = nueva_temperatura
        print(f"¡Temperatura actualizada! La nueva temperatura es de: {self.__temperatura}°C, temperatura ideal para un espacio interior.")

control = Termostato(16)
#Consultando la temperatura inicial, desde el metodo getter, para mostrarla al usuario antes de solicitar la nueva temperatura
print(f"Temperatura inicial: {control.temperatura}°C")
nueva_temperatura = float(input("Ingrese la nueva temperatura: "))
control.temperatura = nueva_temperatura