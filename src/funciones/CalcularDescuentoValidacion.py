def calcular_descuento(precio, porcentaje):
    # Validación de argumentos
    if not isinstance(precio, (int, float)) or precio < 0:
        raise ValueError("El precio debe ser un número positivo")

    if not isinstance(porcentaje, (int, float)) or not (0 <= porcentaje <= 100):
        raise ValueError("El porcentaje debe ser un número entre 0 y 100")

    # Cálculo del descuento
    descuento = precio * (porcentaje / 100)
    return precio - descuento

try:
    precio_final = calcular_descuento(100, 15)
    print(f"Precio con descuento: {precio_final}")  # Imprime: Precio con descuento: 85.0

    # Esto lanzará un error
    precio_erroneo = calcular_descuento(-50, 10)
except ValueError as e:
    print(f"Error: {e}")  # Imprime: Error: El precio debe ser un número positivo

# En este código, la función `calcular_descuento` incluye validaciones para asegurarse de que los argumentos `precio` y `porcentaje` sean del tipo correcto y estén dentro de los rangos esperados. Si los argumentos no cumplen con las condiciones, se lanza un `ValueError` con un mensaje descriptivo. El bloque `try-except` se utiliza para manejar estas excepciones y mostrar un mensaje de error en caso de que se produzca una validación fallida. Este ejemplo muestra cómo implementar validaciones en las funciones para garantizar que se reciban datos correctos.