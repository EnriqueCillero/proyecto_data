import json
from proyecto import safe_divide, read_csv_sum_revenue, filter_customers_json


# --------------------------
# TEST safe_divide
# --------------------------
def test_safe_divide():
    assert safe_divide(10, 2) == 5
    assert safe_divide(5, 0) is None
    assert safe_divide(10, -2) == -5
    assert safe_divide("x", 2) is None 


# --------------------------
# TEST read_csv_sum_revenue
# --------------------------
def test_read_csv_sum_revenue(tmp_path):
    # Crear un CSV temporal con units_sold y unit_price
    csv_file = tmp_path / "ventas.csv"

    with open(csv_file, "w", encoding="utf-8") as f:
        f.write("units_sold,unit_price\n")
        f.write("2,10\n")     # 20
        f.write("3,5\n")      # 15
        f.write("-1,4\n")     # ignorado (negativo)
        f.write("x,2\n")      # ignorado (no numérico)

    result = read_csv_sum_revenue(str(csv_file))

    assert result == 35  # 20 + 15