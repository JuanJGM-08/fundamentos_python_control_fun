acceso_registrado = True

acceso_permitido = False
if acceso_permitido:
    print("Acceso concedido.")
else:
    if acceso_registrado:
        print("Acceso concedido.")

# El programa evalúa dos variables booleanas, 'acceso_permitido' y 'acceso_registrado', utilizando una estructura de control anidada. Primero verifica si 'acceso_permitido' es True; si lo es, se muestra un mensaje indicando que el acceso ha sido concedido. Si 'acceso_permitido' es False, se evalúa la variable 'acceso_registrado'. Si 'acceso_registrado' es True, también se muestra un mensaje indicando que el acceso ha sido concedido. En este caso, aunque 'acceso_permitido' es False, 'acceso_registrado' es True, por lo que el resultado de la evaluación es True y se concede el acceso.