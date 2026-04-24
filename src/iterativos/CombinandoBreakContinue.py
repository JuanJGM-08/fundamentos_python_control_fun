numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
limite = 50
suma = 0

for num in numeros:
    # Ignoramos múltiplos de 3
    if num % 3 == 0:
        print(f"Omitiendo {num} (múltiplo de 3)")
        continue

    # Sumamos el número
    suma += num
    print(f"Añadiendo {num}: suma = {suma}")

    # Si la suma supera el límite, terminamos
    if suma > limite:
        print(f"Límite de {limite} superado")
        break
# En este ejemplo, se define una lista de números impares y un límite para la suma. El bucle 'for' itera a través de cada número en la lista. Si el número es un múltiplo de 3, se imprime un mensaje y se utiliza 'continue' para saltar a la siguiente iteración, lo que significa que no se sumará ese número. Si el número no es un múltiplo de 3, se suma a la variable 'suma' y se imprime el valor actual de la suma. Si en algún momento la suma supera el límite establecido, se imprime un mensaje indicando que el límite ha sido superado y se utiliza 'break' para salir del bucle inmediatamente.