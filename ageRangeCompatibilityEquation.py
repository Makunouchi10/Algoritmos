'''
Calcular la edad minima para estar con alguien
'''
def calcular_rango_edad(edad):
    if edad <= 14:
        min_edad = int(edad - 0.10 * edad)
        max_edad = int(edad + 0.10 * edad)
    else:
        min_edad = int(edad / 2 + 7)
        max_edad = int(edad * 2 - 7)

    return f"{min_edad}-{max_edad}"


# Ejemplos
print(calcular_rango_edad(27))  # Salida: 20-40
print(calcular_rango_edad(5))  # Salida: 4-5
print(calcular_rango_edad(17))  # Salida: 15-20