# matriz de precios
precios_pasillos = [
    [10.0, 55.0, 20.0],
    [45.0, 80.0, 12.0],
    [100.0, 30.0, 48.0]
]

incremento = 0.10

for i in range(len(precios_pasillos)):
    print(len(precios_pasillos))
    for j in range(len(precios_pasillos[i])):
        
        if precios_pasillos[i][j] < 50:
            precios_pasillos[i][j] += precios_pasillos[i][j] * incremento

print("Precios finales:")
for fila in precios_pasillos:
    print(fila)

print(len(precios_pasillos))