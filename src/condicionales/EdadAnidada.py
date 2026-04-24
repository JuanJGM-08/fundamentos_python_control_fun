edad = 30
estado_civil = 'soltero'

if edad >= 18:
    if estado_civil == 'casado':
        print('Eres un adulto casado.')
    else:
        print('Eres un adulto soltero.')
else:
    print('Eres menor de edad.')

# El programa evalúa dos condiciones anidadas: primero verifica si la edad es mayor o igual a 18 años, y luego verifica el estado civil. Dependiendo de las condiciones, se muestra un mensaje indicando si la persona es un adulto casado, un adulto soltero o menor de edad.