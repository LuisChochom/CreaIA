class PersonajeBase:
    def camniar(self):
        print("El personaje esta avanzando por el mapa...")
    
    def descansar(self):
        print("El personaje esta recuperando energia...")

class Mago(PersonajeBase):
    def lanzar_hechizo(self):
        print("El mago lanza una bola de fuego!")

class Guerrero(PersonajeBase):
    def bloquear_ataque(self):
        print("El guerrero levanta su escudo de metal.")

mi_mago = Mago()
mi_gerrero = Guerrero()

mi_mago.camniar()
mi_mago.descansar()
mi_gerrero.camniar()
mi_gerrero.descansar()
mi_mago.lanzar_hechizo()
mi_gerrero.bloquear_ataque()
mi_gerrero.lanzar_hechizo()