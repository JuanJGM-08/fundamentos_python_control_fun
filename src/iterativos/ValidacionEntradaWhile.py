def obtener_numero_en_rango(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Error: El número debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Error: Debes introducir un número entero.")

edad = obtener_numero_en_rango("Introduce tu edad (0-120): ", 0, 120)
print(f"Edad registrada: {edad} años")
# En este ejemplo, se define una función 'obtener_numero_en_rango()' que solicita al usuario que introduzca un número dentro de un rango específico (en este caso, entre 0 y 120). La función utiliza un bucle 'while' para continuar solicitando la entrada hasta que el usuario ingrese un número válido. Se maneja la excepción 'ValueError' para asegurarse de que el usuario introduzca un número entero. Si el número ingresado está fuera del rango permitido, se muestra un mensaje de error y se vuelve a solicitar la entrada. Finalmente, se llama a la función para obtener la edad del usuario y se imprime el resultado.