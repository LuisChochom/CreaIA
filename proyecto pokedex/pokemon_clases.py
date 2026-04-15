import random

class Pokemon:
    def __init__(self, nombre, hp_max, ep_max):
        self.nombre = nombre
        # Encapsulamiento: Atributos privados
        self._hp_maximo = hp_max
        self._hp_actual = hp_max
        self._energia_maxima = ep_max
        self._energia_actual = ep_max
        self.defendiendo = False

    @property
    def hp_actual(self):
        return self._hp_actual

    @hp_actual.setter
    def hp_actual(self, valor):
        # Lógica de estado: El HP nunca es negativo
        if valor < 0:
            self._hp_actual = 0
        elif valor > self._hp_maximo:
            self._hp_actual = self._hp_maximo
        else:
            self._hp_actual = valor

    @property
    def energia_actual(self):
        return self._energia_actual

    @energia_actual.setter
    def energia_actual(self, valor):
        if valor < 0:
            self._energia_actual = 0
        elif valor > self._energia_maxima:
            self._energia_actual = self._energia_maxima
        else:
            self._energia_actual = valor

    def atacar(self, oponente):
        # Polimorfismo: Se sobrescribe en las clases hijas
        pass

    def defender(self):
        # Consume 5 EP y reduce daño del siguiente ataque a la mitad 
        if self.energia_actual >= 5:
            self.energia_actual -= 5
            self.defendiendo = True
            return True
        return False

    def descansar(self):
        # Restaura 20 EP
        self.energia_actual += 20

# --- Linajes Elementales (Herencia y Polimorfismo) ---

class PokemonFuego(Pokemon):
    def atacar(self, oponente):
        if self.energia_actual < 15: return 0
        self.energia_actual -= 15
        danio = 30 if isinstance(oponente, PokemonPlanta) else 20 # Fuego > Planta
        if oponente.defendiendo:
            danio //= 2
            oponente.defendiendo = False
        oponente.hp_actual -= danio
        return danio

class PokemonAgua(Pokemon):
    def atacar(self, oponente):
        if self.energia_actual < 15: return 0
        self.energia_actual -= 15
        danio = 30 if isinstance(oponente, PokemonFuego) else 20 # Agua > Fuego 
        if oponente.defendiendo:
            danio //= 2
            oponente.defendiendo = False
        oponente.hp_actual -= danio
        return danio

class PokemonPlanta(Pokemon):
    def atacar(self, oponente):
        if self.energia_actual < 15: return 0
        self.energia_actual -= 15
        danio = 30 if isinstance(oponente, PokemonAgua) else 20 # Planta > Agua 
        if oponente.defendiendo:
            danio //= 2
            oponente.defendiendo = False
        oponente.hp_actual -= danio
        return danio

class PokemonElectrico(Pokemon):
    def atacar(self, oponente):
        if self.energia_actual < 15: return 0
        self.energia_actual -= 15
        danio = 20 # Eléctrico daño normal 
        if random.random() <= 0.20: # 20% Probabilidad de paralizar
            print(f"¡{oponente.nombre} ha sido paralizado!")
        if oponente.defendiendo:
            danio //= 2
            oponente.defendiendo = False
        oponente.hp_actual -= danio
        return danio