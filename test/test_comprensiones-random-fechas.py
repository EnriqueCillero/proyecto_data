import random
from proyecto import squares_of_odds, random_color, days_between


# --------------------------
# TEST squares_of_odds
# --------------------------
def test_squares_of_odds():
    # Impares entre 1 y 5 → 1, 3, 5 → cuadrados: 1, 9, 25
    assert squares_of_odds(5) == [1, 9, 25]

    # n = 0 → rango vacío
    assert squares_of_odds(0) == []

    # n = 1 → solo 1 es impar
    assert squares_of_odds(1) == [1]

    # n = 2 → solo 1 es impar
    assert squares_of_odds(2) == [1]

    # n = 10 → impares: 1,3,5,7,9 → cuadrados: 1,9,25,49,81
    assert squares_of_odds(10) == [1, 9, 25, 49, 81]



# --------------------------
# TEST random_color
# --------------------------
def test_random_color():
    # La salida depende de la semilla, así que será determinista.
    assert random_color(0) in ["rojo", "azul", "verde"]
    assert random_color(1) in ["rojo", "azul", "verde"]

    # Probamos valores específicos usando la misma implementación
    random.seed(0)
    colores = ["rojo", "azul", "verde"]
    esperado = random.choice(colores)

    assert random_color(0) == esperado


# --------------------------
# TEST days_between
# --------------------------
def test_days_between():
    assert days_between("2024-01-01", "2024-01-10") == 9
    assert days_between("2024-01-10", "2024-01-01") == 9   # abs()
    assert days_between("2024-01-01", "2024-01-01") == 0

    # Caso de error: fecha inválida → retorna 0
    assert days_between("fecha_mala", "2024-01-01") == 0
    assert days_between("2024-01-01", "mala") == 0