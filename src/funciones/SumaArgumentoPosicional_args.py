def sumar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

# Podemos pasar cualquier cantidad de argumentos
print(sumar(1, 2))  # Imprime: 3
print(sumar(1, 2, 3, 4, 5))  # Imprime: 15
print(sumar())  # Imprime: 0

# En este código, la función `sumar` utiliza el parámetro `*numeros`, lo que permite pasar una cantidad variable de argumentos. La función itera sobre los números proporcionados y los suma para obtener el total. Si no se pasan argumentos, el total será 0. Este ejemplo muestra cómo usar parámetros de longitud variable en las funciones de Python para manejar casos donde no se conoce de antemano cuántos argumentos se recibirán.