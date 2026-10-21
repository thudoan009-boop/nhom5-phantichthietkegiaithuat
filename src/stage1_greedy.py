# ==================== src/stage1_greedy.py ====================
"""
Stage 1 - Greedy theo ti le fame / cost
"""

from typing import List, Tuple
import time
from .utils import calculate_total_cost, calculate_total_fame, validate_tour


def solve_greedy(
    n: int,
    locations: List[str],
    cost_matrix: List[List[float]],
    fame: List[int],
    budget: float
) -> Tuple[List[int], int, float, float]:
    """
    Thuat toan Greedy:
    - Bat dau tu 0
    - Moi buoc chon diem co fame/cost cao nhat ma van quay ve duoc trong budget
    - Tra ve: path, total_fame, total_cost, execution_time_ms
    """
    start_time = time.perf_counter()

    # TODO: TV2 + TV3 implement thuat toan Greedy o day

    path = [0]          # tam thoi
    total_fame = 0
    total_cost = 0.0

    execution_time_ms = (time.perf_counter() - start_time) * 1000
    return path, total_fame, total_cost, execution_time_ms