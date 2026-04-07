# * **Instrucción:** El gerente necesita calcular precios al por mayor. Pide al usuario que ingrese un número (ejemplo: 7), para imprimir la tabla de multiplicar de ese número del 1 al 10.
numero = int(input("Ingrese el numero para mostrar la tabla de multiplicar: "))
for index in range(1, 11):
    multi = index * numero
    print(f"{index} * {numero} = {multi}")


# Reto 2: La Meta de Ahorro de la Tienda (Uso de 'while')
# * **Instrucción:** La tienda quiere comprar un nuevo rótulo luminoso que cuesta 100,000 dólares. Crea un programa que tenga una meta de 100000 y un ahorro que empiece en 0. Usa un bucle para preguntarle al gerente: "¿Cuánto dinero depositamos hoy a la cuenta de ahorros?". Suma eso al ahorro total. El bucle debe repetirse *mientras* el ahorro sea menor a la meta. Al salir del bucle, felicita al gerente.
         
