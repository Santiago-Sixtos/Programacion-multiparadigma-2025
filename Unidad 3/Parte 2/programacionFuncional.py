"""
Solución Parte 2: Conversión de Paradigmas.
Refactorización de procesar_ventas a estilo funcional.
"""

# Datos de prueba que se dieron
ventasEjemplo = [ 
    {'id': 1, 'monto': 50},
    {'id': 2, 'monto': 150},
    {'id': 3, 'monto': 200},
    {'id': 4, 'monto': 80},
    {'id': 5, 'monto': 300},
]

#Funciones Puras Pequeñas (Helpers) 
def esVentaSignificativa(venta):
    """
    Predicado puro: Retorna True si el monto es mayor a 100.
    """
    return venta['monto'] > 100

def calcularConImpuestos(monto):
    """
    Calcula el monto con el 15% de impuesto.
    """
    return monto * 1.15

def transformarVenta(venta):
    """
    Crea una NUEVA estructura de datos (inmutabilidad).
    No modifica el diccionario original.
    """
    montoFinal = calcularConImpuestos(venta['monto'])
    return {
        'id': venta['id'],
        'montoOriginal': venta['monto'],
        'montoFinal': montoFinal
    }

#Función Principal (Composición)
def procesarVentasFuncional(ventas):
    """
    Pipeline funcional: Filtrar -> Transformar -> Agregar.
    Reemplaza el bucle for imperativo.
    """
    # 1. Filtrado (filter)
    # Seleccionamos solo las ventas que cumplen la condición
    ventasFiltradas = filter(esVentaSignificativa, ventas)
    
    # 2. Transformación (map)
    # Aplicamos la transformación a cada venta filtrada.
    # Convertimos a list() para materializar los datos y poder usarlos dos veces
    # (una para retornarlos y otra para sumar el total).
    resultado = list(map(transformarVenta, ventasFiltradas))
    
    # 3. Agregación (sum)
    # Extraemos solo los montos finales y los sumamos
    total = sum(item['montoFinal'] for item in resultado)
    
    return resultado, total

# --- Bloque de Ejecución y Pruebas ---
if __name__ == "__main__":
    print("Datos Originales")
    print(ventasEjemplo)
    
    # Ejecutamos la lógica funcional
    listaProcesada, totalCalculado = procesarVentasFuncional(ventasEjemplo)
    
    print("\nResultado del Procesamiento Funcional")
    print(f"Total calculado: {totalCalculado}")
    print("Lista detallada:")
    for venta in listaProcesada:
        print(venta)
        
    # Verificación de Inmutabilidad
    print("\nVerificación")
    print(f"¿La lista original sigue intacta? {ventasEjemplo[0] == {'id': 1, 'monto': 50}}")
    
    assert totalCalculado == 747.5
    print("¡Prueba de cálculo correcta!")