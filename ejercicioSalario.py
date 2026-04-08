class Empleado:
    def __init__ (self, salario_inicial):
        self.__salario = salario_inicial #atributo privado
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, nuevo_salario):
        while nuevo_salario <= 300:
            print("Error: El nuevo salario debe ser mayor a 300. Por favor, ingrese un nuevo salario.")
            nuevo_salario = float(input("Ingrese el nuevo salario: "))
        
        self.__salario = nuevo_salario
        print(f"¡Salario actualizado! El nuevo salario es de: Q{self.__salario}")

empleado = Empleado(400)
print(f"Salario inicial: Q{empleado.salario}")
nuevo_salario = float(input("Ingrese el nuevo salario: "))
empleado.salario = nuevo_salario