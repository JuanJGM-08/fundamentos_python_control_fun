def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.

    Args:
        base: Longitud de la base del triángulo
        altura: Altura del triángulo

    Returns:
        El área del triángulo

    Ejemplos:
        >>> area_triangulo(4, 3)
        6.0
        >>> area_triangulo(5, 8)
        20.0
    """
    return (base * altura) / 2

#help(): Muestra la documentación de un objeto
#pydoc: Módulo que genera documentación a partir de docstrings
#doctest: Permite ejecutar ejemplos incluidos en los docstrings como pruebas

# Este código define una función `area_triangulo` que calcula el área de un triángulo dado su base y altura. La función incluye una docstring que describe su propósito, los argumentos que recibe, lo que devuelve y ejemplos de uso. Al llamar a esta función con diferentes valores de base y altura, se puede obtener el área del triángulo correspondiente. Este ejemplo muestra cómo documentar una función para mejorar su claridad y facilitar su uso por parte de otros desarrolladores.