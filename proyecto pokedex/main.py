import random
from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
from pokemon_clases import PokemonFuego, PokemonAgua, PokemonPlanta, PokemonElectrico

def crear_objeto_pokemon(id_catalogo):
    # Instanciación Dinámica: Extrae datos y llama al constructor (Criterio 4)
    datos = CATALOGO_POKEMON[id_catalogo]
    tipo = datos["tipo"]
    n, h, e = datos["nombre"], datos["hp_maximo"], datos["energia_maxima"]
    
    if tipo == "Fuego": return PokemonFuego(n, h, e)
    elif tipo == "Agua": return PokemonAgua(n, h, e)
    elif tipo == "Planta": return PokemonPlanta(n, h, e)
    elif tipo == "Electrico": return PokemonElectrico(n, h, e)

def ejecutar_simulacion():
    print("===== SIMULADOR DE BATALLAS POKÉMON (POO) =====")
    try: # Manejo de Errores (Criterio 75, pág 4)
        print("1. Jugador vs Jugador\n2. Jugador vs Computadora")
        modo = input("> Opción: ")
        
        mostrar_catalogo_disponible()
        
        p1_idx = input("Jugador 1, elija el número de su Pokémon: ")
        p1 = crear_objeto_pokemon(p1_idx)
        print(f"¡Has seleccionado a {p1.nombre}!")

        if modo == "2":
            p2_idx = random.choice(list(CATALOGO_POKEMON.keys()))
            p2 = crear_objeto_pokemon(p2_idx)
            print(f"¡La computadora ha seleccionado a {p2.nombre}!")
        else:
            p2_idx = input("Jugador 2, elija el número de su Pokémon: ")
            p2 = crear_objeto_pokemon(p2_idx)

        # Ciclo de Combate
        while p1.hp_actual > 0 and p2.hp_actual > 0:
            # Turno Jugador 1
            print(f"\n--- TURNO DE {p1.nombre} ---")
            procesar_turno(p1, p2)
            if p2.hp_actual <= 0: break

            # Turno Jugador 2 o Computadora (Criterio 8)
            print(f"\n--- TURNO DE {p2.nombre} ---")
            if modo == "2":
                accion_ia = random.choice(["1", "2", "3"])
                ejecutar_accion(p2, p1, accion_ia)
            else:
                procesar_turno(p2, p1)

        ganador = p1.nombre if p1.hp_actual > 0 else p2.nombre
        print(f"\n¡{ganador.upper()} ES EL VENCEDOR!")

    except (ValueError, KeyError):
        print("\n[ERROR] Entrada no válida. Use solo números del catálogo.")
        ejecutar_simulacion()

def procesar_turno(atacante, defensor):
    print(f"[{atacante.nombre}] HP: {atacante.hp_actual} | EP: {atacante.energia_actual}")
    print("1. Atacar | 2. Defender | 3. Descansar")
    accion = input("> Elija acción: ")
    ejecutar_accion(atacante, defensor, accion)

def ejecutar_accion(p_activo, p_objetivo, accion):
    if accion == "1":
        resultado = p_activo.atacar(p_objetivo)
        # Manejo especial para el tipo Eléctrico y su parálisis
        if isinstance(resultado, tuple):
            danio, paraliza = resultado
            print(f"¡{p_activo.nombre} ataca! Daño: {danio}. {'¡PARALIZADO!' if paraliza else ''}")
        else:
            print(f"¡{p_activo.nombre} ataca e inflige {resultado} de daño!")
    elif accion == "2":
        if p_activo.defender():
            print(f"{p_activo.nombre} se pone en guardia.")
        else:
            print(f"¡{p_activo.nombre} no tiene energía para defender!")
    elif accion == "3":
        p_activo.descansar()
        print(f"{p_activo.nombre} está descansando para recuperar EP.")

if __name__ == "__main__":
    ejecutar_simulacion()