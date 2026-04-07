inventario = [
    ["Croquetas", 15, 20, 0],
    ["Juguete", 10, 5, 0],
    ["Champu", 5, 12, 0]
]

def valor_total(fila):
    return fila[1] * fila[2]

def mostrar_resumen_final():
    total_acumulado = 0
    print("\n" + "*"*45)
    print("      RESUMEN INVENTARIO 'HUELLITAS'")
    print("*"*45)
    
    for i in range(len(inventario)):
        subtotal = valor_total(inventario[i])
        inventario[i][3] = subtotal
        total_acumulado += subtotal
        
        print(f"Producto: {inventario[i][0]:<12} | Valor Estante: Q{subtotal}")
    
    print("*" * 45)
    print(f"VALOR TOTAL INVENTARIO: Q{total_acumulado}")
    print("*"*45)

print ("Prodcutos disponibles.")
for i in range(len(inventario)):
    print(f"Producto: {inventario[i][0]:<12} | Stock: {inventario[i][1]:<12} | Precio: Q{inventario[i][2]:<12}")

while True:
    print("\n MENÚ PRINCIPAL ")
    print("1. Vender | 2. Agregar | 3. Eliminar | 4. Salir e Imprimir Resumen")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        for p in inventario:
            if p[0].lower() == nombre.lower():
                cantidad = int(input(f"cantidad de {p[0]} a vender: "))
                if cantidad <= p[1]:
                    p[1] -= cantidad
                    print("¡Venta exitosa!")
                else:
                    print(f"Error: Solo hay {p[1]} unidades.")
                break
    
    elif opcion == "2":
        nombre = input("Nuevo Producto: ")
        stock = int(input("Stock inicial: "))
        precio = float(input("Precio: "))
        inventario.append([nombre, stock, precio, 0])
        print(f"'{nombre}' agregado correctamente.")

    elif opcion == "3":
        nombre = input("Nombre a eliminar: ")
        for i in range(len(inventario)):
            if inventario[i][0].lower() == nombre.lower():
                inventario.pop(i)
                print(f"'{nombre}' eliminado del sistema.")
                break

    elif opcion == "4":
        mostrar_resumen_final()
        print("\nCerrando sistema...")
        break