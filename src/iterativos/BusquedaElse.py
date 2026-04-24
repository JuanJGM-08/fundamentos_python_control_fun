def buscar_usuario(usuarios, nombre):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            print(f"Usuario encontrado: {usuario}")
            return usuario
    else:
        print(f"Usuario '{nombre}' no encontrado, creando nuevo perfil...")
        nuevo_usuario = {"nombre": nombre, "nivel": 1}
        usuarios.append(nuevo_usuario)
        return nuevo_usuario

base_usuarios = [
    {"nombre": "Ana", "nivel": 5},
    {"nombre": "Carlos", "nivel": 3}
]

buscar_usuario(base_usuarios, "Ana")      # Existente
buscar_usuario(base_usuarios, "Roberto")  # Nuevo
# En este ejemplo, se define una función 'buscar_usuario()' que toma una lista de usuarios y un nombre como argumentos. La función utiliza un bucle 'for' para iterar a través de cada usuario en la lista. Si encuentra un usuario cuyo nombre coincide con el nombre buscado, imprime un mensaje indicando que el usuario ha sido encontrado y devuelve el perfil del usuario. Si el bucle termina sin encontrar ningún usuario con el nombre especificado (es decir, sin ejecutar 'return'), se ejecuta el bloque 'else' asociado al bucle, que imprime un mensaje indicando que el usuario no ha sido encontrado y crea un nuevo perfil para ese usuario, lo agrega a la lista de usuarios y devuelve el nuevo perfil. Al probar la función con diferentes nombres, se puede observar cómo maneja tanto casos en los que el usuario ya existe como casos en los que se debe crear un nuevo perfil.