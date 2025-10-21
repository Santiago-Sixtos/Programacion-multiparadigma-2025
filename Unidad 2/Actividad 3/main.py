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
        estado = "Completado" if self._completado else "Pendiente"
        return f"[Tarea Normal] {self._descripcion} - ({estado})"
    
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
        return f"[Tarea Urgente] {self._descripcion} - ({estado}) - Prioridad: {self._prioridad}"
    
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
        
        print("==================")
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
        if not os.path.exists(self._archivos_json):
            print("Archivo de tareas no encontrado. Empezando lista vacía.")
            return

        try:
            with open(self._archivos_json, 'r', encoding='utf-8') as f:
                listaDatos = json.load(f)
            
            self._tareas = []
            
            for datosTarea in listaDatos:
                tareaObj = None
                if datosTarea["tipo"] == "TareaUrgente":
                    tareaObj = TareaUrgente(datosTarea["descripcion"], datosTarea["prioridad"])
                elif datosTarea["tipo"] == "Tarea":
                    tareaObj = Tarea(datosTarea["descripcion"])
                
                if tareaObj:
                    if datosTarea["completado"]:
                        tareaObj.marcarCompletada()
                    self._tareas.append(tareaObj)
                    
            print("Tareas cargadas desde", self._archivos_json)
        except json.JSONDecodeError:
            print(f"Error: El archivo '{self._archivo_json}' está corrupto o vacío.")
        except IOError as e:
            print(f"Error al cargar el archivo: {e}")

#Funcion principal
def main():
    gestor = GestorTareas(archivoJason="misTareas.json")
    gestor.cargarJson()

    while True:
        print("=========================")
        print("SISTEMA GESTOR DE TAREA")
        print("1. Agregar tarea normal")
        print("2. Agregar tarea urgente")
        print("3. Listar tareas")
        print("4. Marcar tarea como completada")
        print("5. Eliminar tarea")
        print("6. Guardar y salir")
        print("========================")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            desc = input("Descripcion de la tarea: ")
            gestor.agregarTarea(Tarea(desc))

        elif opcion == "2":
            desc = input("Descripcion de la tarea urgente: ")
            prioridad = input("Nivel de prioridad. Ej. Alta, media o baja: ")
            gestor.agregarTarea(TareaUrgente(desc, prioridad))
        
        elif(opcion == "3"):
            gestor.listarTareas()

        elif(opcion == "4"):
            gestor.listarTareas()

            try:
                idx = int(input("Ingresa el numero de la tarea a completar: "))
                gestor.marcarTareaCompletada(idx - 1)
            except ValueError:
                print("Error: Favor de ingresar un numero")
            
        elif opcion == "5":
            gestor.listarTareas()

            try:
                idx = int(input("Ingrese el numero que desee elimnar: "))
                gestor.eliminarTarea(idx - 1)
            except ValueError:
                print("Error: Debes ingresar un numero")
        
        elif opcion == "6":
            gestor.guardarJson()
            print("Gracias por usar el gestor de tareas.")
            break

if __name__ == "__main__":
    main()


    
