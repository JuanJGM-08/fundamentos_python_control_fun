def calcular_raiz_cuadrada(numero, precision=0.0001):
    aproximacion = numero / 2  # Valor inicial
    while abs(aproximacion**2 - numero) > precision:
        aproximacion = (aproximacion + numero/aproximacion) / 2
    return aproximacion

print(f"Raíz cuadrada de 25: {calcular_raiz_cuadrada(25):.6f}")  # 5.000000
print(f"Raíz cuadrada de 7: {calcular_raiz_cuadrada(7):.6f}")    # 2.645751
# En este ejemplo, se define una función 'calcular_raiz_cuadrada()' que utiliza el método de aproximación de Newton para calcular la raíz cuadrada de un número dado. La función toma dos argumentos: 'numero', que es el número del cual se desea calcular la raíz cuadrada, y 'precision', que determina la precisión del resultado. El bucle 'while' continúa ejecutándose hasta que la diferencia entre el cuadrado de la aproximación y el número original sea menor que la precisión especificada. Finalmente, se devuelve la aproximación calculada. Se llaman a la función con los números 25 y 7, y se imprime el resultado con una precisión de 6 decimales.