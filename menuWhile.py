opcion = ""

while opcion != "salir" and opcion != "2":
    print("1 - saludar")
    print("2 - salir")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1" or opcion == "saludar":
        print("Hola! como estas?")
    elif opcion == "2" or opcion == "salir":
        print("Adios, que tengas un buen dia.")
    else:
        print("Opcion invalida, por favor ingrese una opcion valida.")