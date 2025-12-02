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
    # Creaamos un CSV temporal con units_sold y unit_price
    csv_file = tmp_path / "ventas.csv"

    with open(csv_file, "w", encoding="utf-8") as f:
        f.write("units_sold,unit_price\n")
        f.write("2,10\n")     # 20
        f.write("3,5\n")      # 15
        f.write("-1,4\n")     # ignorado (negativo)
        f.write("x,2\n")      # ignorado (no numérico)

    result = read_csv_sum_revenue(str(csv_file))

    assert result == 35  # 20 + 15


# --------------------------
# TEST filter_customers_json
# --------------------------
def test_filter_customers_json(tmp_path):
    # Crear JSON de entrada
    in_file = tmp_path / "clientes.json"
    out_file = tmp_path / "clientes_filtrados.json"

    clientes = [
        {"email": "ana@example.com", "age": 25},
        {"email": "invalido", "age": 30},            # sin @ → descartado
        {"email": "pepe@example.com", "age": -1},     # age inválida → descartado
        {"email": "luis@example.com", "age": 40}
    ]

    with open(in_file, "w", encoding="utf-8") as f:
        json.dump(clientes, f)

    count = filter_customers_json(str(in_file), str(out_file))

    # Deben pasar solo Ana (25) y Luis (40)
    assert count == 2

    # Verificar que realmente se escribieron los clientes correctos
    with open(out_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["email"] == "ana@example.com"
    assert data[1]["email"] == "luis@example.com"