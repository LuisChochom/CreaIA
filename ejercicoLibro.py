class LibroFisico:
    # 1. el constructor pido solamente lo esencial de afuera
    def __init__(self, titulo, autor, precio=100):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        # 2. Atributo interno, por defecto siempre inicia en True
        self.disponible = True

    # 3. un método de la clase
    def prestar_libro(self):
        # if self.disponible == False:  > False == False > True 
        if not self.disponible: # not False > True 
            print(f"El libro: {self.titulo} no está disponible") 
        else:
            print(f"Libro: {self.titulo} disponible! Libro prestado y su precio es {self.precio}")
            self.disponible = False

libro1 = LibroFisico("El Quijote", "Miguel de Cervantes", 200) 
libro2 = LibroFisico("Cien años de soledad", "Gabriel García Márquez")
# intento 1
libro1.prestar_libro() # Libro disponible! Libro prestado

# intento 2
libro1.prestar_libro() # El libro no está disponible

libro2.prestar_libro() # Libro disponible! Libro prestado