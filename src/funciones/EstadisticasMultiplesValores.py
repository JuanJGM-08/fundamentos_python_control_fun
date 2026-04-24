def estadisticas(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    return total, promedio, minimo, maximo

datos = [4, 8, 15, 16, 23, 42]
suma, media, menor, mayor = estadisticas(datos)

print(f"Suma: {suma}")        # Imprime: Suma: 108
print(f"Promedio: {media}")   # Imprime: Promedio: 18.0
print(f"Mínimo: {menor}")     # Imprime: Mínimo: 4
print(f"Máximo: {mayor}")     # Imprime: Máximo: 42

# En este código, la función `estadisticas` toma una lista de números y calcula varias estadísticas: la suma total, el promedio, el valor mínimo y el valor máximo. La función devuelve estos valores como una tupla. Al llamar a la función con una lista de datos, se desempaquetan los resultados en variables individuales para luego imprimir cada estadística por separado. Este ejemplo muestra cómo una función puede devolver múltiples valores y cómo se pueden manejar esos valores al llamarla.