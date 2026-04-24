cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]

pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

# En este ejemplo, se utiliza una comprensión de listas para crear una nueva lista llamada 'cuadrados' que contiene los cuadrados de los números del 1 al 5. Luego, se imprime la lista resultante. En el segundo ejemplo, se crea una lista llamada 'pares' que contiene solo los números pares del 0 al 9 utilizando una condición dentro de la comprensión de listas.