import numpy as np

from proyecto import (
    scipy_root_cos_minus_x,
    scipy_integral_sin,
    interp_linear,
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


# --------------------------
# TEST interp_linear
# --------------------------
def test_interp_linear_basic():
    # Datos de prueba: relación lineal y = 2x
    x = [0.0, 1.0, 2.0]
    y = [0.0, 2.0, 4.0]

    # En xq = 1.5, la interpolación lineal debería dar 3.0
    xq = 1.5
    result = interp_linear(x, y, xq)
    assert abs(result - 3.0) < 1e-6


def test_interp_linear_extrapolate():
    # Comprobamos extrapolación lineal fuera del rango
    # Misma relación y = 2x
    x = [0.0, 1.0, 2.0]
    y = [0.0, 2.0, 4.0]

    # xq = 3.0 está fuera del rango [0, 2], pero con fill_value="extrapolate"
    # deberíamos obtener 6.0
    xq = 3.0
    result = interp_linear(x, y, xq)
    assert abs(result - 6.0) < 1e-6
