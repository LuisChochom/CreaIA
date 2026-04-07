class Camion():
    pass

class CentroLogistico():
    pass

camion1 = Camion()
camion2 = Camion()
camion3 = Camion()
camion4 = Camion()
camion5 = Camion()

garaje_principal = [camion1, camion2, camion3, camion4, camion5]
print("-"*50)
impuesto_total = len(garaje_principal) * 500
print(f"Impuesto total: {impuesto_total}")
print("-"*50)

for i in garaje_principal:
    print(f"El ID del camion es: {id(i)} ")
print("-"*50)

if len(garaje_principal) > 4:
    print("Capacidad excedida! Debes mover camiones a otra sucursal.")
    print("-"*50)
else:
    print("Capacidad optima.")
    print("-"*50)