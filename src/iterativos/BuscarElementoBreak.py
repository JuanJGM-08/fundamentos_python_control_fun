def buscar_elemento(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice

    return -1  # Si llegamos aquí, el elemento no está en la lista

numeros = [4, 7, 2, 9, 1, 5]
posicion = buscar_elemento(numeros, 9)
print(f"El elemento se encuentra en la posición: {posicion}")
# En este ejemplo, se define una función 'buscar_elemento()' que toma una lista y un objetivo como argumentos. La función utiliza un bucle 'for' junto con 'enumerate()' para iterar sobre los elementos de la lista y sus índices. Si el elemento actual es igual al objetivo, se devuelve su índice. Si el bucle termina sin encontrar el objetivo, se devuelve -1 para indicar que el elemento no está presente en la lista. En este caso, se busca el número 9 en la lista de números y se imprime su posición, que es 3.