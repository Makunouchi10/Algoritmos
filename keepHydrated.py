import math
def calcular_litros(time):
    litros = time * 0.5  # Calcula la cantidad de litros
    return math.floor(litros)  # Redondea hacia abajo

# Ejemplos de uso
print(calcular_litros(3))    # Salida: 1
print(calcular_litros(6.7))  # Salida: 3
print(calcular_litros(11.8)) # Salida: 5