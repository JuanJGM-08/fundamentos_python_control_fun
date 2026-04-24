transacciones = [
    {"id": 1, "monto": 1200, "estado": "completada"},
    {"id": 2, "monto": -50, "estado": "error"},
    {"id": 3, "monto": 800, "estado": "pendiente"},
    {"id": 4, "monto": 1500, "estado": "completada"},
    {"id": 5, "monto": 0, "estado": "cancelada"}
]

total_procesado = 0

for t in transacciones:
    # Ignoramos transacciones no completadas
    if t["estado"] != "completada":
        print(f"Transacción {t['id']}: {t['estado']} - ignorada")
        continue

    # Verificamos montos válidos
    if t["monto"] <= 0:
        print(f"Transacción {t['id']}: monto inválido ({t['monto']})")
        continue

    # Procesamos la transacción
    total_procesado += t["monto"]
    print(f"Transacción {t['id']}: {t['monto']}€ procesada")

print(f"Total procesado: {total_procesado}€")
# En este ejemplo, se define una lista de transacciones, cada una representada como un diccionario con un 'id', un 'monto' y un 'estado'. El programa utiliza un bucle 'for' para iterar a través de cada transacción. Dentro del bucle, se realizan varias verificaciones: primero, se verifica si el estado de la transacción es "completada". Si no lo es, se imprime un mensaje indicando que la transacción ha sido ignorada y se utiliza 'continue' para saltar a la siguiente iteración del bucle. Luego, se verifica si el monto de la transacción es válido (mayor que cero). Si el monto es inválido, se imprime un mensaje indicando el error y se utiliza 'continue' para saltar a la siguiente iteración. Si ambas verificaciones son super