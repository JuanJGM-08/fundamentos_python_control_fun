numeros = [0, 0, 1, 0]

if any(numeros):
    print("Al menos un número es no cero.")

# En este ejemplo, la función any() evalúa si al menos uno de los elementos en la lista 'numeros' es verdadero (en este caso, no cero). Dado que hay un número no cero en la lista, la condición se cumple y se imprime el mensaje correspondiente. Si todos los números fueran cero, la función any() devolvería False y no se imprimiría nada.