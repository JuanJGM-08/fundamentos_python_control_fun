def dividir_seguro(a, b):
    """
    Realiza una división segura entre dos números.

    Args:
        a: El numerador
        b: El denominador

    Returns:
        El resultado de la división a/b, o None si b es cero

    Ejemplo:
        >>> dividir_seguro(10, 2)
        5.0
        >>> dividir_seguro(10, 0)
        None
    """
    if b == 0:
        return None
    return a / b

# este código define una función `dividir_seguro` que realiza una división entre dos números, `a` y `b`. La función incluye una docstring que describe su propósito, los argumentos que recibe, lo que devuelve y un ejemplo de uso. Si el denominador `b` es cero, la función devuelve `None` para evitar un error de división por cero. De lo contrario, devuelve el resultado de la división `a/b`. Este ejemplo muestra cómo manejar casos especiales en una función y cómo documentarla adecuadamente para mejorar su claridad y usabilidad.