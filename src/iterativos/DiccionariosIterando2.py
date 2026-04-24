usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}

for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# Iterando solo sobre valores
for valor in usuario.values():
    print(valor)