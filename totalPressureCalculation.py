'''
calcular presion de gases
'''
def calcular_presion_total(m1, M1, m2, M2, V, temperatura_celsius):
    # Convertir temperatura a Kelvin
    T = temperatura_celsius + 273.15

    # Constante del gas en dm³·atm·K⁻¹·mol⁻¹
    R = 0.082

    # Calcular presión total
    P_total = (m1 / M1 + m2 / M2) * R * T / V
    return P_total

# Ejemplo de uso
if __name__ == "__main__":
    # Introducir los valores
    m1 = float(input("Introduce la masa del gas 1 (g): "))
    M1 = float(input("Introduce la masa molar del gas 1 (g/mol): "))
    m2 = float(input("Introduce la masa del gas 2 (g): "))
    M2 = float(input("Introduce la masa molar del gas 2 (g/mol): "))
    V = float(input("Introduce el volumen del recipiente (dm³): "))
    temperatura_celsius = float(input("Introduce la temperatura (°C): "))

    presion_total = calcular_presion_total(m1, M1, m2, M2, V, temperatura_celsius)

    print(f"La presión total ejercida por los gases es: {presion_total:.2f} atm")