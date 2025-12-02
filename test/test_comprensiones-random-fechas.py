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


