#Librerias
import json
import os

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

class GestorTareas: 
    def __init__(self, archivoJason: str = "tareas.json"):
        self._tareas = []
        self._archivos_json = archivoJason

    def agregarTarea(self, tarea: Tarea):
        if isinstance(tarea, Tarea):
            self._tareas.append(tarea)
            print("Tarea agregada exitosamente")
        else:
            print("Error del sistema: Solo se pueden agregar objetos de tipo tarea")
    
    def listarTareas(self):
        if not self._tareas:
            print("No hay tareas registradas")
            return
        
        print("LISTADO DE TAREAS")
        for i, tarea in enumerate(self._tareas):
            print(f"{i + 1}. {tarea.mostrarInfo()}")
        print("==================")

    def marcarTareaCompletada(self, indice: int):
        try:
            tarea = self._tareas[indice]
            tarea.marcarCompletado()
        except IndexError:
            print(f"Error: indice {indice + 1} fuera de rango")
        except Exception as e:
            print(f"Error: {e}")

    def eliminarTarea(self, indice: int):
        try:
            tareaEliminado = self._tareas.pop(indice)
            print(f"Tarea '{tareaEliminado._descripcion}' eliminada")
        except IndexError:
            print(f"Error: indice {indice + 1} fuera de rango")

    #Metodos de persistencia sobre el json
    def guardarJson(self):
        listaParaGuardar = [tarea.toDict() for tarea in self._tareas]

        try:
            with open(self._archivos_json, 'w', encoding='utf-8') as f:
                      json.dump(listaParaGuardar, f, indent=4, ensure_ascii = False)
            print("Tarea guardada en", self._archivos_json)
        except IOError as e:
            print(f"Error al guardar archivo: {e}")
    
    def cargarJson(self):
        if not os.path.exists(self._archivo_json):
            print("Archivo de tareas no encontrado. Empezando lista vacía.")
            return

        try:
            with open(self._archivo_json, 'r', encoding='utf-8') as f:
                listaDatos = json.load(f)
            
            self._tareas = []
            
            for datosTarea in listaDatos:
                tareaObj = None
                if datosTarea["tipo"] == "TareaUrgente":
                    tareaObj = TareaUrgente(datosTarea["descripcion"], datosTarea["prioridad"])
                elif datosTarea["tipo"] == "Tarea":
                    tareaObj = Tarea(datosTarea["descripcion"])
                
                if tareaObj:
                    if datosTarea["completada"]:
                        tareaObj.marcar_completada()
                    self._tareas.append(tareaObj)
                    
            print("Tareas cargadas desde", self._archivo_json)
        except json.JSONDecodeError:
            print(f"Error: El archivo '{self._archivo_json}' está corrupto o vacío.")
        except IOError as e:
            print(f"Error al cargar el archivo: {e}")



    
