def convertir_temperatura(valor, origen, destino):
    """
    Convierte una temperatura entre diferentes unidades.

    Args:
        valor: El valor de la temperatura a convertir
        origen: Unidad de origen ('C', 'F' o 'K')
        destino: Unidad de destino ('C', 'F' o 'K')

    Returns:
        float: La temperatura convertida, o None si los parámetros son inválidos
    """
    # Validación de parámetros
    unidades_validas = {'C', 'F', 'K'}
    if origen not in unidades_validas or destino not in unidades_validas:
        return None

    # Si origen y destino son iguales, no hay conversión necesaria
    if origen == destino:
        return valor

    # Primero convertimos a Celsius como unidad intermedia
    if origen == 'F':
        celsius = (valor - 32) * 5/9
    elif origen == 'K':
        celsius = valor - 273.15
    else:  # origen es 'C'
        celsius = valor

    # Luego convertimos de Celsius a la unidad de destino
    if destino == 'F':
        return celsius * 9/5 + 32
    elif destino == 'K':
        return celsius + 273.15
    else:  # destino es 'C'
        return celsius

# Ejemplos de uso
print(convertir_temperatura(25, 'C', 'F'))    # Imprime: 77.0
print(convertir_temperatura(98.6, 'F', 'C'))  # Imprime: 37.0
print(convertir_temperatura(0, 'C', 'K'))     # Imprime: 273.15
print(convertir_temperatura(20, 'X', 'Y'))    # Imprime: None

# En este código, la función `convertir_temperatura` se encarga de convertir una temperatura entre las unidades Celsius, Fahrenheit y Kelvin. La función incluye validaciones para asegurarse de que las unidades de origen y destino sean válidas. Si las unidades son iguales, la función devuelve el valor sin cambios. Si las unidades son diferentes, la función primero convierte la temperatura a Celsius como unidad intermedia y luego a la unidad de destino. Al llamar a esta función con diferentes valores y unidades, se pueden obtener las temperaturas convertidas según los criterios establecidos. Este ejemplo muestra cómo manejar múltiples casos de conversión dentro de una sola función.