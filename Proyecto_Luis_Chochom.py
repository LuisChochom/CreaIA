# Función para validar que el dato ingresado cumpla con el formato requerido
def es_valido(dato):
    # Verifica que la cadena tenga exactamente 5 caracteres
    if len(dato) != 5:
        return False

    # Verifica que todos los caracteres sean números
    if not dato.isdigit():
        return False

    # El primer dígito debe representar un producto válido (1, 2 o 3)
    if dato[0] != '1' and dato[0] != '2' and dato[0] != '3':
        return False

    # El quinto dígito debe ser un código de control (0 o 1)
    if dato[4] != '0' and dato[4] != '1':
        return False

    return True


# Determina el rango de producción basado en el promedio por lote
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


# Convierte el número de producto en su nombre descriptivo
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


# Acumuladores para los 3 tipos de productos (índices 0, 1 y 2)
lotes = [0, 0, 0]
unidades = [0, 0, 0]

# Lista para almacenar las entradas que no pasaron la validación
datos_invalidos = []

# Bucle principal de captura de datos
while True:
    dato = input("Ingrese el dato o FIN: ")
    dato = dato.upper() # Permite reconocer "fin" en minúsculas

    if dato == "FIN":
        break

    # Si la validación falla, se guarda en la lista de errores
    if es_valido(dato) == False:
        print("Dato invalido")
        datos_invalidos.append(dato)
    else:
        # Extrae el producto y calcula la cantidad desde los caracteres de la cadena
        producto = int(dato[0])
        # Descompone los dígitos 1, 2 y 3 para formar el número de unidades
        cantidad = int(dato[1]) * 100 + int(dato[2]) * 10 + int(dato[3])

        # Ajusta el código de producto al índice de la lista (1-1 = 0, etc.)
        indice = producto - 1

        # Suma un lote y acumula las unidades en la posición correcta
        lotes[indice] = lotes[indice] + 1
        unidades[indice] = unidades[indice] + cantidad


# Bloque para mostrar los registros rechazados
print("\nDatos invalidos ingresados:")
if len(datos_invalidos) == 0:
    print("Ninguno")
else:
    i = 0
    while i < len(datos_invalidos):
        print(datos_invalidos[i])
        i = i + 1

print()


# Impresión de la tabla de resultados con formato de columnas
print(f"{'Producto':15} {'Lotes':15} {'Total unidades':15} {'Prom. por lote':15} {'Categoria':15}")

promedios = [0, 0, 0]

i = 0
while i < 3:
    # Evita error de división por cero si un producto no tuvo ingresos
    if lotes[i] != 0:
        promedio = unidades[i] / lotes[i]
    else:
        promedio = 0

    promedios[i] = promedio
    categoria = obtener_categoria(promedio)

    # Imprime la fila del producto actual alineando columnas y formateando decimales
    print(f"{nombre_producto(i+1):15} {lotes[i]:15} {unidades[i]:15} {promedio:15.2f} {categoria:15}")

    i = i + 1


# Cálculo del producto que acumuló más unidades en total
mayor_unidades = unidades[0]
pos_unidades = 0

i = 1
while i < 3:
    if unidades[i] > mayor_unidades:
        mayor_unidades = unidades[i]
        pos_unidades = i
    i = i + 1


# Cálculo del producto con mayor frecuencia de lotes
mayor_lotes = lotes[0]
pos_lotes = 0

i = 1
while i < 3:
    if lotes[i] > mayor_lotes:
        mayor_lotes = lotes[i]
        pos_lotes = i
    i = i + 1


# Cálculo del promedio general de las categorías activas
suma = 0
contador = 0

i = 0
while i < 3:
    if lotes[i] != 0:
        suma = suma + promedios[i]
        contador = contador + 1
    i = i + 1

# Si no hubo ningún lote válido, el promedio general queda en 0
if contador != 0:
    promedio_general = suma / contador
else:
    promedio_general = 0


# Resumen final de estadísticas
print("Producto mayor cantidades:", nombre_producto(pos_unidades + 1))
print("Producto con mas lotes:", nombre_producto(pos_lotes + 1))
print("Promedio general:", round(promedio_general,2))