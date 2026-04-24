# Versión más explícita con comentarios
#for item in coleccion:
    #if condicion(item):
        # Procesamiento normal
       # procesar(item)
    #else:
        #pass  # Intencionalmente no hacemos nada con estos elementos
#else:
    # Este bloque se ejecuta si el bucle termina normalmente (sin break)
    #print("Procesamiento completado sin interrupciones")

# En este ejemplo, se muestra un bucle 'for' que itera a través de una colección de elementos. Dentro del bucle, se verifica una condición para cada elemento. Si la condición se cumple, se procesa el elemento normalmente. Si la condición no se cumple, se utiliza 'pass' para indicar que no se realizará ninguna acción para ese elemento. Después de que el bucle ha terminado de iterar a través de todos los elementos, se ejecuta el bloque 'else' asociado al bucle. Este bloque se ejecutará solo si el bucle termina normalmente, es decir, sin ser interrumpido por una declaración 'break'. En este caso, el bloque 'else' imprime un mensaje indicando que el procesamiento se ha completado sin interrupciones. Esta estructura puede ser útil para manejar casos en los que solo queremos realizar acciones específicas para ciertos elementos y no necesitamos hacer nada con los demás, mientras que también queremos ejecutar código adicional después de que el bucle haya terminado su iteración completa.