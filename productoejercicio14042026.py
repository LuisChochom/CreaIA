class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __gt__(self, otro_producto):
        return self.precio > otro_producto.precio
    
    def __add__(self, otro_producto):
        return self.precio + otro_producto.precio
    
    def __sub__(self, otro_producto):
        return self.precio - otro_producto.precio
    
    def __str__(self):
        return f"{self.nombre} (Q{self.precio})"

producto1 = Producto("Producto A", 10)
producto2 = Producto("Producto B", 50)
producto3 = Producto("Producto C", 15)
producto4 = Producto("Producto D", 5)

lista_productos = [producto1, producto2, producto3, producto4]

total_inventario = producto1.precio + producto2.precio + producto3.precio + producto4.precio

producto_mas_caro = producto1
for producto in lista_productos:
    if producto > producto_mas_caro:
        producto_mas_caro = producto


print("Resumen del inventario:")
for producto in lista_productos:
    print(producto)

print(f"Total del inventario: Q{total_inventario}")
print(f"Producto más caro: {producto_mas_caro.nombre} con un precio de Q{producto_mas_caro.precio}")