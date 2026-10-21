# ==================== src/stage2_bruteforce.py ====================
"""
Stage 2 - Brute Force / DFS Backtracking + Nhanh can
"""

from typing import List, Tuple
import time
from .utils import calculate_total_cost, calculate_total_fame, validate_tour


def solve_bruteforce(
    n: int,
    locations: List[str],
    cost_matrix: List[List[float]],
    fame: List[int],
    budget: float
) -> Tuple[List[int], int, float, float]:
    """
    DFS + Backtracking:
    - Xet moi tap con hop le (khong bat buoc di het)
    - Dung nhanh can de cat nhanh
    - Muc tieu: max total_fame, neu bang thi min total_cost
    - Tra ve: path, total_fame, total_cost, execution_time_ms
    """
    start_time = time.perf_counter()

    # TODO: TV4 + TV5 implement DFS + nhanh can o day

    path = [0]          # tam thoi
    total_fame = 0
    total_cost = 0.0

    execution_time_ms = (time.perf_counter() - start_time) * 1000
    return path, total_fame, total_cost, execution_time_ms