"""
Parte 3: Implementación Práctica.
Sistema de transformación de datos configurable.
"""
from functools import reduce

#Fábrica de Filtros
def crearFiltro(predicado):
    """
    Recibe un predicado (función que devuelve bool) y retorna una 
    NUEVA función que filtra una lista completa.
    """
    #Retornamos una lambda que espera lista de datos
    return lambda lista: list(filter(predicado, lista))