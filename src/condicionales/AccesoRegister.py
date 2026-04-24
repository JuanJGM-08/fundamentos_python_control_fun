acceso_registrado = True

acceso_permitido = False

if acceso_permitido or acceso_registrado:
    print("Acceso concedido.")

# El programa evalúa dos variables booleanas, 'acceso_permitido' y 'acceso_registrado', utilizando el operador lógico 'or'. Si al menos una de las variables es True, se muestra un mensaje indicando que el acceso ha sido concedido. En este caso, aunque 'acceso_permitido' es False, 'acceso_registrado' es True, por lo que el resultado de la evaluación es True y se concede el acceso.