modo_debug = False

for i in range(100):
    # En modo normal, no mostramos nada durante el procesamiento
    if not modo_debug:
        pass
    else:
        print(f"Procesando iteración {i}")

    # Código de procesamiento real aquí
# En este ejemplo, se define una variable 'modo_debug' que controla si se muestra información de depuración durante el procesamiento de un bucle. Si 'modo_debug' es False, se utiliza la declaración 'pass' para indicar que no se realizará ninguna acción en esa parte del código, lo que significa que no se imprimará nada durante el procesamiento. Si 'modo_debug' es True, se imprimirá un mensaje indicando la iteración actual del bucle. Esto permite al programador activar o desactivar fácilmente la salida de depuración sin modificar el resto del código de procesamiento.