"""
Práctica Unidades 1 y 2 — PROYECTOS II

Instrucciones generales:
- Este archivo se completará por etapas en distintas ramas de Git.
- NO cambies los nombres de las funciones ni sus parámetros.
- Puedes añadir funciones auxiliares si lo necesitas.
- Al finalizar, todas las funciones deben estar implementadas y probadas (puedes ejecutar tests propios).
"""

# === IMPORTS (añade otros si son necesarios) ===
import csv, json, os, random, math
from datetime import datetime
from typing import List, Dict, Optional

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize, integrate, interpolate

# 1) Básicos y cadenas
def sum_even(nums: List[int]) -> int:
    """Suma los enteros pares de la lista. Si no hay pares, devuelve 0."""
    return sum(n for n in nums if n % 2 == 0)


def normalize_str(s: str) -> str:
    """Devuelve s sin espacios al inicio/fin y en minúsculas."""
    return s.strip().lower()


def count_words(text: str) -> Dict[str,int]:
    """
    Devuelve un dict palabra->frecuencia.
    Reglas: separa por espacios; elimina . , ; : ! ? al final de cada token; ignora mayúsculas.
    """
    trailing = ".,;:!?"

    tokens = text.split()
    counts: Dict[str, int] = {}

    for token in tokens:
        cleaned = token.rstrip(trailing).lower()

        if cleaned == "":
            continue

        counts[cleaned] = counts.get(cleaned, 0) + 1

    return counts


# 2) Ficheros y excepciones
def safe_divide(a: float, b: float) -> Optional[float]:
    """Devuelve a/b. Si b==0 o hay error, devuelve None."""
    try:
        if b == 0:
            return None
        return a / b
    except Exception:
        return None


def read_csv_sum_revenue(path: str) -> float:
    """
    Lee un CSV con columnas units_sold y unit_price.
    Convierte a numérico; ignora NaN o negativos; suma units_sold*unit_price.
    """
    import csv

    total = 0.0

    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)

            # Saltamos la cabecera
            header = next(reader, None)

            for row in reader:
                if len(row) < 2:
                    continue  # fila inválida, no contiene todos los datos

                try:
                    units = float(row[0])
                    price = float(row[1])

                    # Ignoramos negativos, no tiene sentido que tegamos stock negativo o precios negativos
                    if units < 0 or price < 0:
                        continue

                    total += units * price

                except Exception:
                    # Ignoranamos excepciones generales durante la conversión
                    continue

        return total

    except FileNotFoundError:
        # En caso de encontrar el archivo, devolvemos 0
        return 0.0
    except Exception:
        # En caso de excepción devolvemos 0
        return 0.0


def filter_customers_json(in_path: str, out_path: str) -> int:
    """
    JSON (lista de objetos con email y age).
    Escribe en out_path solo clientes con email que contenga '@' y age > 0.
    Devuelve el número de clientes escritos.
    """
    try:
        # Leemos el JSON de entrada
        with open(in_path, "r", encoding="utf-8") as f:
             # Cargamos el JSON en un diccionario
            data = json.load(f)    

        valid_customers = []

        # Recorremos y filtramos la información
        for customer in data:
            email = customer.get("email", "")
            age = customer.get("age", 0)

            # Filtramos por las condiciones expuestas en el enunciado
            if "@" in email and age > 0:
                valid_customers.append(customer)

        # Escribimos el resultado en path de salida
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(valid_customers, f)

        # Devolvemos la longituad de la lista que hemos creado a partir de los filtros
        return len(valid_customers)

    except FileNotFoundError:
        # Informamos al usurio del error
        print("Error: Archivo no encontrado")
        # Archivo no encontrado, retornamos 0
        return 0
    except json.JSONDecodeError:
        # Informamos al usurio del error
        print("Error: Json inválido")
        # JSON inválido, retornamos 0 
        return 0
    except Exception:
        # Informamos al usurio del error
        print("Error desconocido durate el filtrado de datos")
        # Error general, retornamos 0
        return 0


# 3) Comprensiones, random, datetime
def squares_of_odds(n: int) -> List[int]:
    """Lista de cuadrados de impares 1..n (ambos inclusive)."""
    """
    Usando list comprehensión, recorremos la lista elevando al cuadrado cada elemento
    y luego sacamos el módulo 2 para saber si par o no, devolviendo el resultado en la misma linea
    """
    return [x**2 for x in n if x % 2 != 0]


def random_color(seed: int) -> str:
    """Fija random.seed(seed) y retorna un color aleatorio de ['rojo','azul','verde']."""

    # Fijamos la semilla
    random.seed(seed)
    
    # Definimos la lista de posible opciones
    colores = ["rojo", "azul", "verde"]

    # Usando la libreria random devolvemos un resultado.
    return random.choice(colores)


def days_between(d1: str, d2: str) -> int:
    """Recibe fechas 'YYYY-MM-DD'. Devuelve abs(d2-d1) en días (entero)."""
    try:
        # Intentamos convertir la fecha en el formato indicado al formato datetime de python
        f1 = datetime.strptime(d1, "%Y-%m-%d")
        f2 = datetime.strptime(d2, "%Y-%m-%d")

        # Restamos la fecha, obetieniendo un timedelta
        diff = f2 - f1

        # Retornamos el resultado absoluto de la resta para no tener que ordenar la fechas
        return abs(diff.days)
    except Exception:
        # En caso de error de coversion, deveolvemos un 0 e informamos al usuario
        print("Error durante la conversión de las fechas provistas")
        return 0


# 4) NumPy
def numpy_vector_length(v: List[float]) -> float:
    """Norma Euclídea de v con NumPy."""
    try:
        # Convertimos la lista de Python a un array de NumPy
        arr = np.array(v, dtype=float)

        # Calculamos la norma Euclídea usando np.linalg.norm
        return float(np.linalg.norm(arr))

    except Exception:
        print("Error calculando la norma del vector con NumPy")
        return 0.0


def numpy_minmax_scale(arr: List[float]) -> List[float]:
    """
    Normaliza a [0,1]. Si todos los valores son iguales, devuelve todos 0.0.
    """
    try:
        # Convertimos la lista a array NumPy
        vec = np.array(arr, dtype=float)

        # Calculamos mínimo y máximo
        min_val = np.min(vec)
        max_val = np.max(vec)
        diff = max_val - min_val

        # Delvolvemos 0 en caso no haber diferencia entre min y max
        if diff == 0:
            return [0.0 for _ in arr]

        # Normalización vectorizada
        scaled = (vec - min_val) / diff

        # Devolvemos una lista
        return scaled.tolist()

    except Exception:
        print("Error durante la normalización min-max")
        return [0.0 for _ in arr]


# 5) SciPy
def scipy_root_cos_minus_x() -> float:
    """Raíz de f(x)=cos(x)-x con optimize.root, x0=0.5."""
    try:
        # Definimos la funcion lambda y la guardamos en una variable
        f = lambda x: np.cos(x) - x

        # Utilizamos la funcion de scipy para en encontrar un valor en la función f(x) y le pasamos el valor incial indicado
        sol = optimize.root(f, x0=0.5)

        # Retornamos el primer valor del vector casteado a float como se indica en la función
        return float(sol.x[0])
    
    except Exception:
        print("Error calculando la raíz con SciPy")
        # Por seguir un poco la linea de el resto de funciones, devolvemos 0
        return 0.0


def scipy_integral_sin() -> float:
    """Integral de sin(x) de 0 a pi con integrate.quad. Devuelve el área."""
    try:
        # Calculamos la integral definidoa de la funcion np.sin, usando de límites 0 y np.pi y lo guardamos en una tupla
        result, _ = integrate.quad(np.sin, 0, np.pi)

        # Devolvemos solo el resultado sin el error estimado con el tipo de la cabecera
        return float(result)
    
    except Exception:
        # En caso de error, devolvemos 0 e informamos al usuario
        print("Error calculando la integral con SciPy")
        return 0.0

def interp_linear(x: List[float], y: List[float], xq: float) -> float:
    """Interpolación lineal: devuelve f(xq) usando interpolate.interp1d."""
    pass

# 6) Visualización
def plot_line_time_series(xs: List[float], ys: List[float], out_path: str) -> bool:
    """
    Dibuja línea con título y etiquetas. Guarda en out_path y devuelve True si existe.
    """
    pass

def plot_bar(categories: List[str], values: List[float], out_path: str) -> bool:
    """Barras con etiquetas. Guarda y devuelve True si existe."""
    pass

def plot_scatter(x: List[float], y: List[float], out_path: str) -> bool:
    """Dispersión con grid y legend (usa label). Guarda y devuelve True si existe."""
    pass

# 7) POO
class Vector2D:
    """
    Implementa:
      - __init__(x, y)
      - __add__(other): suma vectorial, devuelve Vector2D
      - __eq__(other): igualdad por componentes
      - __repr__(): 'Vector2D(x=?, y=?)'
      - length(self) -> float: norma Euclídea
    """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: "Vector2D") -> "Vector2D":
        """Suma vectorial."""
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other: object) -> bool:
        """Igualdad por componentes."""
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        """Representación legible del vector."""
        return f"Vector2D(x={self.x}, y={self.y})"

    def length(self) -> float:
        """Norma euclídea: sqrt(x^2 + y^2)."""
        try:
            # Convertimos a np.array
            vec = np.array([self.x, self.y], dtype=float)

            # Devolvemos el valor
            return float(np.linalg.norm(vec))
        except Exception:
            # En caso de error, devolvemos 0
            return 0.0
