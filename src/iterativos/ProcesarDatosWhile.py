def calcular_factorial(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
    return resultado

numero = 5
print(f"El factorial de {numero} es {calcular_factorial(numero)}")  # 120
# En este ejemplo, se define una función 'calcular_factorial()' que toma un número 'n' como argumento y calcula su factorial utilizando un bucle 'while'. El resultado se inicializa en 1 y se multiplica por 'n' en cada iteración del bucle, mientras 'n' sea mayor que 0. Después de cada multiplicación, 'n' se decrementa en 1. Finalmente, la función devuelve el resultado del factorial. Se llama a la función con el número 5 y se imprime el resultado, que es 120.