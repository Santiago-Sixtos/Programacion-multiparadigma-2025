"""
Modulo de persistencia

Contiene funciones auxiliares para manejar la lectura y escritura dde datos en archivos JSON.
"""

import json

def guardarJson(datos: dict, nombreArchivo: str):
    try:
        with open(nombreArchivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent = 4, ensure_ascii=False)

        print(f"Datos guardados exitosamente en '{nombreArchivo}'.")

    except IOError as e:
        print(f"Error al guardar el archivo: {e}.")

    except TypeError as e:
        print(f"Error dde tipo al serializar a JSON: {e}.")

def cargarJson(nombreArchivo: str) -> dict | None:
    try:
        with open(nombreArchivo, 'r', encoding='utf-8') as f:
            datos = json.load(f)
            return datos
    
    except FileNotFoundError:
        print(f"Archivo '{nombreArchivo}' no encontrado. Se creara uno nuevo al guardar")
        return None

    except json.JSONDecodeError:
        print(f"Error: El archivo '{nombreArchivo}' esta vacio o corrupto")
        return None
    
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
        return None