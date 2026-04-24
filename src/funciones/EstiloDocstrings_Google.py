def validar_email(email):
    """
    Verifica si una dirección de correo electrónico tiene formato válido.

    Args:
        email (str): La dirección de correo a validar

    Returns:
        bool: True si el formato es válido, False en caso contrario

    Raises:
        TypeError: Si email no es una cadena de texto
    """
    if not isinstance(email, str):
        raise TypeError("El email debe ser una cadena de texto")
    return "@" in email and "." in email.split("@")[-1]

#este código define una función `validar_email` que verifica si una dirección de correo electrónico tiene un formato válido. La función toma un argumento `email`, que debe ser una cadena de texto, y devuelve `True` si el formato es válido (es decir, si contiene un "@" y un "." después del "@"), o `False` en caso contrario. Si el argumento no es una cadena de texto, la función lanza un `TypeError`. Este ejemplo muestra cómo documentar una función con una docstring que describe su propósito, los argumentos que recibe, lo que devuelve y las excepciones que puede lanzar.