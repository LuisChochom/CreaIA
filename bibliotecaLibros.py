class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

class Biblioteca:
    def __init__(self, nombre_sucursal):
        self.nombre_sucursal = nombre_sucursal
        self.catalogo = []
    
    def agregar_libro(self, nuevo_libro):
        self.catalogo.append(nuevo_libro)
        print(f"Libro agregado: {nuevo_libro}")
    
    def mostrar_inventario(self):
        print(f"Inventario de la biblioteca '{self.nombre_sucursal}':")
        for libro in self.catalogo:
            print(f"- {libro}")

biblioteca = Biblioteca("Central")
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")
libro3 = Libro("La Sombra del Viento", "Carlos Ruiz Zafón")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.mostrar_inventario()