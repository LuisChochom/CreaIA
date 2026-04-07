print("*"*50)
print("Control de Bodega La Central")
print("*"*50)

cantidad = int(input("Ingrese la cantidad de cajas de leche existentes. "))

if (cantidad > 20):
    print("Inventario saludable.")
elif (cantidad == 1 or cantidad <= 20 ):
    print("Alerta: Hacer pedido al proveedor.")
elif (cantidad == 0):
    print("Urgente: Producto agotado.")