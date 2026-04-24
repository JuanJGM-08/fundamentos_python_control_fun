# Usando while
suma = 0
i = 1
while i <= 10:
    suma += i
    i += 1
print(f"Suma (while): {suma}")

# Equivalente con for
suma = 0
for i in range(1, 11):
    suma += i
print(f"Suma (for): {suma}")
# En este ejemplo, se muestra cómo usar un bucle 'while' para calcular la suma de los números del 1 al 10. La variable 'suma' se inicializa en 0 y se incrementa con el valor de 'i' en cada iteración del bucle, mientras 'i' sea menor o igual a 10. Después del bucle, se imprime el resultado. Luego, se muestra una versión equivalente utilizando un bucle 'for' con la función 'range()', que también calcula la suma de los números del 1 al 10. Ambos métodos producen el mismo resultado, que es 55.