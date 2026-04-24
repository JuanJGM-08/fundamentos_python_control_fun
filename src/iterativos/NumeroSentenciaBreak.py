for numero in range(1, 11):
    if numero == 5:
        print("¡Encontrado el 5! Saliendo del bucle...")
        break
    print(f"Número actual: {numero}")

print("Bucle terminado")
# En este ejemplo, se utiliza un bucle 'for' para iterar a través de los números del 1 al 10. Dentro del bucle, se verifica si el número actual es igual a 5. Si se encuentra el número 5, se imprime un mensaje y se utiliza la declaración 'break' para salir del bucle inmediatamente. Si el número no es 5, se imprime el número actual. Después de que el bucle termina (ya sea por encontrar el número 5 o por completar la iteración), se imprime un mensaje indicando que el bucle ha terminado.