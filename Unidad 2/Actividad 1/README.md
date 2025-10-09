# Actividad: Creación de una Clase Simple en Python

Este proyecto implementa una clase `Libro` en Python para demostrar los conceptos fundamentales de la Programación Orientada a Objetos (POO), como clases, objetos, atributos y métodos.

## Diseño de la Clase `Libro`

El diseño de la clase se basa en modelar las características y acciones esenciales de un libro dentro del contexto de una biblioteca.

### Atributos

- **Atributos de Instancia**:

  - `titulo`, `autor`, `añoPublicacion`: Son las características fundamentales que definen un libro de forma única. Cada libro (objeto) tendrá sus propios valores para estos atributos.
  - `prestado`: Este es el estado del libro. Es un atributo de instancia porque el estado de préstamo es individual para cada libro. Se inicializa en `False` por defecto, ya que se asume que un libro recién añadido a la biblioteca está disponible.

- **Atributo de Clase**:
  - `biblioteca`: Se eligió como un atributo de clase porque es una propiedad compartida por todos los libros del sistema. En lugar de que cada objeto guarde una copia del nombre "Biblioteca Central", todas las instancias comparten este único valor, lo cual es más eficiente en memoria y representa correctamente el modelo (todos pertenecen al mismo lugar).

### Métodos

- `__init__(self, ...)`: Se encarga de recibir los datos básicos y asignarlos a los atributos de la instancia, garantizando que cada libro se cree con un estado inicial válido en este caso recibio los datos de titulo, autor y año de publicación.
- `prestar()` y `devolver()`: Representan las acciones clave que se pueden realizar con un libro. Estos métodos manipulan el atributo de estado `prestado`, cambiando su valor de `True` a `False` y viceversa. Son la interfaz para interactuar con el estado del objeto.
- `mostrarEstado()`: Método de utilidad que proporciona una representación clara y legible de toda la información del objeto en un momento dado. Fundamental para depurar y verificar que el estado del libro cambia correctamente después de llamar a los métodos `prestar()` y `devolver()`.

## Demostración de Ejecución

Aquí se muestra una captura de pantalla de la ejecución del script `main.py`. El programa primero crea tres libros, muestra su estado inicial (todos disponibles), luego realiza algunas operaciones de préstamo y devolución, y finalmente muestra el estado actualizado de cada libro.

## Captura 1

![Ejemplo de ejecución en consola](/Unidad%202/Actividad%201/PruebasImagen/CapturaPrueba1.png)

## Captura 1-1

![Ejemplo de ejecucion en consola](/Unidad%202/Actividad%201/PruebasImagen/CapturaPrueba2.png)
