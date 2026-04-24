def saludar(nombre):
    print(f"Hola, {nombre}")
    # No hay return explícito

resultado = saludar("Laura")
print(f"La función devolvió: {resultado}")  # Imprime: La función devolvió: None

# En este código, la función `saludar` imprime un mensaje de saludo pero no tiene una declaración `return`. Por lo tanto, cuando se llama a la función, devuelve `None` por defecto. Al imprimir el resultado de la función, se muestra que el valor devuelto es `None`, lo que ilustra el concepto de que una función sin un `return` explícito devuelve `None` en Python.