def calcular_precio_con_iva(precio_base, tasa_iva=0.21):
    return precio_base * (1 + tasa_iva)

precio_final = calcular_precio_con_iva(100)
print(f"Precio con IVA: {precio_final} €")  # Imprime: Precio con IVA: 121.0 €

# En este código, la función `calcular_precio_con_iva` toma un precio base y una tasa de IVA (que por defecto es 0.21 o 21%). La función calcula el precio final sumando el IVA al precio base y devuelve el resultado. Al llamar a la función con un precio base de 100, se obtiene el precio final con IVA incluido, que se imprime en la consola. Este ejemplo muestra cómo se pueden usar funciones para realizar cálculos y devolver resultados basados en los argumentos proporcionados.