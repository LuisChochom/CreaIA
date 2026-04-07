def saludo(nombre):
    print("hola buenos días!")
    print(f"¿Cómo estás, {nombre}?")

def despedida(nombre):
    print("adiós, que tengas un buen día!")
    print(f"¡Hasta luego, {nombre}!")

def calculo_impuestos(precio):
    impuestos = precio * 0.15
    total = precio + impuestos

    return total


# funcion con vario puntos de retorno
def generar_mensaje(nombre):
    if nombre == "Alice":
        return "Hola Alice, ¿cómo estás?"
    
        # esto no se va a ejecutar porque el return anterior ya terminó la función
        apellido = input("Ingrese su apellido: ")
        return f"Hola {nombre} {apellido}, ¿cómo estás?"
    
    elif nombre == "Bob":
        return "Hola Bob, ¿cómo estás?"
    else:
        return "Hola, ¿cómo estás?"
    

def menu():
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Calcular impuestos")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    nombre = input("Ingrese su nombre: ")

    while True:
        match opcion:
            case "1":
                saludo(nombre)
            case "2":
                despedida(nombre)
            case "3":
                precio = float(input("Ingrese el precio: "))
                precio_total = calculo_impuestos(precio)

                print(f"El precio total con impuestos es: {precio_total}")
            case "4":
                print("Saliendo...")
                break

            case _:
                print("Opción no válida")

        opcion = input("Seleccione una opción: ")


menu()
