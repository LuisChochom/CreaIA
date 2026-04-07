cliente = {
    "nombre":"Luis",
    "edad":25,
    "Ciudad": "Xela"
}

print(f"Nombre:{cliente['nombre']} Edad:{cliente['edad']} años Ciudad:{cliente['Ciudad']} ")
print(cliente)
cliente["Ciudad"] = "San Marcos"
cliente["edad"] += 1
print(cliente)

#print(f"Nombre:{cliente['nombre']} Edad:{cliente['edad']} años Ciudad:{cliente['Ciudad']} ")