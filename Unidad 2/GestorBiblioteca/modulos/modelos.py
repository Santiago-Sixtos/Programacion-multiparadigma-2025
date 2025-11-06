"""
Modulo de modelos:

Contiene las clases de entidad que definien la estructura 
de los datos principales del sistema

"""

class ItemBiblioteca:
    #Inicializacion del item
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
    #Inicializacion del nuevo libro
    def __init__(self, titulo: str, autor: str, año: int):
        super().__init__(titulo)
        self._autor = autor
        self._año = año
    
    def mostrarInfo(self) -> str:
        return (f"[Libro] {self._titulo} escrito por {self._autor} [{self._año}]" f"- Estado: {self._estado}")
    
    #Sobreescribir del diccionario
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

    def mostrarInfo(self) -> str:
        if not self._librosPrestados:
            return f"Usuario: {self._nombre} no tiene libros prestados."
        
        titulos = ", ".join(self._librosPrestados)
        return f"Usuario: {self._nombre} tiene {titulos}"
    
    #Se convierte el objeto 'Usuario' a un  diccionario para JSON
    def toDict(self) -> dict:
        return {
            "nombre": self._nombre,
            "libros_prestados": self._librosPrestados
        }