print("="*25)
print("Ejercicio #1")
print("="*25)

nombreParticipante = input("Ingrese el nombre del participante. ")
edad = int(input("Ingrese la edad del participante. "))
inscripcion = input("El participante tiene inscripcion. (si/no) ")

if (edad >= 15) and (inscripcion == "si"):
    print("Participante autorizado para ingresar al torneo.")
else:
    print("Participante no autorizado para ingresar al torneo.")

print("="*25)
print("Ejercicio #2")
print("="*25)

bateria = int(input("Ingrese el porcentaje de batería: "))
if bateria <= 20:
    print("Debe cargar el celular")
else:
    print("La batería es suficiente")

print("="*25)
print("Ejercicio #3")
print("="*25)

pesoPaquete = float(input("Ingrese el peso (kg) del paquete a enviar: "))

if pesoPaquete < 1:
    print("Paquete liviano")
elif 1 <= pesoPaquete <= 5:
    print("Paquete estándar")
elif pesoPaquete > 5:
    print("Paquete pesado")

print("="*25)
print("Ejercicio #4")
print("="*25)

color = input("Ingrese el color del semáforo: ")
if color == "verde":
    print("Avanzar")
elif color == "amarillo":
    print("Precaución")
else:
    print("Detenerse")

print("="*25)
print("Ejercicio #5")
print("="*25)
nombreCliente = input("Ingrese el nombre del cliente: ")
edad = int(input("Ingrese la edad del cliente: "))
tipoEntrada = input("Ingrese el tipo de entrada  ( general o vip )")
dineroDisponible = float(input("Dinero disponible del cliente: "))
precioBebidaEspecial = float(input("Ingrese el precio de la bebida especial: "))

if tipoEntrada == "vip":
    print("Validando el ingreso a vip")
    if edad >= 18:
        print("Tiene acceso al VIP")
        print(f"Acceso aprobado para {nombreCliente}")
        comprarBebida = input("Desea comprar bebida especial (si/no): ")
        if comprarBebida == "si":
            if dineroDisponible >= precioBebidaEspecial:
                cambio = dineroDisponible - precioBebidaEspecial
                print(f"Su cambio es de: {cambio}")
                print("Gracias por preferirnos.")
            else:
                print("No cuenta con fondos suficientes para su compra.")
        else:
            print("Bienvenido! que tenga una excelente experiencia.")
    else:
        print ("No cumple con la mayoria de edad para ingresar al area VIP.")
else:
    print("Su tipo de entrada es general. Bienvenido.")


print("="*25)
print("Ejercicio #6")
print("="*25)

nombreEstudiante = input("Ingrese el nombre del estudiante: ")
promedioFinal = float(input("Promedio final: "))
ingresoFamiliarMensual = float(input("Indique el ingreso familiar mensual: "))
cantidadMateriasAprobadas = int(input("Cantidad de materia aprobadas: "))

if promedioFinal < 70:
    print("No recibe beca")
    print("Sin beca 0")
elif promedioFinal == 70 or promedioFinal <= 84 and ingresoFamiliarMensual <= 400000:
    print(f"Estudiante: {nombreEstudiante}")
    print("Resultado: Beca parcial.")
    print("Monto asignado: 50000")
elif promedioFinal >= 85 and cantidadMateriasAprobadas >= 5 and ingresoFamiliarMensual <= 400000:
    print(f"Estudiante: {nombreEstudiante}")
    print("Resultado: Beca completa.")
    print("Monto asignado: 100000")

print("="*25)
print("Ejercicio #7")
print("="*25)

nombreDelCliente = input("Ingrese el nombre del cliente: ")
temporada = input("( alta , media , baja ) ")
cantidadDeNoches = int(input("Ingrese la cantida de noches: "))
precioBaseNoche = float(input("Ingrese el precio por noche: "))
tieneMembresía = input("tiene membresia ( si/no )? ")

if temporada == "alta" and cantidadDeNoches < 3:
    totalBase = cantidadDeNoches * precioBaseNoche
    subtotal = totalBase * 0.20
    total = totalBase + subtotal
    descuento = 0
    totalFinal = total - descuento
    print (f"Cliente: {nombreDelCliente}")
    print (f"Subtotal con recargo: {total}")
    print (f"Descuento aplicado: {descuento}")
    print (f"Total final: {totalFinal}")
elif temporada == "alta" and tieneMembresía == "si" and cantidadDeNoches >= 3:
    totalBase = cantidadDeNoches * precioBaseNoche
    subtotal = totalBase * 0.20
    total = totalBase + subtotal
    descuento = total * 0.15
    totalFinal = total - descuento
    print (f"Cliente: {nombreDelCliente}")
    print (f"Subtotal con recargo: {total}")
    print (f"Descuento aplicado: {descuento}")
    print (f"Total final: {totalFinal}")
elif temporada == "alta" and tieneMembresía == "si" or cantidadDeNoches == 2:
    totalBase = cantidadDeNoches * precioBaseNoche
    subtotal = totalBase * 0.20
    total = totalBase + subtotal
    descuento = total * 0.05
    totalFinal = total - descuento
    print (f"Cliente: {nombreDelCliente}")
    print (f"Subtotal con recargo: {total}")
    print (f"Descuento aplicado: {descuento}")
    print (f"Total final: {totalFinal}")
elif temporada == "media" and cantidadDeNoches < 3:
    totalBase = cantidadDeNoches * precioBaseNoche
    subtotal = totalBase * 0.10
    total = totalBase + subtotal
    descuento = 0
    totalFinal = total - descuento
    print (f"Cliente: {nombreDelCliente}")
    print (f"Subtotal con recargo: {total}")
    print (f"Descuento aplicado: {descuento}")
    print (f"Total final: {totalFinal}")
elif temporada == "media" and tieneMembresía == "si" and cantidadDeNoches >= 3:
    totalBase = cantidadDeNoches * precioBaseNoche
    subtotal = totalBase * 0.10
    total = totalBase + subtotal
    descuento = total * 0.15
    totalFinal = total - descuento
    print (f"Cliente: {nombreDelCliente}")
    print (f"Subtotal con recargo: {total}")
    print (f"Descuento aplicado: {descuento}")
    print (f"Total final: {totalFinal}")
elif temporada == "media" and tieneMembresía == "si" or cantidadDeNoches == 2:
    totalBase = cantidadDeNoches * precioBaseNoche
    subtotal = totalBase * 0.10
    total = totalBase + subtotal
    descuento = total * 0.05
    totalFinal = total - descuento
    print (f"Cliente: {nombreDelCliente}")
    print (f"Subtotal con recargo: {total}")
    print (f"Descuento aplicado: {descuento}")
    print (f"Total final: {totalFinal}")
elif temporada == "baja":
    totalBase = cantidadDeNoches * precioBaseNoche
    subtotal = 0
    total = totalBase + subtotal
    descuento = 0
    totalFinal = total - descuento
    print (f"Cliente: {nombreDelCliente}")
    print (f"Subtotal con recargo: {total}")
    print (f"Descuento aplicado: {descuento}")
    print (f"Total final: {totalFinal}")


print("="*25)
print("Ejercicio #8")
print("="*25)

opcion = input("Ingrese una opcion (1 o matricular, 2 o notas, 3 o certificado, 4 o salir): ")
tipoDeUsuario = input("Ingrese el tipo de usuario ( admin , profesor , estudiante ) ")
promedioDelEstudiante = float(input("Ingrese el promedio del estudiante: "))

match opcion:
    case ("1" | "matricular") if tipoDeUsuario == "admin" or tipoDeUsuario == "profesor":
        print ("Matriculacion realizada correctamente.")
    case ("2" | "notas") if tipoDeUsuario == "estudiante" or tipoDeUsuario == "profesor":
        print ("Notas mostradas correctamente.")
    case ("3" | "certificado") if tipoDeUsuario == "estudiante" and promedioDelEstudiante >= 70:
        print ("Certificado generado correctamente.")
    case "4" | "salir":
        print ("Saliendo...")


print("="*25)
print("Ejercicio #9")
print("="*25)

nombreCliente = input("Ingrese el nombre del cliente: ")
nombreDelProducto = input("Ingrese el nombre del producto: ")
precioUnitario = float(input("Ingrese el precio unitario del producto: "))
cantidadDeseada = int(input("Ingrese la cantidad a comprar: "))
cantidadEnStock = int(input("Ingrese la cantidad existente en tienda: "))
membresiaGamer = input("Tiene membresia gamer ( si/no ) ")

if cantidadDeseada > cantidadEnStock:
    print("No se puede realizar la venta.")
elif cantidadEnStock > cantidadDeseada:
    subtotal = cantidadDeseada * precioUnitario
    if subtotal > 50000 and membresiaGamer == "si":
        descuento = subtotal * 0.20
        total = subtotal - descuento
    elif subtotal > 30000 or membresiaGamer == "si":
        descuento = subtotal * 0.10
        total = subtotal - descuento
    else:
        descuento = 0
        total = subtotal - descuento

    print("Venta aprobada.")
    print(f"Subtotal: {subtotal}")
    print(f"Descuento: {descuento}")
    print(f"Total final: {total}")


print("="*25)
print("Ejercicio #10")
print("="*25)

nombreDelJugador = input("Ingrese el nombre del jugador: ")
claseDelJugador = input("Tipo de jugador ( guerrero , mago , arquero ) ")
opcionDeMision = input("Ingrese la opcion de mision: ") 
nivelDelJugador = int(input("Ingrese el nivel del jugador: "))
cantidadEnemigosDerrotados = int(input("Ingrese la cantidad de enemigos derrotados: "))

match opcionDeMision:
    case "1" | "bosque":
        recompensa = cantidadEnemigosDerrotados * 10
        print(f"Mision {opcionDeMision} completada")
        print(f"Recompensa base: {recompensa}")
        print(f"Recompensa total: {recompensa}")
    case "2" | "castillo" if nivelDelJugador >= 5:
        recompensa = cantidadEnemigosDerrotados * 20
        print(f"Mision {opcionDeMision} completada")
        print(f"Recompensa base: {recompensa}")
        if claseDelJugador == "guerrero" or claseDelJugador == "mago":
            bonoExtra = 50
            recompensaTotal = recompensa + bonoExtra
            print(f"Bono adicional: {bonoExtra}")
            print(f"Recompensa total: {recompensaTotal}")
        else:
            print(f"Recompensa total: {recompensa}")

    case "3" | "dragon" if nivelDelJugador >= 10:
        recompensa = cantidadEnemigosDerrotados * 50
        print(f"Mision {opcionDeMision} completada")
        print(f"Recompensa base: {recompensa}")
        if claseDelJugador == "guerrero" or claseDelJugador == "arquero":
            if cantidadEnemigosDerrotados > 3:
                bonoExtra = 100
            else:
                bonoExtra = 0
            recompensaTotal = recompensa + bonoExtra
            print(f"Bono adicional: {bonoExtra}")
            print(f"Recompensa total: {recompensaTotal}")
        else:
            print(f"Recompensa total: {recompensa}")
    case "4" | "Salir":
        print("Saliendo...")