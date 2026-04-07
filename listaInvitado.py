lista_invitados = []

def agregar_invitado(nombre, lista_invitados_local):
    lista_invitados_local.append(nombre)
    return lista_invitados_local

def mostrar_lista(lista_invitados):
    for invitado in lista_invitados:
            print(f"Nombre: {invitado}")

def buscar_invitado(nombre, lista_invitados):
    if nombre in lista_invitados:
        return True
    else:
        return False

def eliminar_invitado(nombre, lista_invitados_local):
    if buscar_invitado(nombre):
        lista_invitados_local.remove(nombre)
        print ("Nombre eliminado de la lista.")
        return lista_invitados_local
    else:
        print("El nombre no esta en la lista")

def menu(lista_invitados):
    print ("1.Registrar nuevo invitado.")
    print ("2. Ver lista completa.")
    print ("3. Eliminar a alguien (por si se porta mal).")
    print ("4. Salir.")

    while True:
        opcion = int(input("Selecciona una opción: "))

        match opcion:
            case 1:
                nombre = input("Ingrese el nombre de la persona a registrar. ")
                lista_invitados = agregar_invitado(nombre, lista_invitados)
                print("Registro exitoso...")
            case 2:
                mostrar_lista(lista_invitados)
            case 3:
                nombre = input("Ingrese el nombre de la persona a eliminar: ")
                lista_invitados = eliminar_invitado(nombre, lista_invitados)
            case 4:
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Inténtalo de nuevo.")


menu(lista_invitados)