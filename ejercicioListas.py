# Lista de estantes con cantidades de productos
inventario = [
    [10, 4, 8],
    [5, 12, 3],
    [7, 20, 6]
]

total = 0

for estante in inventario:
    for cantidad in estante:
        if cantidad > 5 and cantidad % 2 == 0:
            total += cantidad

print("Total de frutas:", total)