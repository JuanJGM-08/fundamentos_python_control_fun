def dividir(dividendo, divisor):
    return dividendo / divisor

# Usando argumentos posicionales
resultado1 = dividir(10, 2)  # resultado1 = 5.0

# Usando argumentos por nombre
resultado2 = dividir(divisor=2, dividendo=10)  # resultado2 = 5.0

# En este código, la función `dividir` toma dos parámetros: `dividendo` y `divisor`. Al llamar a la función, se pueden usar argumentos posicionales (donde el orden importa) o argumentos por nombre (donde se especifica el nombre del parámetro). Ambos métodos producen el mismo resultado, que es 5.0 en este caso. Este ejemplo ilustra cómo los parámetros y argumentos funcionan en las funciones de Python.