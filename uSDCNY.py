def convertir_usd_a_cny(dolares):
    tipo_de_cambio = 6.75  # Tipo de cambio de CNY por USD
    yuanes = dolares * tipo_de_cambio
    return f"{yuanes:.2f} Chinese Yuan"

# Ejemplos de uso:
print(convertir_usd_a_cny(15))   # '101.25 Chinese Yuan'
print(convertir_usd_a_cny(465))  # '3138.75 Chinese Yuan'