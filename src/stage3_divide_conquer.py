# ==================== src/stage3_divide_conquer.py ====================
"""
Stage 3 - Divide & Conquer
"""

from typing import List, Tuple
import time
from .utils import calculate_total_cost, calculate_total_fame, validate_tour

""" 
TV5 Ma trận chi phí cost[i][j] kích thước N × N và mảng fame, budget từ Task 1.1.
"""
def divide_graph(n: int, cost_matrix: List[List[float]], fame: List[int], budget: float):
    """
    Divide step: Chia cac diem (1..n-1) thanh 2 cum, trich xuat cost matrix, fame array va phan bo budget.
    """
    points = list(range(1, n))
    mid = len(points) // 2
    
    # Danh sach ID diem cua 2 cum (khong gom diem 0 de tranh trung lap khi giai noi cum)
    nodes_A = points[:mid]
    nodes_B = points[mid:]
    
    # Trich xuat mang fame con cho tung cum
    fame_A = [fame[i] for i in nodes_A]
    fame_B = [fame[i] for i in nodes_B]
    
    # Trich xuat ma tran chi phi con
    def extract_sub_matrix(nodes):
        size = len(nodes)
        sub_matrix = [[0.0] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                sub_matrix[i][j] = cost_matrix[nodes[i]][nodes[j]]
        return sub_matrix

    cost_A = extract_sub_matrix(nodes_A)
    cost_B = extract_sub_matrix(nodes_B)
    
    # Danh khoang 20% ngan sach cho buoc combine
    reserve_budget = budget * 0.2
    available_budget = budget - reserve_budget
    
    sum_fame_A = sum(fame_A)
    sum_fame_B = sum(fame_B)
    total_fame = sum_fame_A + sum_fame_B
    
    if total_fame > 0:
        budget_A = (sum_fame_A / total_fame) * available_budget
        budget_B = (sum_fame_B / total_fame) * available_budget
    else:
        budget_A = available_budget / 2.0
        budget_B = available_budget / 2.0
        
    # Ban giao day du: nodes, cost_sub, fame_sub, budget_sub cho TV6
    cluster_A = (nodes_A, cost_A, fame_A, budget_A)
    cluster_B = (nodes_B, cost_B, fame_B, budget_B)
    
    return cluster_A, cluster_B

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