def filtrar_pares(lista):
    """
    Filtra los números pares de una lista.

    Parameters
    ----------
    lista : list
        Lista de números enteros

    Returns
    -------
    list
        Nueva lista que contiene solo los números pares
    """
    return [num for num in lista if num % 2 == 0]

# Este código define una función `filtrar_pares` que toma una lista de números enteros como argumento y devuelve una nueva lista que contiene solo los números pares. La función utiliza una comprensión de listas para iterar sobre cada número en la lista original y verificar si es par (es decir, si el número dividido por 2 tiene un residuo de 0). Si el número es par, se incluye en la nueva lista. La función también incluye una docstring que describe su propósito, los parámetros que recibe y lo que devuelve, siguiendo el estilo de documentación recomendado por NumPy. Este ejemplo muestra cómo crear una función para filtrar elementos de una lista y cómo documentarla adecuadamente para mejorar su claridad y usabilidad.