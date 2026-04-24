def calcular_pago(horas, tarifa=15, moneda="EUR"):
    total = horas * tarifa
    return f"{total} {moneda}"# Diferentes formas de llamar a la función
pago1 = calcular_pago(40)  # 40 horas, tarifa predeterminada, moneda predeterminada
pago2 = calcular_pago(35, 20)  # 35 horas, tarifa de 20, moneda predeterminada
pago3 = calcular_pago(30, moneda="USD")  # 30 horas, tarifa predeterminada, moneda USD
pago4 = calcular_pago(horas=25, tarifa=18, moneda="GBP")  # Todo especificado por nombre

print(pago1)  # Imprime: 600 EUR
print(pago2)  # Imprime: 700 EUR
print(pago3)  # Imprime: 450 USD
print(pago4)  # Imprime: 450 GBP

# En este código, la función `calcular_pago` tiene tres parámetros: `horas`, `tarifa` y `moneda`. El parámetro `horas` es obligatorio, mientras que `tarifa` y `moneda` tienen valores predeterminados. La función calcula el pago total multiplicando las horas por la tarifa y devuelve una cadena con el total y la moneda. Se muestran diferentes formas de llamar a la función, utilizando tanto argumentos posicionales como argumentos por nombre, lo que demuestra la flexibilidad en cómo se pueden pasar los argumentos a las funciones en Python.