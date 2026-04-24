while True:
    entrada = input("Escribe algo (o 'salir' para terminar): ")

    if entrada.lower() == 'salir':
        print("Programa terminado.")
        break

    print(f"Has escrito: {entrada}")
# En este ejemplo, se utiliza un bucle 'while' para crear un programa que pregunta al usuario si desea continuar. El bucle se ejecuta indefinidamente hasta que el usuario responde con "salir". Si el usuario responde con "salir", el programa muestra un mensaje de finalización y utiliza la declaración 'break' para salir del bucle. Si el usuario introduce cualquier otra cosa, el programa muestra lo que ha escrito y vuelve a solicitar la entrada.