def crear_lista_pares(maximo):
    return [num for num in range(2, maximo + 1, 2)]

def crear_diccionario_cuadrados(numeros):
    return {num: num ** 2 for num in numeros}

pares = crear_lista_pares(10)
print(pares)  # Imprime: [2, 4, 6, 8, 10]

cuadrados = crear_diccionario_cuadrados([1, 2, 3, 4])
print(cuadrados)  # Imprime: {1: 1, 2: 4, 3: 9, 4: 16}

# En este código, la función `crear_lista_pares` genera una lista de números pares hasta un número máximo especificado. La función `crear_diccionario_cuadrados` crea un diccionario donde las claves son los números de la lista proporcionada y los valores son sus cuadrados. Al llamar a estas funciones, se obtienen y se imprimen la lista de pares y el diccionario de cuadrados, respectivamente. Este ejemplo muestra cómo las funciones pueden devolver estructuras de datos complejas como listas y diccionarios.