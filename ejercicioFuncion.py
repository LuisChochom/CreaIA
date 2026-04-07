def mensaje_bienvenida():
    print ("Bienvenido al sistema de venta\nEsperamos que tenga una excelente compra.")

def saludar_cliente(nombre):
    return f"Hola {nombre}, bienvenido al gimnasio"

def calcular_total(precio, cantidad):
    total_pagar = precio * cantidad
    return total_pagar

def comprar_fichas(dinero_disponible):
    precio_ficha = 9.99
    if dinero_disponible >= precio_ficha:
        cantidad_compra = dinero_disponible / precio_ficha
        total_compra = cantidad_compra * precio_ficha
        cambio = dinero_disponible - total_compra
        return cantidad_compra, cambio
    elif dinero_disponible < precio_ficha:
        cantidad_compra = 0
        cambio = 0
        return cantidad_compra, cambio
def es_mayor_de_edad(edad):
    if edad >= 18:
        return edad == True
    else:
        return edad == False


def main():
    opcion = int(input("Ingrese la opcion a elegir (1.Mensaje simple 2.Saludar cliente 3.Calcular Total 4.Comprar fichas"))

    match opcion:
        case 1:
            mensaje_bienvenida()
        case 2:
            nombre = input("Ingrese su nombre: ")
            print (saludar_cliente(nombre))
        case 3:
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantida a comprar: "))

            print(f"El total a pagar: {calcular_total(precio, cantidad)}")
        case 4:
            opcion = input("Ingrese una de las dos opciones que desea realizar (comprar o salir): ")

            while (opcion != "salir"):
                nombre = input("Ingrese su nombre: ")
                dinero_disponible = float(input("Ingrese la cantidad de dinero que tiene disponible: "))
                cantidad_compra, cambio = comprar_fichas(dinero_disponible)

                if cantidad_compra == 0 and cambio == 0:
                    print ("No cuenta con suficientes fondos.")
                    break
                else:
                    print (f"Cantidad monedas a comprar: {cantidad_compra}")
                    print (f"Cambio: {cambio}")
        case 5:
            edad = int(input("Ingrese la edad de la persona: "))
            edad = es_mayor_de_edad(edad)
            if edad == True:
                print("Es mayor de edad.")
            else:
                print ("Es menor de edad.")
            

main()
