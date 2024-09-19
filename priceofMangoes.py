def mango(cantidad, precio):
    # Calculamos cuántos grupos de 3 mangos hay
    grupos_de_tres = cantidad // 3
    # Los mangos pagados son los que están fuera de esos grupos
    mangos_pagados = cantidad - grupos_de_tres
    # Calculamos el costo total
    costo_total = mangos_pagados * precio
    return costo_total

# Ejemplos de uso
print(mango(2, 3))  # 6
print(mango(3, 3))  # 6
print(mango(5, 3))  # 12
print(mango(9, 5))  # 30