import os
from pathlib import Path
from proyecto import plot_line_time_series, plot_bar, plot_scatter



# Guardamos el path base que queremos utilizar y creamos la carpeta
BASE_PATH = Path(__file__).resolve().parent.parent
FIGURES = BASE_PATH / "figures"
FIGURES.mkdir(exist_ok=True)


# --------------------------
# TEST plot_line_time_series
# --------------------------
def test_plot_line_time_series():
    out_path =  FIGURES / "test_line.png"

    xs = [0, 1, 2, 3]
    ys = [10, 15, 8, 20]

    result = plot_line_time_series(xs, ys, out_path)

    # Debe devolver True y el archivo debe existir
    assert result is True
    assert os.path.exists(out_path)


# --------------------------
# TEST plot_bar
# --------------------------
def test_plot_bar():
    out_path = FIGURES/ "test_bar.png"

    categories = ["A", "B", "C"]
    values = [5, 10, 7]

    result = plot_bar(categories, values, out_path)

    # Debe devolver True y el archivo debe existir
    assert result is True
    assert os.path.exists(out_path)


# --------------------------
# TEST plot_scatter
# --------------------------
def test_plot_scatter():
    out_path = FIGURES / "test_scatter.png"

    x = [1, 2, 3, 4]
    y = [2, 4, 6, 8]

    result = plot_scatter(x, y, out_path)

    # Debe devolver True y el archivo debe existir
    assert result is True
    assert os.path.exists(out_path)
