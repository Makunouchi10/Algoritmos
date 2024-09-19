'''
Programa que calcula la edad de un perro y un gato
con respecto a los años humanos
'''
def calcular_edades(human_years):
    if human_years < 1:
        raise ValueError("humanYears debe ser un número entero mayor o igual a 1")

    # Cálculo de años de gato
    if human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4

    # Cálculo de años de perro
    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15 + 9
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]

# Ejemplo de uso
human_years = 5
edades = calcular_edades(human_years)
print(edades)  # Salida: [5, 43, 44]