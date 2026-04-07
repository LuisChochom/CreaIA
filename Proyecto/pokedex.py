# ====================================================================
# ARCHIVO PROVISTO POR EL PROFESOR: pokedex.py
# ====================================================================
# Este archivo simula una base de datos. Contiene la información en crudo
# de los Pokémon disponibles. Usted debe importar este catálogo en su main.py
# y utilizar estos datos para instanciar sus objetos.
# ====================================================================

CATALOGO_POKEMON = {
    "1": {"tipo": "Fuego", "nombre": "Charmander", "hp_maximo": 100, "energia_maxima": 50},
    "2": {"tipo": "Fuego", "nombre": "Vulpix", "hp_maximo": 90, "energia_maxima": 60},
    "3": {"tipo": "Agua", "nombre": "Squirtle", "hp_maximo": 110, "energia_maxima": 45},
    "4": {"tipo": "Agua", "nombre": "Psyduck", "hp_maximo": 95, "energia_maxima": 55},
    "5": {"tipo": "Planta", "nombre": "Bulbasaur", "hp_maximo": 105, "energia_maxima": 50},
    "6": {"tipo": "Planta", "nombre": "Oddish", "hp_maximo": 90, "energia_maxima": 60},
    "7": {"tipo": "Electrico", "nombre": "Pikachu", "hp_maximo": 80, "energia_maxima": 70},
    "8": {"tipo": "Electrico", "nombre": "Magnemite", "hp_maximo": 75, "energia_maxima": 80}
}

def mostrar_catalogo_disponible():
    """
    Imprime en la consola el catálogo de Pokémon disponibles de forma tabulada.
    """
    print("\n" + "="*45)
    print("         CATÁLOGO POKÉMON OFICIAL")
    print("="*45)
    
    for clave, datos in CATALOGO_POKEMON.items():
        print(f"[{clave}] {datos['nombre']} | Tipo: {datos['tipo']} | HP: {datos['hp_maximo']} | EP: {datos['energia_maxima']}")
    
    print("="*45 + "\n")