from proyecto import sum_even, normalize_str, count_words

def test_sum_even():
    assert sum_even([1, 2, 3, 4, 6]) == 12
    assert sum_even([1, 3, 5]) == 0
    assert sum_even([]) == 0


def test_normalize_str():
    assert normalize_str("  HoLA  ") == "hola"
    assert normalize_str("MUNDO") == "mundo"
    assert normalize_str("\t Espacio \n") == "espacio"


def test_count_words():
    text = "Hola hola, HOLA!! adiós?"
    expected = {"hola": 3, "adiós": 1}
    assert count_words(text) == expected

    assert count_words("uno, dos; tres tres tres.") == {
        "uno": 1,
        "dos": 1,
        "tres": 3
    }

    # word with only symbols ignored
    assert count_words("!!! ??? ...") == {}