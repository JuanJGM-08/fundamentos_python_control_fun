encontrado = False

for i in range(5):
    for j in range(5):
        if i * j > 10:
            print(f"Valor encontrado: {i} * {j} = {i*j}")
            encontrado = True
            break  # Sale del bucle interno

    if encontrado:
        break  # Sale del bucle externo

# En este ejemplo, se utiliza un bucle 'for' anidado para iterar a través de los números del 0 al 4 tanto para 'i' como para 'j'. Dentro del bucle interno, se verifica si el producto de 'i' y 'j' es mayor que 10. Si se encuentra un valor que cumple esta condición, se imprime el valor encontrado y se establece la variable 'encontrado' en True. Luego, se utiliza 'break' para salir del bucle interno. Después de salir del bucle interno, se verifica si la variable 'encontrado' es True, lo que indica que se ha encontrado un valor que cumple la condición. Si es así, se utiliza otro 'break' para salir del bucle externo, lo que detiene completamente la búsqueda. Como resultado, el programa imprimirá el primer valor encontrado que cumple la condición y luego terminará.