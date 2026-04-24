condiciones = [True, True, False, True]

if all(condiciones):
    print("Todas las condiciones son verdaderas.")
else:
    print("Al menos una condición es falsa.")

# En este ejemplo, la función all() evalúa si todas las condiciones en la lista 'condiciones' son verdaderas. Dado que hay una condición que es falsa, la función all() devuelve False y se imprime el mensaje indicando que al menos una condición es falsa. Si todas las condiciones fueran verdaderas, se imprimiría el mensaje indicando que todas las condiciones son verdaderas.