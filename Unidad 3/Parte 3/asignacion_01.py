"""
Parte 3: Implementación Práctica.
Sistema de transformación de datos configurable.
"""
from functools import reduce

#Fábrica de Filtros
def crearFiltro(predicado):
    """
    Recibe un predicado (función que devuelve bool) y retorna una 
    nueva función que filtra una lista completa.
    """
    #Retornamos una lambda que espera lista de datos
    return lambda lista: list(filter(predicado, lista))

#Fábrica de Transformadores
def crearTransformador(funcion):
    """
    Recibe una función de transformación y retorna una 
    nueva función que aplica esa transformación a toda una lista.
    """
    # Retornamos una lambda que aplica map a la lista recibida
    return lambda lista: list(map(funcion, lista))

#Fábrica de Reductores
def crearReductor(funcion, valorInicial):
    """
    Recibe una función de reducción y un valor inicial.
    Retorna una nueva función que reduce una lista a un solo valor.
    """
    #Retornamos una lambda que aplica reduce a la lista recibida
    return lambda lista: reduce(funcion, lista, valorInicial)

#Función de Composición (El Pipeline)
def componer(*funciones):
    """
    Recibe múltiples funciones y retorna una nueva función 
    que las aplica en secuencia (de izquierda a derecha).
    """
    return lambda datoInicial: reduce(lambda acc, f: f(acc), funciones, datoInicial)


#Main
if __name__ == "__main__":
    print("Inicio de Pruebas")
    
    numeros = [1, -2, 3, -4, 5, -6, 7, 8, -9, 10]
    print(f"Datos de entrada: {numeros}")

    #Definimos el Pipeline: 
    pipeline = componer(
        #Filtrar solo positivos
        crearFiltro(lambda x: x > 0),
        #Elevar al cuadrado
        crearTransformador(lambda x: x ** 2),
        #Sumar todo (reducir)
        crearReductor(lambda acc, x: acc + x, 0)
    )

    #Ejecutamos el pipeline con los datos
    resultado = pipeline(numeros)
    
    print(f"Resultado obtenido: {resultado}")
    
    #Verificación manual:
    esperado = 248
    assert resultado == esperado
    print("El cálculo es correcto.")