# Asignar una función a una variable
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32 # Función que convierte temperatura de Celsius a Fahrenheit, se creo para mejor funcionamiento del codigo
convertir = celsius_a_fahrenheit
temperatura_f = convertir(25)  # Equivalente a celsius_a_fahrenheit(25)
print(f"25°C equivalen a {temperatura_f}°F")  # Imprime: 25°C equivalen a 77.0°F

# este codigo muestra cómo asignar una función a una variable y luego usar esa variable para llamar a la función. En este caso, la función `celsius_a_fahrenheit` se asigna a la variable `convertir`, lo que permite usar `convertir` como un alias para la función original.