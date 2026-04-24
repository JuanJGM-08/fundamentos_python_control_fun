numeros = [1, 2, 3, 4, 5]
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(paridad)  # Salida: ['impar', 'par', 'impar', 'par', 'impar']

# El programa define una lista de números del 1 al 5 y utiliza una comprensión de listas para crear una nueva lista llamada 'paridad'. En esta nueva lista, cada número se evalúa para determinar si es par o impar utilizando una expresión ternaria. Si el número es divisible por 2 (es decir, si el residuo de la división por 2 es 0), se asigna "par"; de lo contrario, se asigna "impar". Finalmente, se imprime la lista resultante que indica la paridad de cada número.