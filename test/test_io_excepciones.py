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


