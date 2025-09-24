#lIbrerias utilizadas
import json

#Metodos definidos 
def cargarTareas():
    #Verificacion de la existencia del archivo JSON
    try:
        with open('tareas.json', 'r') as archivo: 
            return json.load(archivo)
    except FileNotFoundError:
        #Si el archivo no existe, se crea
        return []
    
def guardarTareas(listaDeTareas):
    #Abrimos el archivo y escribimos en el "w"
    with open('tareas.json', 'w') as archivo:
        return json.dump(listaDeTareas, archivo, indent=4)
    
def agregarTareas(tareas):
    descripcion = input("Esriba la nueva tarea:")

    #Creamos un diccionario para la nueva tarea
    nuevaTarea = {
        "descripcion": descripcion,
        "estado": "pendiente"
    }

    #Agregamos la tarea
    tareas.append(nuevaTarea)
    print("Tarea agregada con exito!")
    return tareas

def listarTareas(tareas):
    print("\n--- TAREAS PENDIENTES ---")
    
    if not tareas:
        print("¡Sin tareas pendientes! Agrega una para empezar.")
        return
    
    #Imprimimos el encabezado
    print(f"{'No.':<5} | {'Descripicion':<30} | {'Estado'}")
    print("-" * 50)

    #Iteramos sobre la lista para imprimir cada tarea con su numero
    for t, tareas in enumerate(tareas, start=1):
        print(f"{t:<5} | {tareas['descripcion']:<30} | {tareas['estado']}")
    
    print("-" * 50)
   
def marcarTarea(tareas):
    #Mostramos las tareas disponibles a elegir
    listarTareas(tareas)

    #Sin tareas no se puede marcar tareas
    if not tareas: 
        return tareas
    
    try:
        numTareas = int(input("Ingrese el numero de la tarea a completar"))

        #Indice de la tarea a completar
        indice = numTareas - 1

        #Validamos que el indice este dentro del rango
        if 0 <= indice < len(tareas):
            tareas[indice]["estado"] = "completada"
            print(f"Tarea '{tareas[indice]['descripcion']}' ha sido marcada como completada.")
        else:
            print("Numero de tarea no valido")

    except ValueError:
        print("Entrada no valida. Favor de ingresar un numero valido.")

    return tareas

def eliminarTarea(tareas):
    listarTareas(tareas)

    if not tareas:
        return tareas
    
    try:
        numTarea = int(input("Ingrese el numero de la tarea que desea eliminar: "))

        indice = numTarea - 1

        if 0 <= indice < len(tareas):
            tareaEliminada = tareas[indice]['descripcion']
            tareas.pop(indice)

            print(f"Tarea '{tareaEliminada}' ha sido eliminada con exito. ")
        else:
            print("Numero de tarea no valido")
    except ValueError:
        print("Entrada no valida. Favor de ingresar otro numero.")

    return tareas