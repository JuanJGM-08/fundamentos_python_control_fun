def saludar(nombre, mensaje="¡Bienvenido!"):
    print(f"Hola {nombre}. {mensaje}")

saludar("Carlos")  # Usa el mensaje predeterminado
# Imprime: Hola Carlos. ¡Bienvenido!

saludar("María", "¿Cómo estás hoy?")  # Usa el mensaje personalizado
# Imprime: Hola María. ¿Cómo estás hoy?
# En este código, la función `saludar` tiene un parámetro obligatorio `nombre` y un parámetro opcional `mensaje` con un valor predeterminado. Si no se proporciona un mensaje al llamar a la función, se usará el mensaje predeterminado "¡Bienvenido!". Si se proporciona un mensaje personalizado, se usará ese mensaje en su lugar. Este ejemplo muestra cómo funcionan los parámetros con valores predeterminados en las funciones de Python.