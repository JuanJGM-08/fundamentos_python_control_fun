usuario = 'admin'
contrasena = '1234'

if usuario == 'admin':
    if contrasena == '1234':
        print('Acceso concedido.')
    else:
        print('Contraseña incorrecta.')
else:
    print('Usuario no reconocido.')

# El programa evalúa dos condiciones anidadas: primero verifica si el usuario es "admin" y luego verifica si la contraseña es "1234". Si ambas condiciones se cumplen, se muestra un mensaje indicando que el acceso ha sido concedido. Si la contraseña es incorrecta, se muestra un mensaje de "Contraseña incorrecta". Si el usuario no es reconocido, se muestra un mensaje de "Usuario no reconocido".