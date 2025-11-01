# Importamos las clases y funciones desde nuestros módulos
from modulos.modelo import GestorTareas, Tarea, TareaUrgente
from modulos.utilidades import mostrarMenu, pedirIndiceTarea

def main():
    #Instancia del gestor
    gestor = GestorTareas(archivoJason="misTareas.json")
    gestor.cargarJson()

    while True:
        # Menu pero ahora ddesde utilidades
        mostrarMenu()
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            desc = input("Descripción de la tarea: ")
            gestor.agregarTarea(Tarea(desc))

        elif opcion == "2":
            desc = input("Descripción de la tarea urgente: ")
            prioridad = input("Nivel de prioridad (Ej. Alta, Media, Baja): ")
            gestor.agregarTarea(TareaUrgente(desc, prioridad))
        
        elif opcion == "3":
            gestor.listarTareas()

        elif opcion == "4":
            gestor.listarTareas()
            #Funcion desde la utilidad
            idx = pedirIndiceTarea(accion="completar")
            if idx is not None:
                gestor.marcarTareaCompletada(idx)
                
        elif opcion == "5":
            gestor.listarTareas()
            #Reutilizamos la funcion de utilidad
            idx = pedirIndiceTarea(accion="eliminar")
            if idx is not None:
                gestor.eliminarTarea(idx)
        
        elif opcion == "6":
            gestor.guardarJson()
            print("Gracias por usar el gestor de tareas.")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Punto de entrada 
if __name__ == "__main__":
    main()