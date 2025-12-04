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
