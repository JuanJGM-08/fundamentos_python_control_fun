def calcular_precio_final(precio_base, impuesto):
    return precio_base + (precio_base * impuesto)

total = calcular_precio_final(100, 0.21)  # 100 va a precio_base, 0.21 va a impuesto
print(f"Precio final: {total}")  # Imprime: Precio final: 121.0
# En este código, la función `calcular_precio_final` toma dos parámetros: `precio_base` e `impuesto`. Al llamar a la función, se le pasan los argumentos 100 y 0.21, lo que hace que la función calcule el precio final incluyendo el impuesto y lo imprima. Este ejemplo ilustra cómo los parámetros y argumentos funcionan en las funciones de Python.