# Gestor de Tareas Personales

Este es un sencillo gestor de tareas desarrollado en Python, que se ejecuta en la terminal. Permite a los usuarios administrar sus tareas diarias de una manera eficiente, guardando toda la información de forma persistente en un archivo `tareas.json`.

El programa está desarrollado siguiendo el paradigma de **programación imperativa**.

## Características

- **Agregar Tarea**: Permite añadir nuevas tareas a la lista.
- **Listar Tareas**: Muestra todas las tareas pendientes y completadas en un formato de tabla claro.
- **Marcar tarea como Completada**: Permite cambiar el estado de una tarea de "pendiente" a "completada".
- **Eliminar Tarea**: Elimina permanentemente una tarea de la lista.
- **Persistencia de Datos**: Todas las tareas se guardan en el archivo `tareas.json`, por lo que no se pierden al cerrar el programa.

## Requisitos

- Python 3.x

## Instrucciones de Ejecución

1.  Asegúrate de tener Python 3 instalado en tu sistema.
2.  Coloca el archivo `Principal.py` en una carpeta.
3.  Abre una terminal o línea de comandos.
4.  Navega hasta la carpeta donde guardaste el archivo usando el comando `cd`.
    ```bash
    cd ruta/a/tu/carpeta/GestorTareasPersonales
    ```
5.  Ejecuta el programa con el siguiente comando:
    ```bash
    python Principal.py
    ```
6.  El programa se iniciará y el archivo `tareas.json` se creará automáticamente en la misma carpeta la primera vez que agregues una tarea.

---

## Ejemplo de Uso

```console
--- Gestor de Tareas ---
1. Agregar tarea
2. Listar tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir
Selecciona una opción: 1
Escribe la nueva tarea: Preparar la presentación para el viernes
Tarea agregada con exito!

--- Gestor de Tareas ---
1. Agregar tarea
2. Listar tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir
Selecciona una opción: 1
Escribe la nueva tarea: Comprar leche
Tarea agregada con exito!

--- Gestor de Tareas ---
1. Agregar tarea
2. Listar tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir
Selecciona una opción: 2

--- Tareas Pendientes ---
No.   | Descripción                    | Estado
--------------------------------------------------
1     | Preparar la presentación para el viernes | pendiente
2     | Comprar leche                  | pendiente
--------------------------------------------------

--- Gestor de Tareas ---
1. Agregar tarea
2. Listar tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir
Selecciona una opción: 3

--- Tareas Pendientes ---
No.   | Descripción                    | Estado
--------------------------------------------------
1     | Preparar la presentación para el viernes | pendiente
2     | Comprar leche                  | pendiente
--------------------------------------------------
Ingresa el número de la tarea a completar: 2
Tarea 'Comprar leche' ha sido marcada como completada.

--- Gestor de Tareas ---
1. Agregar tarea
2. Listar tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir
Selecciona una opción: 5
Gracias por usar el gestor de tareas
```
