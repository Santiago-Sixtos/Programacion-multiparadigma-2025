class Libro:
    #Constructor
    def __init__(self, titulo:str, autor:str, añoPublicacion:int, prestado:bool):
        self.titulo = titulo
        self.autor = autor
        self.añoPublicacion = añoPublicacion
        self.prestado = False

    def prestado(self):
        if self.prestado:
            print(f"El libro ", self.titulo, " esta disponible")
        else:
            self.prestado = True
            print(f"El libro", self.titulo, " ha sido prestado")
    
    def devolver(self):
        if not self.prestado:
            print(f"El libro", self.titulo, " ha sido devuelto")
        else:
            self.titulo = False
            print(f"El libro", self.titulo," ya se encontraba disponible")