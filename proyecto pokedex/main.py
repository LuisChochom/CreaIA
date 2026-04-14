import random
from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
from pokemon_clases import PokemonFuego, PokemonAgua, PokemonPlanta, PokemonElectrico

def crear_pokemon(numero_seleccionado):
    # Instanciación Dinámica: Extrae datos y llama al constructor [cite: 65, 68]
    datos = CATALOGO_POKEMON[numero_seleccionado]
    tipo = datos["tipo"]
    nombre = datos["nombre"]
    hp = datos["hp_maximo"]
    ep = datos["energia_maxima"]

    if tipo == "Fuego": return PokemonFuego(nombre, hp, ep)
    if tipo == "Agua": return PokemonAgua(nombre, hp, ep)
    if tipo == "Planta": return PokemonPlanta(nombre, hp, ep)
    if tipo == "Electrico": return PokemonElectrico(nombre, hp, ep)

def obtener_accion(jugador_nombre, es_computadora=False):
    if es_computadora:
        return random.choice(["1", "2", "3"]) # Modo PvE usando random [cite: 40, 129]
    
    while True:
        print(f"\n1. Atacar (15 EP) | 2. Defender (5 EP) | 3. Descansar (+20 EP)")
        opcion = input(f"{jugador_nombre}, elija su acción: ")
        if opcion in ["1", "2", "3"]: return opcion
        print("Opción inválida.")

def batalla():
    print("--- SIMULADOR DE BATALLAS ---")
    try: # Manejo de errores en menús 
        modo = input("1. PvP | 2. PvE: ")
        mostrar_catalogo_disponible()
        
        p1_choice = input("Jugador 1, elija su Pokémon (número): ")
        p1 = crear_pokemon(p1_choice)
        
        if modo == "2":
            p2_choice = random.choice(list(CATALOGO_POKEMON.keys()))
            p2 = crear_pokemon(p2_choice)
            print(f"La computadora eligió a: {p2.nombre}")
        else:
            p2_choice = input("Jugador 2, elija su Pokémon (número): ")
            p2 = crear_pokemon(p2_choice)

        # Bucle de combate [cite: 121]
        while p1.hp_actual > 0 and p2.hp_actual > 0:
            # Turno P1
            accion = obtener_accion(p1.nombre)
            ejecutar_turno(p1, p2, accion)
            if p2.hp_actual <= 0: break
            
            # Turno P2
            accion_p2 = obtener_accion(p2.nombre, modo == "2")
            ejecutar_turno(p2, p1, accion_p2)

        ganador = p1.nombre if p1.hp_actual > 0 else p2.hp_actual
        print(f"\n¡{ganador} ha ganado la batalla!")

    except (ValueError, KeyError):
        print("Error: Ingrese un número válido del catálogo.")
        batalla()

def ejecutar_turno(atacante, defensor, accion):
    if accion == "1":
        danio = atacante.atacar(defensor)
        print(f"{atacante.nombre} atacó e infligió {danio} de daño.")
    elif accion == "2":
        atacante.defender()
        print(f"{atacante.nombre} se está defendiendo.")
    elif accion == "3":
        atacante.descansar()
        print(f"{atacante.nombre} ha descansado.")

if __name__ == "__main__":
    batalla()