def generar_contraseña(longitud=8):
    """
    Genera una contraseña aleatoria.

    Args:
        longitud: Número de caracteres de la contraseña (predeterminado: 8)

    Returns:
        Una cadena con la contraseña generada
    """
    import random
    import string
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# este código define una función `generar_contraseña` que genera una contraseña aleatoria de una longitud especificada. La función utiliza los módulos `random` y `string` para crear una cadena de caracteres que incluye letras mayúsculas, minúsculas, dígitos y caracteres especiales. La función toma un argumento opcional `longitud`, que por defecto es 8, y devuelve una cadena con la contraseña generada. Este ejemplo muestra cómo crear una función para generar contraseñas seguras y cómo documentarla adecuadamente para mejorar su claridad y usabilidad.