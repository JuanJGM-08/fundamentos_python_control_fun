for i in range(1, 4):
    print(f"Grupo {i}:")

    for j in range(1, 6):
        if j == 3:
            print("  Saltando el elemento 3")
            continue  # Solo afecta al bucle interno

        print(f"  Elemento {j}")

    print("Fin del grupo\n")

# En este ejemplo, se utiliza un bucle 'for' anidado para crear grupos de elementos. El bucle externo itera a través de los números del 1 al 3, representando cada grupo. El bucle interno itera a través de los números del 1 al 5, representando los elementos dentro de cada grupo. Si el elemento actual es igual a 3, se imprime un mensaje indicando que se está saltando ese elemento y se utiliza la declaración 'continue' para saltar a la siguiente iteración del bucle interno, lo que significa que no se ejecutará el código que sigue para ese número dentro del grupo. Como resultado, el número 3 no se imprimirá en ningún grupo, pero los demás números sí lo harán. Al final de cada grupo, se imprime un mensaje indicando el fin del grupo.