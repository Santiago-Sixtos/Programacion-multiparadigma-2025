# Proyecto: Sistema de Gestión de Biblioteca (POO)

Este proyecto es un sistema de gestión de biblioteca por consola, desarrollado en Python como una demostración de los principios clave de la Programación Orientada a Objetos (POO) y el diseño de software modular.

## Propósito del Programa

El sistema permite administrar un catálogo de libros y una lista de usuarios, facilitando las operaciones básicas de una biblioteca:

- Registrar nuevos libros y usuarios.
- Prestar libros a usuarios, actualizando el estado del libro.
- Recibir devoluciones de libros.
- Consultar los libros que están actualmente disponibles.
- Persistencia de datos: Toda la información se guarda en un archivo `bibliotecaDatos.json`, permitiendo que el estado del sistema se recupere entre sesiones.

## Instrucciones de Ejecución

1.  **Requisitos**: Asegúrate de tener Python 3.10 o superior instalado.
2.  **Clonar**: Clona este repositorio en tu máquina local.
3.  **Navegar**: Abre una terminal y navega hasta la carpeta raíz del proyecto (ej. `GestorBiblioteca/`).
4.  **Ejecutar**: Lanza el programa ejecutando el archivo `main.py`:

    ```bash
    python main.py
    ```

5.  El menú interactivo te guiará. El archivo `bibliotecaDatos.json` se creará y actualizará en la misma carpeta desde donde ejecutaste el comando.

## Estructura del Código (Modularidad)

El proyecto está organizado en un paquete principal (`modulos`) para separar las responsabilidades (Alta Cohesión y Bajo Acoplamiento).

- `main.py`: El punto de entrada. Controla el flujo del programa y maneja el menú (la "Vista").
- `modulos/`: El paquete que contiene toda la lógica.
  - `modelos.py`: Contiene las clases de entidad (`ItemBiblioteca`, `Libro`, `Usuario`). Define la estructura de los datos (el "Modelo").
  - `biblioteca.py`: Contiene la clase `Biblioteca`, que es el "cerebro" o "Controlador" del sistema. Orquesta las operaciones y gestiona las listas de objetos.
  - `persistencia.py`: Contiene funciones auxiliares dedicadas exclusivamente a leer y escribir en el archivo JSON.

## Diseño POO Aplicado

- **Encapsulación**: Todos los atributos de las clases son "protegidos" (ej. `self._titulo`, `self._libros`). El acceso y modificación se realizan a través de métodos públicos (ej. `agregarLibro()`, `prestarLibro()`), protegiendo el estado interno.
- **Herencia**: Se utiliza una clase base `ItemBiblioteca` para definir la estructura común de cualquier ítem. La clase `Libro` hereda de `ItemBiblioteca`, reutilizando su código y añadiendo atributos específicos (autor, año).
- **Polimorfismo**: Los métodos `mostrarInfo()` y `toDict()` están definidos en la clase base `ItemBiblioteca` y son sobrescritos en la clase hija `Libro`. Esto permite que la clase `Biblioteca` llame a `libro.mostrarInfo()` sin saber si es un `Libro` u otro tipo de `Item`, y Python ejecutará la versión correcta del método.
