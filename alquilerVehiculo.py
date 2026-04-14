class Vehiculo:
    contador = 0
    def __init__(self, placa, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.precio_alquiler = 100
        self.__kilometraje = 0
        Vehiculo.contador += 1
    
    def disponible(self):
        self.disponible = True
        print(f"El vehículo {self.placa} está disponible para alquiler.")
    
    def alquilado(self):
        self.disponible = False
        print(f"El vehículo {self.placa} ha sido alquilado.")

    def devolver(self):
        self.disponible = True
        print(f"El vehículo {self.placa} ha sido devuelto y está disponible nuevamente.")

    @property
    def kilometraje(self):
        return self.__kilometraje

    @kilometraje.setter
    def actualizar_kilometraje(self, kilometros):
        self.__kilometraje += kilometros
        print(f"El kilometraje del vehículo {self.placa} se ha actualizado a {self.__kilometraje} km.")
    
    def cantidad_vehiculos(self):
        print(f"Cantidad total de vehículos: {Vehiculo.contador}")
    
class Alquiler:
    def __init__(self, placa_ingresada, marca_ingresada, modelo_ingresado):
        self.vehiculo = Vehiculo(placa_ingresada, marca_ingresada, modelo_ingresado)
    
    def mostrar_informacion(self):
        print(f"Información del vehículo: Placa: {self.vehiculo.placa}, Marca: {self.vehiculo.marca}, Modelo: {self.vehiculo.modelo}, Precio de alquiler: Q{self.vehiculo.precio_alquiler}")

print("Bienvenido al sistema de alquiler de vehículos")
vehiculo = Alquiler("ABC123", "Toyota", "Corolla")
print(f"Cantidad de vehiculos disponibles: {Vehiculo.contador}")
vehiculo.mostrar_informacion()
vehiculo.vehiculo.disponible()
vehiculo.vehiculo.alquilado()