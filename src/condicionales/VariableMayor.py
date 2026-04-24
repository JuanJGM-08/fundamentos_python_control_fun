a = 5
b = 10
c = 15

if a > b:
    if a > c:
        print('a es el mayor.')
    else:
        if c > b:
            print('c es el mayor.')
        else:
            print('b es el mayor.')
else:
    if b > c:
        print('b es el mayor.')
    else:
        print('c es el mayor.')

# El programa evalúa tres variables 'a', 'b' y 'c' para determinar cuál de ellas es la mayor. Utiliza una estructura de control anidada con múltiples condiciones para comparar los valores de las variables y mostrar un mensaje indicando cuál es la mayor.