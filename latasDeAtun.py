print("Por favor ingrese la cantidad de latas que desea acomodar para calcular los estantes necesarios")
latas = int(input("Ingrese la cantidad de latas: "))
cantidadPorEstante = int(input("Ingrese la cantidad de latas por estante. "))
latasRestantes = latas%cantidadPorEstante
estantesNecesario = int(latas / cantidadPorEstante)
print(f"Los estantes necesario son: {estantesNecesario}")
print(f"Latas que no se acomodaria en los estantes: {latasRestantes}")