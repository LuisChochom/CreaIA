class Empleado():
    pass

empleado_1 = Empleado()
empleado_2 = Empleado()
empleado_3 = Empleado()

empleado_1.nombre = "Luis"
empleado_1.cargo = "Gerente"
empleado_1.salario = 2500.00

empleado_2.nombre = "Carlos"
empleado_2.cargo = "Cajero"
empleado_2.salario = 2000.00

empleado_3.nombre = "Jose"
empleado_3.cargo = "Bodegero"
empleado_3.salario = 1500.00

print("Listado de empleados de MI TIENDITA")
print("-"*50)
print(f"Nombre: {empleado_1.nombre} Cargo: {empleado_1.cargo} Salario: {empleado_1.salario}")
print(f"Nombre: {empleado_2.nombre} Cargo: {empleado_2.cargo} Salario: {empleado_2.salario}")
print(f"Nombre: {empleado_3.nombre} Cargo: {empleado_3.cargo} Salario: {empleado_3.salario}")