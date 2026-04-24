def calcular_descuento(precio, porcentaje):
    """
    Calcula el precio con descuento.

    Args:
        precio: El precio original
        porcentaje: El porcentaje de descuento (0-100)

    Returns:
        float: El precio después de aplicar el descuento
    """
    return precio - (precio * porcentaje / 100)

# este código define una función `calcular_descuento` que toma un precio y un porcentaje de descuento, y devuelve el precio final después de aplicar el descuento. La función incluye una docstring que describe su propósito, los argumentos que recibe y lo que devuelve. Al llamar a la función con un precio de 100 y un descuento del 15%, se obtiene el precio final con descuento, que se imprime en la consola. Este ejemplo muestra cómo documentar una función para mejorar su legibilidad y facilitar su uso por parte de otros desarrolladores.