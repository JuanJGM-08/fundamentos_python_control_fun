numeros = [1, 2, 0, 4, 0, 6, 7]

for num in numeros:
    if num == 0:
        print("Omitiendo división por cero")
        continue

    resultado = 10 / num
    print(f"10 / {num} = {resultado}")

# En este ejemplo, se define una lista de números que incluye algunos ceros. Se utiliza un bucle 'for' para iterar a través de cada número en la lista. Dentro del bucle, se verifica si el número es igual a cero. Si es así, se imprime un mensaje indicando que se está omitiendo la división por cero y se utiliza la declaración 'continue' para saltar a la siguiente iteración del bucle, lo que significa que no se ejecutará el código que sigue para ese número. Si el número no es cero, se realiza la división de 10 entre ese número y se imprime el resultado. Como resultado, solo se imprimirán los resultados de las divisiones para los números no cero en la lista.