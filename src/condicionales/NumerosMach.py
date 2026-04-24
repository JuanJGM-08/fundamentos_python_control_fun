numeros = [1, 2, 3, 4]

match numeros:
    case []:
        print("La lista está vacía.")
    case [uno]:
        print(f"Un solo elemento: {uno}.")
    case [uno, dos]:
        print(f"Dos elementos: {uno} y {dos}.")
    case [uno, *resto]:
        print(f"Primer elemento: {uno}, resto de la lista: {resto}.")
# El programa define una lista de números y utiliza una estructura de control 'match' para comparar la lista con diferentes patrones. Dependiendo de la cantidad de elementos en la lista, se muestra un mensaje indicando si está vacía, tiene un solo elemento, dos elementos o más, mostrando el primer elemento y el resto de la lista.
