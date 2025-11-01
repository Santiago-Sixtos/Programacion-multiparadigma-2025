# Proyecto: Gestor de Tareas Modular (POO)

Este proyecto es un sistema de gestión de tareas por consola desarrollado en Python. Su objetivo principal es aplicar los principios de la Programación Orientada a Objetos (POO) y una arquitectura de software modular.

## Propósito del Programa

El programa permite a un usuario gestionar una lista de tareas personales. Las funcionalidades incluyen:

- Agregar tareas normales y tareas urgentes (con prioridad).
- Listar todas las tareas pendientes y completadas.
- Marcar tareas como completadas.
- Eliminar tareas.
- Guardar la lista de tareas en un archivo `misTareas.json` para que los datos persistan entre sesiones.

## Cómo Ejecutar el Proyecto

1.  Asegúrate de tener Python 3.10 o superior instalado.
2.  Clona este repositorio en tu máquina local.
3.  Abre una terminal y navega hasta la carpeta raíz del proyecto (ej. `GestorTareasModular/`).
4.  Ejecuta el programa usando el siguiente comando:

    ```bash
    python main.py
    ```

5.  El menú interactivo te guiará. El archivo `misTareas.json` se creará automáticamente en la misma carpeta.

## Descripción de los Módulos

El proyecto está organizado en un paquete principal llamado `modulos` para separar las responsabilidades del código:

- **`main.py`**: Es el punto de entrada del programa. Contiene únicamente el bucle interactivo (`while True`) que maneja las opciones del usuario. Importa clases y funciones de los otros módulos para hacer el trabajo.

- **`modulos/modelo.py`**: Contiene toda la lógica de negocio y las estructuras de datos.

  - **Clase `Tarea`**: La clase base para una tarea.
  - **Clase `TareaUrgente`**: Hereda de `Tarea` y añade la lógica de prioridad.
  - **Clase `GestorTareas`**: El "cerebro" que maneja la lista de tareas, incluyendo los métodos para cargar y guardar en JSON.

- **`modulos/utilidades.py`**: Contiene funciones auxiliares que ayudan a mantener limpio el archivo `main.py`.
  - `mostrarMenu()`: Imprime el menú de opciones en la consola.
  - `pedirIndiceTarea()`: Maneja de forma segura la entrada del usuario cuando se le pide un número, controlando los `ValueError`.
