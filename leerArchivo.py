lineas = 0
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        lineas = lineas + 1
print(f"El número de líneas en el archivo es: {lineas}")
