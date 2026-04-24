# ¡CUIDADO! Bucle infinito
contador = 1
#while contador <= 5:
    #print(contador)
    # Olvidamos incrementar contador

contador = 1
while contador <= 5:
    print(contador)
    contador += 1  # Importante: actualizar la variable de control

# En este ejemplo, se muestra un bucle 'while' que cuenta desde 1 hasta 5. En el primer caso, el bucle es infinito porque no se actualiza la variable 'contador', lo que hace que la condición 'contador <= 5' siempre sea verdadera. En el segundo caso, se corrige el error al incrementar 'contador' en cada iteración, lo que permite que el bucle termine correctamente después de imprimir los números del 1 al 5.