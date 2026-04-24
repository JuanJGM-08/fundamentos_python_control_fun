def crear_usuario(nombre, apellido, edad, email, activo=True):
    return {
        "nombre_completo": f"{nombre} {apellido}",
        "edad": edad,
        "email": email,
        "activo": activo
    }

# Más fácil de leer con argumentos por nombre
usuario = crear_usuario(
    nombre="Juan",
    apellido="Pérez",
    edad=28,
    email="juan@ejemplo.com",
    activo=False
)

# En este código, la función `crear_usuario` toma varios parámetros para crear un diccionario que representa a un usuario. Al llamar a la función, se utilizan argumentos por nombre, lo que hace que el código sea más legible y claro sobre qué valor corresponde a cada parámetro. Este ejemplo muestra cómo usar parámetros con valores predeterminados y argumentos por nombre en las funciones de Python.