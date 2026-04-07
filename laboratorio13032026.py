nombreEstudiante = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
autorizacionProfesor = input("Autorizado por el profesor (si/no)?: ")
saldoDisponible = float(input("Ingrese el saldo disponible: "))
costoPaqueteMinutosExtra = float(input("Costo de paquete minutos extra: "))

if edad >= 15 and autorizacionProfesor == "si":
    contador = 0

    while saldoDisponible >= costoPaqueteMinutosExtra:
        comprar = input("Desea comprar otro paquete? (si/no) ")
        
        if comprar == "si":
            saldoDisponible -= costoPaqueteMinutosExtra
            contador += 1
        elif comprar == "no":
            print(f"\nAcceso aprobado al laboratorio para { nombreEstudiante.upper()}")
            print(f"Compra Realizada")
            print(f"Paquetes comprados: {contador}")
            print(f"Saldo restante: {saldoDisponible}")
            break
    
    print(f"\nAcceso aprobado al laboratorio para { nombreEstudiante.upper()}") 
    print(f"Compra Realizada")
    print(f"Paquetes comprados: {contador}")
    print(f"Saldo restante: {saldoDisponible}")

else:
    print("No puede ingresar al laboratorio.")

