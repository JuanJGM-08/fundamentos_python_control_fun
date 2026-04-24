def obtener_elemento(lista, indice):
    """
    Obtiene un elemento de una lista por su índice.

    Args:
        lista: La lista de elementos
        indice: Posición del elemento a obtener (comienza en 0)

    Returns:
        El elemento en la posición especificada

    Raises:
        IndexError: Si el índice está fuera del rango de la lista
    """
    return lista[indice]

# este código define una función `obtener_elemento` que toma una lista y un índice como argumentos y devuelve el elemento en la posición especificada por el índice. La función incluye una docstring que describe su propósito, los argumentos que recibe, lo que devuelve y las excepciones que puede generar. Al llamar a esta función con diferentes listas e índices, se puede obtener el elemento correspondiente o manejar el error si el índice está fuera del rango de la lista. Este ejemplo muestra cómo crear una función para acceder a elementos de una lista y cómo documentarla adecuadamente para mejorar su claridad y usabilidad.