def contar_palabras(texto):
    """
    Cuenta el número de palabras en un texto.

    Args:
        texto (str): El texto a analizar

    Returns:
        int: El número de palabras encontradas
    """
    return len(texto.split())

# este código define una función `contar_palabras` que toma un argumento `texto`, que es una cadena de texto, y devuelve el número de palabras que contiene. La función utiliza el método `split()` para dividir el texto en palabras y luego cuenta cuántas palabras hay utilizando la función `len()`. La función también incluye una docstring que describe su propósito, los argumentos que recibe y lo que devuelve. Al llamar a esta función con diferentes textos, se puede obtener el conteo de palabras correspondiente. Este ejemplo muestra cómo crear una función para realizar una tarea específica y cómo documentarla adecuadamente para mejorar su claridad y usabilidad.