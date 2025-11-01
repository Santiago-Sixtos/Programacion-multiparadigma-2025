def mostrarMenu():
    #Menu principal
    print("\n--- SISTEMA GESTOR DE TAREA ---")
    print("1. Agregar tarea normal")
    print("2. Agregar tarea urgente")
    print("3. Listar tareas")
    print("4. Marcar tarea como completada")
    print("5. Eliminar tarea")
    print("6. Guardar y salir")

def pedirIndiceTarea(accion: str) -> int | None:
    #Solicitud del usuario del indice de la tarea
    try:
        idx_str = input(f"Ingresa el número de la tarea a {accion}: ")
        idx_int = int(idx_str)
        return idx_int - 1
    except ValueError:
        print("Error: Debes ingresar un número.")
        return None