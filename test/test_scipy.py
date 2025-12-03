import numpy as np

from proyecto import (
    scipy_root_cos_minus_x,
    scipy_integral_sin,
)


# --------------------------
# TEST scipy_root_cos_minus_x
# --------------------------
def test_scipy_root_cos_minus_x():
    # Obtenemos la raíz aproximada de cos(x) - x
    root = scipy_root_cos_minus_x()

    # Comprobamos que f(root) = cos(root) - root ≈ 0
    value = np.cos(root) - root
    assert abs(value) < 1e-6


# --------------------------
# TEST scipy_integral_sin
# --------------------------
def test_scipy_integral_sin():
    # Integral de sin(x) entre 0 y pi debe ser exactamente 2
    result = scipy_integral_sin()
    assert abs(result - 2.0) < 1e-6