for numero in range(1, 11):
    if numero % 2 == 0:  # Si el número es par
        continue  # Saltamos a la siguiente iteración

    print(f"Número impar: {numero}")
# En este ejemplo, se utiliza un bucle 'for' para iterar a través de los números del 1 al 10. Dentro del bucle, se verifica si el número actual es par utilizando el operador módulo (%). Si el número es par, se utiliza la declaración 'continue' para saltar a la siguiente iteración del bucle, lo que significa que no se ejecutará el código que sigue para ese número. Si el número no es par (es impar), se imprime el número. Como resultado, solo se imprimirán los números impares del 1 al 10.