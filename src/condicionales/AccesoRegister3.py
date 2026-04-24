acceso_registrado = True

acceso_permitido = False
if acceso_permitido or (acceso_registrado and True):
    print("Acceso concedido.")

# El programa evalúa dos variables booleanas, 'acceso_permitido' y 'acceso_registrado', utilizando una combinación de operadores lógicos 'or' y 'and'. La condición se evalúa de la siguiente manera: primero se verifica si 'acceso_permitido' es True; si lo es, se concede el acceso. Si 'acceso_permitido' es False, se evalúa la segunda parte de la condición, que verifica si 'acceso_registrado' es True y si la expresión adicional (en este caso, simplemente 'True') también es True. Dado que 'acceso_registrado' es True, el resultado de la evaluación es True y se concede el acceso.