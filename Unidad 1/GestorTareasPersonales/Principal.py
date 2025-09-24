#lIbrerias utilizadas
import json

def cargarTareas():
    #Verificacion de la existencia del archivo JSON
    try:
        with open('tareas.json', 'r') as archivo: 
            return json.load(archivo)
    except FileNotFoundError:
        #Si el archivo no existe, se crea
        return []
    
def guardarTareas(lista_de_tareas):
    #Abrimos el archivo y escribimos en el "w"
    with open('tareas.json', 'w') as archivo:
        return json.dump(lista_de_tareas, archivo, indent=4)
    
def agragarTareas(tareas):
    descripcion = input("Esriba la nueva tarea:")

    #Creamos un diccionario para la nueva tarea
    nueva_tarea = {
        "descripcion": descripcion,
        "estado": "pendiente"
    }

    #Agregamos la tarea
    tareas.append(nueva_tarea)
    print("Tarea agregada con exito!")
    return tareas

def listarTareas(tareas):
    print("\n--- TAREAS PENDIENTES ---")
    
    if not tareas:
        print("¡Sin tareas pendientes! Agrega una para empezar.")
        return
    
    print
   