import numpy as np
from proyecto import numpy_vector_length, numpy_minmax_scale


# --------------------------
# TEST numpy_vector_length
# --------------------------
def test_numpy_vector_length_basic():
    # vector [3, 4] → norma 5
    assert numpy_vector_length([3, 4]) == 5.0

def test_numpy_vector_length_zero():
    # vector [0, 0] → norma 0
    assert numpy_vector_length([0, 0]) == 0.0

def test_numpy_vector_length_negative():
    # norma siempre positiva
    assert numpy_vector_length([-3, -4]) == 5.0

def test_numpy_vector_length_invalid_input():
    # error → retorna 0.0 según la implementación
    assert numpy_vector_length(["a", 2]) == 0.0


# --------------------------
# TEST numpy_minmax_scale
# --------------------------
def test_numpy_minmax_scale_basic():
    # min=1, max=3 → [0, 0.5, 1]
    assert numpy_minmax_scale([1, 2, 3]) == [0.0, 0.5, 1.0]

def test_numpy_minmax_scale_negative():
    # min=-1, max=1 → normalización simétrica
    assert numpy_minmax_scale([-1, 0, 1]) == [0.0, 0.5, 1.0]

def test_numpy_minmax_scale_all_equal():
    # caso especial: diff == 0 → todo 0.0
    assert numpy_minmax_scale([5, 5, 5]) == [0.0, 0.0, 0.0]

def test_numpy_minmax_scale_invalid_input():
    # error → lista de ceros según implementación
    assert numpy_minmax_scale(["x", 1, 2]) == [0.0, 0.0, 0.0]
