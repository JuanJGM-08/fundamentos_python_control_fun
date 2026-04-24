edad = 17
permiso_parental = True

if (edad >= 18) or (edad >= 16 and permiso_parental):
    print("Puedes obtener la licencia de conducir.")
else:
    print("No cumples los requisitos para la licencia.")
# El programa evalúa dos condiciones para determinar si una persona puede obtener una licencia de conducir. La primera condición es si la edad es mayor o igual a 18 años, lo que permite obtener la licencia sin restricciones. La segunda condición es si la edad es mayor o igual a 16 años y se cuenta con permiso parental, lo que también permite obtener la licencia. Si ninguna de las condiciones se cumple, se muestra un mensaje indicando que no se cumplen los requisitos para la licencia.