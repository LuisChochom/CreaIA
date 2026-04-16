from abc import ABC, abstractmethod
import random

# Clase Base Abstracta (Criterio 3 del enunciado)
class Pokemon(ABC):
    def __init__(self, nombre, hp_max, ep_max):
        self.nombre = nombre
        # Encapsulamiento: Uso de variables privadas con guion bajo (Criterio 6)
        self._hp_actual = hp_max
        self._hp_maximo = hp_max
        self._energia_actual = ep_max
        self._energia_maxima = ep_max
        self.bloqueo_activo = False

    # Uso de Decoradores @property y @setter (Criterio 6)
    @property
    def hp_actual(self):
        return self._hp_actual

    @hp_actual.setter
    def hp_actual(self, valor):
        # Lógica de Estado: No permite valores negativos (Criterio 7)
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

    # Método Abstracto: Obliga a las clases hijas a definir su ataque (Criterio 5)
    @abstractmethod
    def atacar(self, oponente):
        pass

    def defender(self):
        # Consume 5 EP y reduce daño a la mitad (Criterio 2)
        if self.energia_actual >= 5:
            self.energia_actual -= 5
            self.bloqueo_activo = True
            return True
        return False

    def descansar(self):
        # Restaura 20 EP (Criterio 2)
        self.energia_actual += 20

# --- Herencia y Polimorfismo (Los Linajes) ---

class PokemonFuego(Pokemon):
    def atacar(self, oponente):
        costo = 15
        if self.energia_actual < costo: return 0 # Valida EP (Criterio 7)
        self.energia_actual -= costo
        
        # Polimorfismo: Ventaja elemental usando isinstance() (Criterio 5)
        # Fuego inflige x2 contra Planta
        from pokemon_clases import PokemonPlanta
        multiplicador = 2 if isinstance(oponente, PokemonPlanta) else 1
        danio = 20 * multiplicador
        
        if oponente.bloqueo_activo:
            danio //= 2
            oponente.bloqueo_activo = False
            
        oponente.hp_actual -= danio
        return danio

class PokemonAgua(Pokemon):
    def atacar(self, oponente):
        costo = 15
        if self.energia_actual < costo: return 0
        self.energia_actual -= costo
        
        # Agua inflige x2 contra Fuego
        multiplicador = 2 if isinstance(oponente, PokemonFuego) else 1
        danio = 20 * multiplicador
        
        if oponente.bloqueo_activo:
            danio //= 2
            oponente.bloqueo_activo = False
            
        oponente.hp_actual -= danio
        return danio

class PokemonPlanta(Pokemon):
    def atacar(self, oponente):
        costo = 15
        if self.energia_actual < costo: return 0
        self.energia_actual -= costo
        
        # Planta inflige x2 contra Agua
        multiplicador = 2 if isinstance(oponente, PokemonAgua) else 1
        danio = 20 * multiplicador
        
        if oponente.bloqueo_activo:
            danio //= 2
            oponente.bloqueo_activo = False
            
        oponente.hp_actual -= danio
        return danio

class PokemonElectrico(Pokemon):
    def atacar(self, oponente):
        costo = 15
        if self.energia_actual < costo: return 0
        self.energia_actual -= costo
        
        danio = 20
        paralizado = False
        # 20% de probabilidad de paralizar (Criterio 2)
        if random.random() <= 0.20:
            paralizado = True
            
        if oponente.bloqueo_activo:
            danio //= 2
            oponente.bloqueo_activo = False
            
        oponente.hp_actual -= danio
        return danio, paralizado