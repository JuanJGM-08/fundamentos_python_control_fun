saldo = 1000
while saldo > 0:
    print(f"Saldo actual: {saldo}€")
    gasto = float(input("Introduce la cantidad a gastar (0 para salir): "))

    if gasto == 0:
        break  # Salimos del bucle inmediatamente

    if gasto > saldo:
        print("No tienes suficiente saldo.")
        continue  # Volvemos al inicio del bucle

    saldo -= gasto

print(f"Saldo final: {saldo}€")
# En este ejemplo, se utiliza un bucle 'while' para simular un sistema de gastos. El usuario tiene un saldo inicial de 1000€. En cada iteración del bucle, se muestra el saldo actual y se solicita al usuario que introduzca una cantidad a gastar. Si el usuario introduce 0, el bucle se rompe y el programa termina. Si el gasto es mayor que el saldo disponible, se muestra un mensaje de error y se vuelve al inicio del bucle para solicitar una nueva cantidad. Si el gasto es válido, se resta del saldo y se continúa con la siguiente iteración. Al finalizar el bucle, se muestra el saldo final.