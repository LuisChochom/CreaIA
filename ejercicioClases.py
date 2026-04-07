class AireAcondicionado:
    def __init__(self):
        self.temperatura = 24

    def bajar_grados(self, grados):
        self.grados = grados
        if self.grados < 16:
            print(f"[ERROR]: La grados es de: {grados}, no debe ser menos de 16 grados.")
        else:
            print(f"[SISTEMA]: La grados es de: {grados}. Estado optimo.")

temp = AireAcondicionado()

while True:
    grados = int(input("Ingrese la grados que desea en el aire acondicionado: "))
    temp.bajar_grados(grados)