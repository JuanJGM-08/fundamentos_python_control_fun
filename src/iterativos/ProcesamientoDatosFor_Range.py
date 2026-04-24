temperaturas = [22, 19, 24, 25, 21, 23, 20]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Encontrar el día más caluroso
max_temp = max(temperaturas)
indice_max = temperaturas.index(max_temp)
print(f"El día más caluroso fue {dias[indice_max]} con {max_temp}°C")

# Calcular la temperatura promedio
promedio = sum(temperaturas) / len(temperaturas)
print(f"Temperatura promedio: {promedio:.1f}°C")

# Días con temperatura superior al promedio
for i in range(len(dias)):
    if temperaturas[i] > promedio:
        print(f"{dias[i]}: {temperaturas[i]}°C (por encima del promedio)")

# En este ejemplo, se define una lista de temperaturas y una lista de días correspondientes. Se utiliza la función 'max()' para encontrar la temperatura más alta y 'index()' para obtener el índice de esa temperatura, lo que permite identificar el día más caluroso. Luego, se calcula la temperatura promedio utilizando 'sum()' y 'len()'. Finalmente, se utiliza un bucle 'for' junto con una condición para imprimir los días en los que la temperatura fue superior al promedio.