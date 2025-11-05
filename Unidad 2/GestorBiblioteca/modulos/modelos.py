"""
Modulo de modelos:

Contiene las clases de entidad que definien la estructura 
de los datos principales del sistema

"""

class ItemBiblioteca:
    #Inicializamos el item
    def __init__(self, titulo: str):
        self._titulo = titulo
        self._estado = "disponible"
    
    def mostrarInfo(self) -> str:
        return f"[{self._titulo}] - Estado: {self.mostrarInfo}"
    
    #Convertimos el objeto a diccionarios para guardarlo como JSON
    def toDict(self) -> dict:
        return {
            "titulo": self._titulo,
            "estado": self._estado,
            "tipo": "Item"
        }
    
class Libro(ItemBiblioteca):
    #Inicializamos el nuevo libro
    def __init__(self, titulo: str, autor: str, año: int):
        super().__init__(titulo)
        self._autor = autor
        self._año = año
    
    def mostrarInfo(self) -> str:
        return (f"[Libro] {self._titulo} escrito por {self._autor} [{self._año}]" f"- Estado: {self._estado}")
    
    #Sobreescribimos el diccionario
    def toDict(self) -> dict:

        datos = super().toDict()

        datos ["tipo"] = "Libro"
        datos ["autor"] = self._autor
        datos ["año"] = self._año
        return datos
    