# Actividad: Implementación de una Clase Inventario

Este proyecto consiste en el desarrollo de un sistema simple para gestionar un inventario, aplicando los principios de **Encapsulación** y **Abstracción** de la Programación Orientada a Objetos en Python.

El sistema se compone de dos clases principales: `Producto` e `Inventario`.

## Diseño y Explicación

El diseño del código se centra en crear un sistema robusto y mantenible, donde los detalles internos de los objetos están protegidos y la interacción se realiza a través de una interfaz pública y controlada.

### Clase `Producto`: Encapsulación

La clase `Producto` representa un artículo individual, esta clase representa nuestro ejemplo de **encapsulación**.

- **Atributos Privados y Protegidos**:

  - El `nombre` es **público** porque actúa como un identificador natural y no requiere validación para ser leído.
  - El `_precio` se define como **protegido** para indicar que, aunque es parte del estado interno, su modificación debe ser controlada.
  - El `__stock` es **privado** porque es un atributo crítico. Queremos un control estricto sobre cómo se modifica para prevenir estados inválidos (ej. un stock negativo). Ocultarlo con `__` hace más difícil su modificación accidental desde fuera de la clase.

- **Getters y Setters con `@property`**:
  - Se utilizan las propiedades para exponer los atributos `_precio` y `__stock` de una manera "pythonica". Esto nos permite añadir **lógica de validación** en los _setters_ (ej. el precio debe ser `> 0`, el stock no puede ser `< 0`). Quien use la clase simplemente interactúa con `producto.precio` o `producto.stock`, sin saber que por detrás se están ejecutando métodos que garantizan la integridad de los datos.

### Clase `Inventario`: Abstracción

La clase `Inventario` representa la colección de productos y es un ejemplo de **abstracción**.

- **Ocultamiento de la Complejidad Interna**:

  - El atributo `__productos` (un diccionario) es **privado**. Esto se debe a que la forma en que almacenamos los productos es un _detalle de implementación_. El usuario de la clase `Inventario` no necesita saber si usamos un diccionario, una lista o una base de datos.
  - La clase expone una **interfaz pública y simple** (`agregarProducto`, `buscarProducto`, `valorInventario`). El usuario solo interactúa con estos métodos, que son fáciles de entender y usar. Toda la complejidad de manejar el diccionario (buscar llaves, actualizar valores, etc.) está oculta (abstraída) dentro de la clase.

- **Métodos Especiales (`__len__` y `__str__`)**:
  - Estos métodos mejoran la abstracción al permitir que el objeto `Inventario` se comporte como una colección nativa de Python. Poder usar `len(mi_inventario)` o `print(mi_inventario)` hace que la interacción con el objeto sea mucho más intuitiva y natural.

## Demostración de Ejecución

A continuación, se muestra una captura de pantalla de la ejecución del script, donde se crea un inventario, se agregan productos, se modifica el estado de uno de ellos y se muestra el valor total del inventario.

![Ejemplo de ejecución del inventario](/Unidad%202/Actividad%202/PruebaImagen/demostracion.png)
