fruta = input("Introduzca una fruta: ")

match fruta:
    case "manzana":
        print("La fruta es una manzana.")
    case "naranja":
        print("La fruta es una naranja.")
    case "plátano":
        print("La fruta es un plátano.")
    case _:
        print("Fruta desconocida.")
# El programa solicita al usuario que introduzca una fruta y utiliza una estructura de control 'match' para comparar la entrada con diferentes casos. Si la fruta coincide con alguno de los casos, se muestra un mensaje correspondiente. Si no coincide con ninguno, se muestra un mensaje de "Fruta desconocida".