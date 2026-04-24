def imprimir_triangulo(altura):
    fila = 1
    while fila <= altura:
        print("*" * fila)
        fila += 1

imprimir_triangulo(5)

# En este ejemplo, se define una función 'imprimir_triangulo()' que toma un argumento 'altura' y utiliza un bucle 'while' para imprimir un triángulo de asteriscos. La variable 'fila' se inicializa en 1 y se incrementa en cada iteración del bucle hasta que alcanza el valor de 'altura'. En cada iteración, se imprime una cadena de asteriscos cuyo número es igual al valor actual de 'fila', lo que crea la forma de un triángulo. Al llamar a la función con el valor 5, se imprime un triángulo de 5 filas.