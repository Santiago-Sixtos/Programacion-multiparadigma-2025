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