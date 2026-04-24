def obtener_calificacion(puntuacion):
    if puntuacion < 0 or puntuacion > 100:
        return "Puntuación inválida"

    if puntuacion >= 90:
        return "Sobresaliente"
    if puntuacion >= 70:
        return "Notable"
    if puntuacion >= 60:
        return "Bien"
    if puntuacion >= 50:
        return "Suficiente"

    return "Insuficiente"

#este código define una función `obtener_calificacion` que toma una puntuación numérica y devuelve una calificación basada en rangos predefinidos. Si la puntuación es menor que 0 o mayor que 100, la función devuelve un mensaje de "Puntuación inválida". Para puntuaciones dentro del rango válido, la función evalúa cada rango de calificación y devuelve la correspondiente. Al llamar a esta función con diferentes valores de puntuación, se pueden obtener las calificaciones correspondientes según los criterios establecidos. Este ejemplo muestra cómo manejar casos especiales (puntuaciones inválidas) y cómo usar múltiples condiciones para determinar el resultado final.