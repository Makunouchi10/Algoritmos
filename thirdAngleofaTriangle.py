'''
calcular angulos de figuras geometricas
'''
def tercer_angle(angulo1, angulo2):
    # Sumar los dos ángulos dados
    suma_angulos = angulo1 + angulo2
    # Calcular el tercer ángulo
    tercer_angulo = 180 - suma_angulos
    return tercer_angulo

# Ejemplo de uso
angulo1 = 50
angulo2 = 70
print(f"El tercer ángulo es: {tercer_angle(angulo1, angulo2)} grados")