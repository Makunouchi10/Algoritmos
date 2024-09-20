'''
Se realizo un cambio de tamaño de imagen a 16/9
'''
def convertir_a_16_9(resolucion_x, resolucion_y):
    # Verificamos que la altura (Y) sea válida
    if resolucion_y <= 0:
        raise ValueError("La altura (Y) debe ser un valor positivo.")

    # Calcular la nueva resolución X para una relación de aspecto 16:9
    nueva_x = round((16 / 9) * resolucion_y)

    return nueva_x, resolucion_y


# Ejemplo de uso
x, y = 1440, 1080
nueva_resolucion = convertir_a_16_9(x, y)
print(f"Nueva resolución (16:9): {nueva_resolucion[0]}x{nueva_resolucion[1]}")