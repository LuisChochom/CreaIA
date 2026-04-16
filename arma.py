class Arma:
    def __init__(self, nombre, puntos_dano):
        self.nombre = nombre
        self.puntos_dano = puntos_dano

class Guerrero:
    def __init__(self, nombre, arma_quipada):
        self.nombre = nombre
        self.arma = arma_quipada

    def atacar(self):
        print(f"{self.nombre} ataca con {self.arma.nombre} causando {self.arma.puntos_dano} puntos de daño.")
    
espada = Arma("Espada Larga", 50)
guerrero = Guerrero("Conan", espada)
guerrero.atacar()