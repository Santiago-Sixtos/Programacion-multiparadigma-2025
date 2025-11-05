"""
Modulo de modelos:

Contiene las clases de entidad que definien la estructura 
de los datos principales del sistema

"""

class ItemBiblioteca:
    #Inicializacion el item
    def __init__(self, titulo: str):
        self._titulo = titulo
        self._estado = "disponible"
    
    def mostrarInfo(self) -> str:
        return f"[{self._titulo}] - Estado: {self.mostrarInfo}"
    
    #Convertir objeto a diccionario para guardarlo como JSON
    def toDict(self) -> dict:
        return {
            "titulo": self._titulo,
            "estado": self._estado,
            "tipo": "Item"
        }
    
class Libro(ItemBiblioteca):
    #Inicializacion el nuevo libro
    def __init__(self, titulo: str, autor: str, año: int):
        super().__init__(titulo)
        self._autor = autor
        self._año = año
    
    def mostrarInfo(self) -> str:
        return (f"[Libro] {self._titulo} escrito por {self._autor} [{self._año}]" f"- Estado: {self._estado}")
    
    #Sobreescribir el diccionario
    def toDict(self) -> dict:

        datos = super().toDict()

        datos ["tipo"] = "Libro"
        datos ["autor"] = self._autor
        datos ["año"] = self._año
        return datos

class Usuario: 
    #Inicializacion del nuevo usuarios
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._librosPrestados = []

    