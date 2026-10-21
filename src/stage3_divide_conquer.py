# ==================== src/stage3_divide_conquer.py ====================
"""
Stage 3 - Divide & Conquer
"""

from typing import List, Tuple
import time
from .utils import calculate_total_cost, calculate_total_fame, validate_tour


def solve_divide_conquer(
    n: int,
    locations: List[str],
    cost_matrix: List[List[float]],
    fame: List[int],
    budget: float
) -> Tuple[List[int], int, float, float]:
    """
    Chia de tri:
    1. Chia tap diem thanh cac cum (divide)
    2. Giai tung cum (conquer)
    3. Ghep cac tuyen con thanh tuyen hoan chinh (combine)
    - Dam bao tuyen cuoi cung hop le (khong lap, cost <= budget)
    - Tra ve: path, total_fame, total_cost, execution_time_ms
    """
    start_time = time.perf_counter()

    # TODO: TV6 + TV7 + TV8 implement o day
    # Co the viet them cac ham phu: divide_graph(), solve_sub_cluster(), combine_tours()

    path = [0]          # tam thoi
    total_fame = 0
    total_cost = 0.0

    execution_time_ms = (time.perf_counter() - start_time) * 1000
    return path, total_fame, total_cost, execution_time_ms