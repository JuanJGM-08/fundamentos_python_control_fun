numeros = [4, 6, 7, 8, 10]  # Ahora incluimos el 7

for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado un primo: {num}!")
        break
else:
    print("No se encontró ningún número primo en la lista")

# En este ejemplo, se define una lista de números y se utiliza un bucle 'for' para iterar a través de cada número en la lista. Dentro del bucle, se verifica si el número es primo comprobando que no sea divisible por 2 ni por 3. Si se encuentra un número primo, se imprime un mensaje indicando que se ha encontrado y se utiliza 'break' para salir del bucle inmediatamente. Si el bucle termina sin encontrar ningún número primo (es decir, sin ejecutar 'break'), se ejecuta el bloque 'else' asociado al bucle, que imprime un mensaje indicando que no se encontró ningún número primo en la lista. En este caso, como el número 7 es primo, el programa imprimirá "¡Encontrado un primo: 7!" y no ejecutará el bloque 'else'.