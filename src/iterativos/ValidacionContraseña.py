def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
            continue  # Optimización: ya verificamos este requisito

        if caracter.islower():
            tiene_minuscula = True
            continue

        if caracter.isdigit():
            tiene_numero = True

    return tiene_mayuscula and tiene_minuscula and tiene_numero

# Probamos algunas contraseñas
contraseñas = ["abc123", "Password", "Password1", "pass123", "PASS123"]
for pwd in contraseñas:
    if validar_contraseña(pwd):
        print(f"'{pwd}' es válida")
    else:
        print(f"'{pwd}' NO es válida")
# En este ejemplo, se define una función 'validar_contraseña()' que verifica si una contraseña cumple con ciertos requisitos: debe tener al menos 8 caracteres, contener al menos una letra mayúscula, una letra minúscula y un número. La función utiliza un bucle 'for' para iterar a través de cada carácter de la contraseña y establece banderas para cada requisito. Si se encuentra un carácter que cumple con un requisito, se establece la bandera correspondiente en True y se utiliza 'continue' para saltar a la siguiente iteración del bucle, lo que optimiza el proceso al no verificar los demás requisitos para ese carácter. Al final del bucle, la función devuelve True si todos los requisitos se cumplen, o False en caso contrario. Luego, se prueban varias contraseñas y se imprime si son válidas o no según los criterios establecidos.