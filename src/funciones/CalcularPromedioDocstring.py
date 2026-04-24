def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Suma todos los números de la lista y divide el resultado
    entre la cantidad de elementos.

    Args:
        numeros: Una lista de valores numéricos

    Returns:
        El promedio como valor flotante

    Ejemplo:
        >>> calcular_promedio([1, 2, 3, 4])
        2.5
    """
    return sum(numeros) / len(numeros)

#este código define una función `calcular_promedio` que toma una lista de números como argumento y devuelve el promedio de esos números. La función incluye una docstring que explica su propósito, los argumentos que recibe, lo que devuelve y un ejemplo de uso. Al llamar a la función con una lista de números, se obtiene el promedio, que se puede imprimir o usar en otras partes del código. Este ejemplo muestra cómo documentar una función para mejorar su claridad y facilitar su uso por parte de otros desarrolladores.