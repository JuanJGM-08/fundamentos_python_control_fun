usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "usuario"},
    {"nombre": "Marta", "rol": "moderador"}
]

for usuario in usuarios:
    match usuario:
        case {"rol": "admin"}:
            print(f"{usuario['nombre']} tiene permisos de administrador.")
        case {"rol": "moderador"}:
            print(f"{usuario['nombre']} puede moderar contenidos.")
        case {"rol": "usuario"}:
            print(f"{usuario['nombre']} es un usuario regular.")
        case _:
            print(f"Rol de {usuario['nombre']} desconocido.")
# El programa define una lista de usuarios, cada uno con un nombre y un rol. Utiliza una estructura de control 'match' para evaluar el rol de cada usuario y muestra un mensaje indicando los permisos o funciones correspondientes según su rol. Si el rol no coincide con ninguno de los casos definidos, se muestra un mensaje de "Rol desconocido".
