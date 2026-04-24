def validar_edades(lista_edades):
    for edad in lista_edades:
        if not isinstance(edad, int) or edad < 0:
            print(f"Edad inválida encontrada: {edad}")
            break
    else:
        print("Todas las edades son válidas")
        return True

    return False

# Probamos con diferentes listas
validar_edades([25, 17, 30, 42])  # Todas válidas
validar_edades([25, -3, 30, 42])  # Una inválida
# En este ejemplo, se define una función 'validar_edades()' que toma una lista de edades como argumento. La función utiliza un bucle 'for' para iterar a través de cada edad en la lista. Dentro del bucle, se verifica si la edad es un número entero no negativo. Si se encuentra una edad que no cumple con esta condición, se imprime un mensaje indicando que se ha encontrado una edad inválida y se utiliza 'break' para salir del bucle inmediatamente. Si el bucle termina sin encontrar ninguna edad inválida (es decir, sin ejecutar 'break'), se ejecuta el bloque 'else' asociado al bucle, que imprime un mensaje indicando que todas las edades son válidas y devuelve True. Si se encuentra una edad inválida, la función devuelve False. Al probar la función con diferentes listas de edades, se puede observar cómo maneja tanto casos válidos como casos con edades inválidas.