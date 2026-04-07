def es_valido(dato):
    # Validar longitud y que sean dígitos
    if len(dato) != 5 or not dato.isdigit():
        return False
    
    # Validar producto
    if dato[0] not in ['1', '2', '3']:
        return False
    
    #Validar entregado o no
    if dato[4] not in ['0', '1']:
        return False
    return True

def obtener_categoria(promedio):
    if promedio <= 99:
        return "Insuficiente"
    elif promedio <= 299:
        return "Regular"
    elif promedio <= 599:
        return "Idoneo"
    else:
        return "Sobreproduccion"


def nombre_producto(codigo):
    if codigo == 1:
        return "Fertilizante"
    elif codigo == 2:
        return "Insecticida"
    elif codigo == 3:
        return "Herbicida"
    else:
        return "Desconocido"


# Listas para acumular datos indice: 0. Fertilizante 1. Insecticida 2. Herbicida
lotes = [0, 0, 0]
unidades = [0, 0, 0]

while True:
    dato = input()
    #Esta linea de codigo es para convertir el fin de minuscula a mayuscula, para que el programa pueda reconocerlo y finalizar la entrada de datos
    dato = dato.upper()

    if dato == "FIN":
        #Detiene el while y finaliza la entrada de datos
        break

    if not es_valido(dato):
        print(f"dato invalido {dato}")
        continue

    #Extraer producto y cantidad del dato ingresado
    producto = int(dato[0])
    cantidad = int(dato[1:4])

    #El indice del producto se obtiene restando 1 al número del producto, ya que los índices de las listas comienzan en 0
    indice = producto - 1

    lotes[indice] += 1 #suma la cantidad de lotes ingresados
    unidades[indice] += cantidad #suma la cantidad producida de un lote

# Mostrar tabla
print(f"{'Producto':15} {'Lotes':15} {'Total unidades':15} {'Prom. por lote':15} {'Categoria':15}")

promedios = [0, 0, 0]

for i in range(3):
    if lotes[i] > 0:
        promedio = unidades[i] / lotes[i]
    else:
        promedio = 0

    promedios[i] = promedio
    categoria = obtener_categoria(promedio)

    print(f"{nombre_producto(i+1):15} {lotes[i]:15} {unidades[i]:15} {promedio:15.2f} {categoria:15}")

# Producto con mayor unidades
max_unidades = max(unidades)
prod_max_unidades = unidades.index(max_unidades) + 1

# Producto con más lotes
max_lotes = max(lotes)
prod_max_lotes = lotes.index(max_lotes) + 1

# Promedio general
total_unidades = sum(unidades)
total_lotes = sum(lotes)

if total_lotes > 0:
    promedio_general = total_unidades / total_lotes
else:
    promedio_general = 0



print(f"\nProducto mayor cantidades: {nombre_producto(prod_max_unidades)}")
print(f"Producto con mas lotes: {nombre_producto(prod_max_lotes)}")
print(f"Promedio de productos producidos: {promedio_general:.2f}")