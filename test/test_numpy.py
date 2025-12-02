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



