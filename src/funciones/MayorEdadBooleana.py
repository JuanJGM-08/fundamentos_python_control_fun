def es_mayor_de_edad(edad):
    return edad >= 18

def es_correo_valido(email):
    return "@" in email and "." in email

# Uso en condicionales
usuario_edad = 17
if es_mayor_de_edad(usuario_edad):
    print("Acceso permitido")
else:
    print("Acceso denegado")  # Imprime: Acceso denegado

# este codigo verifica si el usuario es mayor de edad y si el correo electrónico es válido. La función `es_mayor_de_edad` devuelve `True` si la edad es 18 o más, y `False` en caso contrario. La función `es_correo_valido` verifica si el correo electrónico contiene un "@" y un ".", lo que es una validación básica para correos electrónicos. En el ejemplo de uso, se verifica la edad del usuario y se imprime un mensaje de acceso permitido o denegado según corresponda.