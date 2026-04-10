def es_valido(dato):
    if len(dato) != 5:
        return False

    if not dato.isdigit():
        return False

    if dato[0] != '1' and dato[0] != '2' and dato[0] != '3':
        return False

    if dato[4] != '0' and dato[4] != '1':
        return False

    return True


def obtener_categoria(promedio):
    if promedio <= 99:
        return "Insuficiente"
    else:
        if promedio <= 299:
            return "Regular"
        else:
            if promedio <= 599:
                return "Idoneo"
            else:
                return "Sobreproduccion"


def nombre_producto(codigo):
    if codigo == 1:
        return "Fertilizante"
    else:
        if codigo == 2:
            return "Insecticida"
        else:
            if codigo == 3:
                return "Herbicida"
            else:
                return "Desconocido"


lotes = [0, 0, 0]
unidades = [0, 0, 0]

# Lista para guardar datos invalidos
datos_invalidos = []

while True:
    dato = input("Ingrese el dato o FIN: ")
    dato = dato.upper()

    if dato == "FIN":
        break

    if es_valido(dato) == False:
        print("Dato invalido")
        datos_invalidos.append(dato)
    else:
        producto = int(dato[0])
        cantidad = int(dato[1]) * 100 + int(dato[2]) * 10 + int(dato[3])

        indice = producto - 1

        lotes[indice] = lotes[indice] + 1
        unidades[indice] = unidades[indice] + cantidad


# Mostrar datos invalidos antes de la tabla
print("\nDatos invalidos ingresados:")

if len(datos_invalidos) == 0:
    print("Ninguno")
else:
    i = 0
    while i < len(datos_invalidos):
        print(datos_invalidos[i])
        i = i + 1

print()


# Mostrar tabla
print(f"{'Producto':15} {'Lotes':15} {'Total unidades':15} {'Prom. por lote':15} {'Categoria':15}")

promedios = [0, 0, 0]

i = 0
while i < 3:
    if lotes[i] != 0:
        promedio = unidades[i] / lotes[i]
    else:
        promedio = 0

    promedios[i] = promedio
    categoria = obtener_categoria(promedio)

    print(f"{nombre_producto(i+1):15} {lotes[i]:15} {unidades[i]:15} {promedio:15.2f} {categoria:15}")

    i = i + 1


# Producto con mayor unidades
mayor_unidades = unidades[0]
pos_unidades = 0

i = 1
while i < 3:
    if unidades[i] > mayor_unidades:
        mayor_unidades = unidades[i]
        pos_unidades = i
    i = i + 1


# Producto con más lotes
mayor_lotes = lotes[0]
pos_lotes = 0

i = 1
while i < 3:
    if lotes[i] > mayor_lotes:
        mayor_lotes = lotes[i]
        pos_lotes = i
    i = i + 1


# Promedio general
suma = 0
contador = 0

i = 0
while i < 3:
    if lotes[i] != 0:
        suma = suma + promedios[i]
        contador = contador + 1
    i = i + 1

if contador != 0:
    promedio_general = suma / contador
else:
    promedio_general = 0


print("Producto mayor cantidades:", nombre_producto(pos_unidades + 1))
print("Producto con mas lotes:", nombre_producto(pos_lotes + 1))
print("Promedio general:", round(promedio_general,2))