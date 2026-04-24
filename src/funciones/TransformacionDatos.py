def formato_nombre(nombre, apellido):
    return f"{apellido.upper()}, {nombre.capitalize()}"

print(formato_nombre("ana", "garcía"))  # Imprime: GARCÍA, Ana

# En este código, la función `formato_nombre` toma un nombre y un apellido como argumentos y devuelve una cadena formateada con el apellido en mayúsculas seguido del nombre con la primera letra en mayúscula. Al llamar a la función con los argumentos "ana" y "garcía", se obtiene el resultado "GARCÍA, Ana", que se imprime en la consola. Este ejemplo muestra cómo se pueden manipular cadenas dentro de una función para obtener un formato específico.