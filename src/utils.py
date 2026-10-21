# ==================== src/utils.py ====================
"""
Module tien ich dung chung
"""

from typing import List, Tuple
import os


def load_data(file_path: str) -> Tuple[int, List[str], List[List[float]], List[int], float]:
    """
    Doc file input.txt va kiem tra du lieu.
    Tra ve: n, locations, cost_matrix, fame, budget
    """
    # TODO: TV1 - Doc file + kiem tra du lieu hop le
    # Neu loi thi raise Exception ro rang
    pass


def calculate_total_cost(path: List[int], cost_matrix: List[List[float]]) -> float:
    """Tinh tong chi phi cua tuyen (da bao gom quay ve 0)"""
    # TODO: TV1
    pass


def calculate_total_fame(path: List[int], fame: List[int]) -> int:
    """Tinh tong do noi tieng (khong tinh diem 0 o cuoi)"""
    # TODO: TV1
    pass


def validate_tour(path: List[int], n: int, cost_matrix: List[List[float]], budget: float) -> bool:
    """
    Kiem tra tuyen hop le:
    - Bat dau va ket thuc tai 0
    - Khong lap diem
    - total_cost <= budget
    """
    # TODO: TV1
    pass