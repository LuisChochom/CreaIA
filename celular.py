class Bateria():
    def __init__ (self, porcentaje=100):
        self.porcentaje = porcentaje
    
    def descargar(self, cantidad):
        self.porcentaje -= cantidad
        if self.porcentaje < 0:
            self.porcentaje = 0
    
class Celular():
    def __init__ (self, marca):
        self.marca = marca
        self.bateria = Bateria()
    
    def usar_app(self):
        self.bateria.descargar(10)
        print(f"Abriendo aplicación... en el celular {self.marca}")
        print(f"Batería restante: {self.bateria.porcentaje}%")

celular = Celular("Apple")
celular.usar_app()
celular.usar_app()
celular.usar_app()
celular.usar_app()