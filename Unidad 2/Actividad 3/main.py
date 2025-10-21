class Tarea:
    def __init__(self, descripcion: str):
        self._descripcion = descripcion
        self._completado = False

    #Meotod publico para modificar el estado modificado
    def marcarCompletado(self):
        self._completado = True
        print(F"Tarea '{self._descripcion}' marcada como completado.")

    #Mostramos informacion de la tarea aqui se aplica el polimorfismo
    def mostrarInfo(self) -> str:
        estado = "Completado" if self._completado else "Pendinte"
        return f"[Tarea Normal0] {self._descripcion} - ({estado})"
    
    #Conversion del objeto tarea a JSON
    def toDict(self) -> dict:
        return {
            "tipo": "Tarea",
            "descripcion": self._descripcion,
            "completado": self._completado
        }
    

class TareaUrgente(Tarea):
    def __init__(self, descripcion: str, prioridad: str):
        super().__init__(descripcion)
        self._prioridad = prioridad

    #Sobreescrbimos el metodo mostrarInfo para mandare mensaje diferente
    def mostrarInfo(self) -> str:
        estado = "Completado" if self._completado else "Pendiente"
        return f"[Tarea Normal0] {self._descripcion} - ({estado}) - Prioridad: {self._prioridad}"
    
    #Sobreescritura del diccionario para incluir la prioridad
    def toDict(self):
        datos = super().toDict()
        datos["tipo"] = "TareaUrgente"
        datos["prioridad"] = self._prioridad
        return datos



    
