def analizar_datos(valores, umbral):
    tiene_advertencias = False

    for valor in valores:
        if valor > umbral:
            tiene_advertencias = True
            print(f"Advertencia: valor {valor} excede el umbral {umbral}")
        else:
            pass  # Explícitamente no hacemos nada con valores normales
    else:
        if not tiene_advertencias:
            print("Análisis completo: todos los valores están dentro del rango normal")
            return "OK"

    return "ADVERTENCIA"

# Probamos con diferentes conjuntos de datos
analizar_datos([10, 15, 20, 25], 30)  # Todos dentro del umbral
analizar_datos([10, 35, 20, 25], 30)  # Uno excede el umbral
# En este ejemplo, se define una función 'analizar_datos()' que toma una lista de valores y un umbral como argumentos. La función utiliza un bucle 'for' para iterar a través de cada valor en la lista. Si un valor excede el umbral, se establece la variable 'tiene_advertencias' en True y se imprime una advertencia indicando qué valor ha excedido el umbral. Si un valor no excede el umbral, se utiliza la declaración 'pass' para indicar que no se realizará ninguna acción para ese valor. Después de que el bucle ha terminado de iterar a través de todos los valores, se ejecuta el bloque 'else' asociado al bucle. Si no se han encontrado advertencias (es decir, si 'tiene_advertencias' es False), se imprime un mensaje indicando que el análisis está completo y que todos los valores están dentro del rango normal, y la función devuelve "OK". Si se han encontrado advertencias, la función devuelve "ADVERTENCIA". Al probar la función con diferentes conjuntos de datos, se puede observar cómo maneja tanto casos en los que todos los valores están dentro del umbral como casos en los que uno o más valores exceden el umbral.