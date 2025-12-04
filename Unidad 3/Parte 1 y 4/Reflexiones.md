# Reflexiones sobre Programación Funcional

## Parte 1: Identificación y Análisis de Funciones

A continuación, analizo las funciones proporcionadas:

### Función A: `calcular_promedio`

- **Estado:** **PURA**
- **Por qué:**
  - **Determinista:** Dados los mismos números en la lista, el promedio matemático siempre será el mismo.
  - **Sin efectos secundarios:** No modifica la lista original ni altera variables externas; solo calcula y retorna un valor.

---

### Función B: `siguiente_id`

- **Estado:** **IMPURA**
- **Por qué:**
  - **Efecto secundario:** Modifica una variable externa (`global contador`).
  - **No determinista:** Si la llamo dos veces seguidas sin argumentos, me devuelve valores diferentes ("ID-1", "ID-2"). Su resultado depende del estado del sistema, no de sus argumentos.
- **Cómo convertirla a pura:**
  Eliminar la dependencia global. Pasar el contador actual como argumento y retornar el nuevo ID y el nuevo contador, o usar un generador infinito.

```python
def generarId(contadorActual):
    return f"ID-{contadorActual + 1}"
```

### Función C: agregar_fecha

- **Estado:** **IMPURA**
- **Por qué:**
  - **Efecto secundario:** Modifica el diccionario registro original al hacer `registro['fecha']`
  - **No determinista:** Depende de `datetime.now()`, que cambia cada microsegundo.
- **Cómo convertirla a pura:** Pasar la fecha como argumento para controlar el determinismo. Luego crear y retornar un nuevo diccionario en lugar de modificar el existente(inmutabilidad).

```python
def agregarFechaPura(registro, fecha):
    nuevoRegistro = registro.copy()
    nuevoRegistro['fecha'] = fecha
    return nuevoRegistro
```

### Función D: agregar_fecha

- **Estado:** **PURA**
- **Por qué:**
  - **Sin efecto secundario:** Las compresiones de lista en python crean una nueva lista, dejando la original intacta.
  - **Determinista:** Siempre filtra igual dada la misma lista.

### Función E: agregar_fecha

- **Estado:** **IMPURA**
- **Por qué:**
  - **Efecto secundario:** `random.shuffle(lista)` modifica la lista original "in-place". Si imprime la lista fuera de la funcion, habra cambiado.
  - **No determinista:** Depende del modo `random`.
- **Cómo convertirla a pura:** Crear una copia de mezclar o usar `random.sample` que devuelve una nueva lista.

```python
def mezclarPura(lista):
    # random.sample con k=len(lista) crea una copia mezclada
    return random.sample(lista, len(lista))
```

## Parte 4: Reflexión Metacognitiva

**1. ¿Qué significa que una función sea "pura"?**

**R:** Una función pura es aquella que actúa como una traducción perfecta y aislada: siempre produce el mismo resultado para la misma entrada y no altera nada en el "mundo exterior" (sin efectos secundarios).

- **Ejemplo:** Un diccionario de inglés a español en papel. Si buscas la palabra "Apple", siempre dirá "Manzana". Consultarlo no cambia el significado de las palabras ni gasta la tinta del libro. En cambio, preguntarle a una persona es impuro, porque su respuesta puede cambiar si está cansada o distraída.

**2. En la Parte 3, ¿por qué `crear_transformador` retorna una función en lugar de aplicar directamente la transformación? ¿Qué ventaja ofrece este diseño?**

**R:** Retorna una función porque estamos usando el patrón de Fábrica de Funciones (Clausuras).

**Ventaja:** La gran ventaja es la separación entre configuración y uso. Nos permite definir la lógica (por ejemplo, "multiplicar por 2") una sola vez y guardarla en una variable. Luego, podemos aplicar esa misma lógica guardada a muchas listas diferentes en momentos distintos, haciendo el código mucho más modular y reutilizable en pipelines.

**3. ¿Qué dificultades encontraste al convertir el código imperativo a funcional en la Parte 2?**

**R:** El cambio de la mentalidad de "pasos temporales" a "flujo de datos", al final de programar de una forma hace que uno se adapte de forma automatica a un modo. En el código imperativo, hacía todo en un solo bloque (filtrar, calcular impuesto y sumar al total al mismo tiempo). En funcional, tuve que dividir eso en tres etapas distintas (`filter` -> `map` -> `sum`). Al principio parecía más código, pero comprendi que cada parte es más fácil de entender y probar por separado a pesar de parecer un poco mas.

**4. Si tuvieras que explicar la diferencia entre programación imperativa y funcional a alguien que no programa, ¿qué analogía usarías?**

**R:** Usaría la analogía de la cocina:

- **Programación Imperativa (El Cocinero Solitario):** Un solo cocinero corre por la cocina haciendo todo. "Corta la cebolla. Ahora échala al sartén. Ahora bate los huevos ahí mismo. Uy, se quemó un poco, bájale al fuego". Modifica el estado de la cocina y de la comida constantemente sobre la marcha.

- **Programación Funcional (La Fábrica de Galletas):** Es una línea de ensamblaje. Una máquina _solo_ mezcla la masa y la pasa. La siguiente máquina _solo_ corta la forma y la pasa. La siguiente _solo_ hornea. Ninguna máquina modifica lo que hizo la anterior, solo transforman lo que reciben y lo pasan a la siguiente etapa de forma perfecta y ordenada.
