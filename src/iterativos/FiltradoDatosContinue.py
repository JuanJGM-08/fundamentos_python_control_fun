temperaturas = [22, -5, 28, 31, -15, 19, 26, -8]

print("Temperaturas positivas:")
for temp in temperaturas:
    if temp <= 0:
        continue

    print(f"{temp}°C")
# En este ejemplo, se define una lista de temperaturas que incluye tanto valores positivos como negativos. Se utiliza un bucle 'for' para iterar a través de cada temperatura en la lista. Dentro del bucle, se verifica si la temperatura es menor o igual a cero. Si es así, se utiliza la declaración 'continue' para saltar a la siguiente iteración del bucle, lo que significa que no se ejecutará el código que sigue para esa temperatura. Si la temperatura es positiva, se imprime en formato de grados Celsius. Como resultado, solo se imprimirán las temperaturas positivas de la lista.