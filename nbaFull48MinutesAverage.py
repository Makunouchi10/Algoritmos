'''
calcular el tiempo de juego de un jugador de nba
'''
def nba_extrap(ppg, mpg):
    if ppg == 0:
        return 0
    if mpg == 0:
        return 0  # Esto cubre el caso en el que el jugador no ha jugado minutos.

    extrapolacion = (ppg / mpg) * 48
    return round(extrapolacion, 1)


# Ejemplos de uso
print(nba_extrap(12, 20))  # 28.8
print(nba_extrap(10, 10))  # 48.0
print(nba_extrap(5, 17))  # 14.1
print(nba_extrap(0, 0))  # 0