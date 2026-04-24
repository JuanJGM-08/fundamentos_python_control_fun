datos = ["25", "error", "42", "texto", "17"]

suma = 0
for valor in datos:
    if not valor.isdigit():
        print(f"Valor no numérico ignorado: '{valor}'")
        continue

    suma += int(valor)

print(f"La suma de los valores válidos es: {suma}")
# En este ejemplo, se define una lista de datos que contiene tanto valores numéricos como no numéricos. Se utiliza un bucle 'for' para iterar a través de cada valor en la lista. Dentro del bucle, se verifica si el valor es un dígito utilizando el método 'isdigit()'. Si el valor no es numérico, se imprime un mensaje indicando que se ha ignorado ese valor y se utiliza la declaración 'continue' para saltar a la siguiente iteración del bucle. Si el valor es numérico, se convierte a entero y se suma a la variable 'suma'. Al final del bucle, se imprime la suma de los valores válidos.