class cajaRegistradora():
    def dinero_actual(self):
        print("="*50)
        dinero_incial = float(input("Ingrese la cantidad de apertura para hoy: "))
        self.dinero_acumulado += dinero_incial
        print(f"Apertura de caja: Q.{self.dinero_acumulado}")
        print("="*50)

    def cobrar_producto(self):
        precio = float(input("Ingrese el precio del producto: "))
        self.dinero_acumulado = self.dinero_acumulado + precio
        print(f"Cobro exitoso. Llevamos acumulado: Q.{self.dinero_acumulado}")
        print("="*50)

    def imprimir_cierre_turno(self):
        print(f"Cajero: {self.nombre_cajero} , el total de dinero recaudado en el dia es: Q.{self.dinero_acumulado}") 

caja_express = cajaRegistradora()
caja_express.dinero_acumulado = 0
caja_express.nombre_cajero = "Luis"

while True:
    print("1. Aperturar caja.")
    print("2. Vender producto.")
    print("3. Cierre de caja.")
    print("4. Salir")
    opcion = input("Ingrese la operacion que desea realizar: ")
    match opcion:
        case "1":
            caja_express.dinero_actual()
        case "2":
            caja_express.cobrar_producto()
        case "3":
            caja_express.imprimir_cierre_turno()
            print("Saliendo del sistema...")
            break
        case "4":
            print("Saliendo del sistema...")
            break

    
