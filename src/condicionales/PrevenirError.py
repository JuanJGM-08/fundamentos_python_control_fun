lista = []

if lista and lista[0] == 'Python':
    print("El primer elemento es 'Python'.")

#En este ejemplo, si lista está vacía, la primera condición lista es falsa, y Python no intenta evaluar lista[0] == 'Python', evitando así un IndexError por intentar acceder a un índice inexistente.