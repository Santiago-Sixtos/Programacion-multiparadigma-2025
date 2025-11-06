"""
Modulo principal

Punto de entrada del sistema de gestion de biblioteca.
Contiene el menu interactivo y coordina las llamadas a la clase biblioteca.
"""

#Importamos las clases necesarias desde nuestros modulos
from modulos.modelos import Libro, Usuario
from modulos.biblioteca import Biblioteca

def mostrarMenu():
    print("\n=== Gestión de Biblioteca ===")
    print("1. Agregar nuevo libro")
    print("2. Registrar nuevo usuario")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Mostrar libros disponibles")
    print("6. Mostrar todos los libros")
    print("7. Mostrar todos los usuarios")
    print("8. Guardar y Salir")
    print("===============================")

def main():
    miBiblioteca = Biblioteca(nombreArchivo = "bibliotecaDatos.json")
    miBiblioteca.cargarDatos()

    while True:
        mostrarMenu()
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            print("\n[Agregar Nuevo Libro]")
            titulo = input("Título: ")
            autor = input("Autor: ")

            try:
                año = int(input("Año de publicación: "))
                libro = Libro(titulo, autor, año)
                miBiblioteca.agregarLibro(libro)

            except ValueError:
                print("Error: El año debe ser un número.")

        elif opcion == "2":
            print("\n[Registrar Nuevo Usuario]")
            nombre = input("Nombre de usuario: ")
            usuario = Usuario(nombre)
            miBiblioteca.agregarUsuario(usuario)

        elif opcion == "3":
            print("\n[Prestar Libro]")
            nombreUsuario = input("Nombre de usuario: ")
            tituloLibro = input("Título del libro: ")
            miBiblioteca.prestarLibro(nombreUsuario, tituloLibro)

        elif opcion == "4":
            print("\n[Devolver Libro]")
            nombreUsuario = input("Nombre de usuario: ")
            tituloLibro = input("Título del libro: ")
            miBiblioteca.devolverLibro(nombreUsuario, tituloLibro)

        elif opcion == "5":
            miBiblioteca.mostrarLibrosDisponibles()
            
        elif opcion == "6":
            print("\n--- Catálogo Completo de Libros ---")

            if not miBiblioteca._libros:
                print("No hay libros en el catálogo.")

            for libro in miBiblioteca._libros.values():
                print(f"  - {libro.mostrarInfo()}")
            print("-" * 34)
            
        elif opcion == "7":
            print("\n--- Lista Completa de Usuarios ---")

            if not miBiblioteca._usuarios:
                print("No hay usuarios registrados.")

            for usuario in miBiblioteca._usuarios.values():
                print(f"  - {usuario.mostrarInfo()}")
            print("-" * 33)

        elif opcion == "8":
            print("Guardando datos antes de salir...")
            miBiblioteca.guardarDatos()
            print("Gracias por usar el gestor de biblioteca")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
if __name__ == "__main__":
    main()