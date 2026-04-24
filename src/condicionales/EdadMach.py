edad = 20

match edad:
    case edad if edad < 18:
        print("Eres menor de edad.")
    case edad if edad >= 18 and edad < 65:
        print("Eres adulto.")
    case edad if edad >= 65:
        print("Eres adulto mayor.")
# El programa evalúa la variable 'edad' utilizando una estructura de control 'match' con condiciones específicas para determinar si la persona es menor de edad, adulta o adulta mayor, y muestra un mensaje correspondiente.
