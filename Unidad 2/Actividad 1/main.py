class Libro:
    #Atributo de la clase
    biblioteca = "Biblioteca Central"

    #Constructor
    def __init__(self, titulo:str, autor:str, añoPublicacion:int):
        self.titulo = titulo
        self.autor = autor
        self.añoPublicacion = añoPublicacion
        self.prestado = False

    #Funcion para prestar el libro
    def prestar(self):
        if self.prestado:
            print(f"El libro ", self.titulo, " ya ha sido prestado")
        else:
            self.prestado = True
            print(f"El libro ", self.titulo, " ha sido prestado")
    
    #Funcion para devolver el libro
    def devolver(self):
        if not self.prestado:
            print(f"El libro ", self.titulo, " ya se encontraba disponible")
        else:
            self.prestado = False
            print(f"El libro ", self.titulo," ha sido devuelto")

    def mostrarEstado(self):
        #Determinamos el estado del libro
        estadoActual = "Prestado" if self.prestado else "Disponible"

        #Informacion del libro
        print("\n-------------------------")
        print(f"     FICHA DEL LIBRO     ")
        print("-------------------------")
        print(f"Título: ", self.titulo)
        print(f"Autor: ", self.autor)
        print(f"Año de Publicación: ", self.añoPublicacion)
        print(f"Estado: ", estadoActual)
        print(f"Ubicación: ", Libro.biblioteca)
        print("-------------------------")

if __name__ == "__main__":

    #Instancia de 3 objetos
    print("Creando catalogo de libros")
    libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 1943)
    libro2 = Libro("El señor de los anillos", "J.R.R Tolkien", 1954)
    libro3 = Libro("La sombra del viento", "Carlos Ruiz Zafon", 2001)
    print("Catalogo de libros creados")

    print("==================================================")

    #Estado inicial de todos los libros
    print("Estado inicial de los libros")
    libro1.mostrarEstado()
    libro2.mostrarEstado()
    libro3.mostrarEstado()

    print("==================================================")

    #Acciones de prestar y devolver
    print("Acciones de biblioteca")
    libro2.prestar()
    libro3.prestar()
    libro2.devolver()

    #Prueba de prestar un libro que ya se presto
    libro3.prestar()

    print("==================================================")

    #Mostramos estado final de todos los libros
    print("Estado final de los libros")
    libro1.mostrarEstado()
    libro2.mostrarEstado()
    libro3.mostrarEstado()