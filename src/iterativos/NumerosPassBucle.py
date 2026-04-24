# Bucle que no hace nada para los números pares
for numero in range(1, 10):
    if numero % 2 == 0:
        pass  # No hacemos nada con los números pares
    else:
        print(f"Procesando número impar: {numero}")

# En este ejemplo, se utiliza un bucle 'for' para iterar a través de los números del 1 al 9. Dentro del bucle, se verifica si el número actual es par utilizando el operador módulo (%). Si el número es par, se utiliza la declaración 'pass' para indicar que no se realizará ninguna acción para ese número. Si el número no es par (es impar), se imprime un mensaje indicando que se está procesando ese número. Como resultado, solo se imprimirán los números impares del 1 al 9, mientras que los números pares serán ignorados sin generar ningún error o acción adicional.