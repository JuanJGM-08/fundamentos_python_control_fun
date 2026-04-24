# Enfoque mejorado: siempre devuelve una lista (vacía en caso de error)
def filtrar_positivos(numeros):
    if not isinstance(numeros, list):
        return []  # Lista vacía en caso de error

    return [num for num in numeros if num > 0]

# este código define una función `filtrar_positivos` que toma una lista de números y devuelve una nueva lista que contiene solo los números positivos. Si el argumento proporcionado no es una lista, la función devuelve una lista vacía en lugar de generar un error. Esto garantiza que la función siempre devuelva un tipo de dato consistente (una lista), lo que facilita su uso y manejo en otras partes del código.