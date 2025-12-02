import random
from proyecto import squares_of_odds, random_color, days_between


# --------------------------
# TEST squares_of_odds
# --------------------------
def test_squares_of_odds():
    assert squares_of_odds([1, 2, 3, 4, 5]) == [1, 9, 25]
    assert squares_of_odds([]) == []
    assert squares_of_odds([2, 4, 6]) == []        # todos pares
    assert squares_of_odds([1]) == [1]


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
