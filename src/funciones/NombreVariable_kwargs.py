def mostrar_informacion(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

# Podemos pasar cualquier cantidad de argumentos por nombre
mostrar_informacion(nombre="Python", creador="Guido van Rossum", año=1991)
# Imprime:
# nombre: Python
# creador: Guido van Rossum
# año: 1991

# En este código, la función `mostrar_informacion` utiliza el parámetro `**datos`, lo que permite pasar una cantidad variable de argumentos por nombre. La función itera sobre los pares clave-valor en el diccionario `datos` y los imprime. Al llamar a la función, se pueden proporcionar tantos argumentos por nombre como se desee, y la función los manejará correctamente. Este ejemplo muestra cómo usar parámetros de longitud variable para argumentos por nombre en las funciones de Python.