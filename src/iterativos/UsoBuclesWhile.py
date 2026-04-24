def encontrar_raiz(numero, max_iteraciones=10):
    aproximacion = numero / 2
    iteracion = 0

    while abs(aproximacion**2 - numero) > 0.001 and iteracion < max_iteraciones:
        aproximacion = (aproximacion + numero/aproximacion) / 2
        iteracion += 1
        print(f"Iteración {iteracion}: {aproximacion:.6f}")
    else:
        if iteracion < max_iteraciones:
            print(f"Convergencia alcanzada en {iteracion} iteraciones")
            return aproximacion

    print("No se alcanzó convergencia en el número máximo de iteraciones")
    return aproximacion

encontrar_raiz(25)  # Debería converger rápidamente
encontrar_raiz(612, 5)  # Probablemente no converja en 5 iteraciones
# En este ejemplo, se define una función 'encontrar_raiz()' que utiliza el método de aproximación de Newton para encontrar la raíz cuadrada de un número dado. La función toma un número y un número máximo de iteraciones como argumentos. Dentro del bucle 'while', se calcula una nueva aproximación de la raíz cuadrada y se incrementa el contador de iteraciones. Si la aproximación es suficientemente precisa (diferencia menor a 0.001) o si se alcanza el número máximo de iteraciones, el bucle termina. El bloque 'else' asociado al bucle se ejecuta solo si el bucle termina normalmente (sin interrupciones), lo que permite verificar si se alcanzó la convergencia o no. Al probar la función con diferentes números y límites de iteraciones, se puede observar cómo maneja ambos casos: cuando se alcanza la convergencia y cuando no se logra dentro del límite establecido.