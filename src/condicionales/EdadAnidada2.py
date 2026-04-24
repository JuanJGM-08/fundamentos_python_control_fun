edad = 16
permiso_padres = True

if edad >= 18:
    print('Puedes obtener la licencia de conducir.')
else:
    if edad >= 16:
        if permiso_padres:
            print('Puedes obtener la licencia con permiso de tus padres.')
        else:
            print('Necesitas el permiso de tus padres para obtener la licencia.')
    else:
        print('Eres demasiado joven para conducir.')

# El programa evalúa la edad de una persona para determinar si puede obtener una licencia de conducir. Si la edad es mayor o igual a 18 años, se permite obtener la licencia sin restricciones. Si la edad es menor a 18 pero mayor o igual a 16, se verifica si se cuenta con el permiso de los padres para permitir obtener la licencia. Si la edad es menor a 16, se indica que la persona es demasiado joven para conducir.
