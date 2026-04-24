def dividir_seguro(a, b):
    # Verificación de seguridad
    if b == 0:
        print("Error: División por cero")
        return None  # Salida anticipada

    # Este código solo se ejecuta si b no es cero
    resultado = a / b
    return resultado

print(dividir_seguro(10, 2))   # Imprime: 5.0
print(dividir_seguro(10, 0))   # Imprime: Error: División por cero y luego None

# En este código, la función `dividir_seguro` realiza una verificación para evitar la división por cero. Si el divisor `b` es cero, la función imprime un mensaje de error y devuelve `None`, lo que termina la ejecución de la función de manera anticipada. Si `b` no es cero, la función procede a realizar la división y devuelve el resultado. Este ejemplo ilustra cómo usar un `return` para salir de una función antes de que se ejecute el código restante, lo que es útil para manejar casos especiales o errores.