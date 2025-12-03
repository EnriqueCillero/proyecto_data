import numpy as np

from proyecto import (
    scipy_root_cos_minus_x,
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



