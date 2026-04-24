# Mejor: separar la obtención del resultado de su presentación
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

# Uso
notas = [7, 8, 6, 9]
promedio = calcular_promedio(notas)
print(f"El promedio es: {promedio}")  # La impresión se hace fuera de la función

# En este código, la función `calcular_promedio` se encarga únicamente de calcular el promedio de una lista de números y devolver el resultado. La presentación del resultado (en este caso, imprimirlo en la consola) se realiza fuera de la función, lo que permite que la función sea más flexible y reutilizable en diferentes contextos sin estar acoplada a una forma específica de mostrar el resultado. Este enfoque mejora la separación de responsabilidades y facilita el mantenimiento del código.