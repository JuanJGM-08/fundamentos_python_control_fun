# Correcto
def crear_perfil(nombre, edad, ciudad="Madrid"):
    return f"Perfil: {nombre}, {edad} años, {ciudad}"# Incorrecto - causaría un error de sintaxis
# def crear_perfil(nombre, ciudad="Madrid", edad):
#     return f"Perfil: {nombre}, {edad} años, {ciudad}"

# este codigo define una función `crear_perfil` que tiene un parámetro obligatorio `nombre`, un parámetro obligatorio `edad`, y un parámetro opcional `ciudad` con un valor predeterminado de "Madrid". La función devuelve una cadena que describe el perfil de la persona. Es importante que los parámetros con valores predeterminados se coloquen después de los parámetros obligatorios para evitar errores de sintaxis.