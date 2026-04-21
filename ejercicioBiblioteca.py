class Libro:
    def __init__(self, titulo, autor, id_libro):
        self._titulo = titulo
        self._autor = autor
        self._id_libro = id_libro
        self._prestado = False

    # Getters y Setters con decoradores
    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def id_libro(self):
        return self._id_libro

    @property
    def prestado(self):
        return self._prestado

    @prestado.setter
    def prestado(self, valor):
        self._prestado = valor

    def marcar_como_prestado(self):
        self._prestado = True

#--- modelo ---
class Biblioteca:
    def __init__(self):
        self._libros = []

    @property
    def libros(self):
        return self._libros

    def agregar_libro(self, libro):
        self._libros.append(libro)

    def buscar_por_id(self, id_buscar):
        for libro in self._libros:
            if libro.id_libro == id_buscar:
                return libro
        return None
    
#--- vista ---
class VistaBiblioteca:
    def mostrar_menu(self):
        print("\n--- SISTEMA DE BIBLIOTECA ---")
        print("1. Añadir Libro")
        print("2. Listar Libros")
        print("3. Prestar Libro")
        print("4. Salir")
        return input("Seleccione una opción: ")

    def pedir_datos_libro(self):
        titulo = input("Ingrese el título: ")
        autor = input("Ingrese el autor: ")
        id_libro = input("Ingrese el ID: ")
        return titulo, autor, id_libro

    def mostrar_libros(self, lista_libros):
        print("\nID | Título | Autor | Estado")
        print("-" * 35)
        for libro in lista_libros:
            estado = "Prestado" if libro.prestado else "Disponible"
            print(f"{libro.id_libro} | {libro.titulo} | {libro.autor} | {estado}")

    def pedir_id_prestamo(self):
        return input("Ingrese el ID del libro a prestar: ")

    def mostrar_mensaje(self, mensaje):
        print(f">> {mensaje}")

#--- controlador ---    
class ControladorBiblioteca:
    def __init__(self, modelo_biblioteca, vista):
        self.modelo = modelo_biblioteca
        self.vista = vista

    def iniciar(self):
        opcion = ""
        while opcion != "4":
            opcion = self.vista.mostrar_menu()

            if opcion == "1":
                # Añadir libro
                t, a, i = self.vista.pedir_datos_libro()
                nuevo_libro = Libro(t, a, i)
                self.modelo.agregar_libro(nuevo_libro)
                self.vista.mostrar_mensaje("Libro añadido con éxito.")

            elif opcion == "2":
                # Listar libros
                todos_los_libros = self.modelo.libros
                self.vista.mostrar_libros(todos_los_libros)

            elif opcion == "3":
                # Prestar libro
                id_a_prestar = self.vista.pedir_id_prestamo()
                libro_encontrado = self.modelo.buscar_por_id(id_a_prestar)
                
                if libro_encontrado:
                    libro_encontrado.marcar_como_prestado()
                    self.vista.mostrar_mensaje("Libro marcado como prestado.")
                else:
                    self.vista.mostrar_mensaje("Error: ID no encontrado.")

            elif opcion == "4":
                self.vista.mostrar_mensaje("Saliendo del sistema...")
            else:
                self.vista.mostrar_mensaje("Opción no válida.")

# --- Bloque Principal ---
if __name__ == "__main__":
    modelo = Biblioteca()
    vista = VistaBiblioteca()
    controlador = ControladorBiblioteca(modelo, vista)
    controlador.iniciar()