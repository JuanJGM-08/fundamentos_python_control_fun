def calcular_descuento(precio, porcentaje=10):
    # La variable 'descuento' solo existe dentro de esta función
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

precio_con_descuento = calcular_descuento(100)
print(f"Precio con descuento: {precio_con_descuento}")  # Imprime: Precio con descuento: 90.0
# print(descuento)  # Esto daría error porque 'descuento' no existe fuera de la función

# En este código, la función `calcular_descuento` calcula el precio final después de aplicar un descuento. La variable `descuento` es local a la función y no puede ser accedida desde fuera de ella, lo que demuestra el concepto de alcance de variables en Python.