while True:
    respuesta = input("¿Quieres continuar? (s/n): ").lower()

    if respuesta == "n":
        print("Programa finalizado.")
        break

    if respuesta == "s":
        print("Continuando...")
    else:
        print("Respuesta no válida. Introduce 's' o 'n'.")

# En este ejemplo, se utiliza un bucle 'while' para crear un programa que pregunta al usuario si desea continuar. El bucle se ejecuta indefinidamente hasta que el usuario responde con "n" (no). Si el usuario responde con "s" (sí), el programa muestra un mensaje de continuación. Si el usuario introduce una respuesta no válida, se muestra un mensaje de error y se vuelve a solicitar la entrada. El programa finaliza cuando el usuario decide no continuar.
