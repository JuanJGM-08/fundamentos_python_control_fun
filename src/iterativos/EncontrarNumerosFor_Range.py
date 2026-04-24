def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primos = []
for num in range(2, 20):
    if es_primo(num):
        primos.append(num)

print(f"Números primos entre 2 y 19: {primos}")  # [2, 3, 5, 7, 11, 13, 17, 19]
# En este ejemplo, se define una función 'es_primo()' que verifica si un número es primo. Luego, se utiliza un bucle 'for' para iterar sobre los números del 2 al 19 y se llama a la función para verificar si cada número es primo. Si lo es, se agrega a la lista 'primos'. Finalmente, se imprime la lista de números primos encontrados en ese rango.