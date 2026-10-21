"""
File main.py - Menu dieu khien toan bo du an TSP / Orienteering
"""

import sys
import os

# Them thu muc goc vao path de import duoc package src
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.utils import load_data, validate_tour
from src.stage1_greedy import solve_greedy
from src.stage2_bruteforce import solve_bruteforce
from src.stage3_divide_conquer import solve_divide_conquer


def print_result(stage_name, path, total_fame, total_cost, exec_time, locations, budget):
    """
    Ham in ket qua ra man hinh theo dinh dang thong nhat
    """
    print("=" * 60)
    print(f"[STAGE] {stage_name}")
    print("=" * 60)
    print(f"Ngan sach       : {budget:,.0f} VND")
    print(f"Lo trinh chi so : {' -> '.join(map(str, path))}")

    # Chuyen chi so thanh ten dia diem
    loc_names = [locations[i] for i in path]
    print(f"Lo trinh dia diem: {' -> '.join(loc_names)}")
    print(f"Tong do noi tieng: {total_fame}")
    print(f"Tong chi phi     : {total_cost:,.0f} VND")
    print(f"Thoi gian thuc thi: {exec_time:.4f} ms")
    print("=" * 60)


def run_benchmark(n, locations, cost_matrix, fame, budget):
    """
    Chay ca 3 thuat toan tren cung mot bo du lieu va so sanh
    """
    print("\n>>> BAT DAU BENCHMARK CA 3 THUAT TOAN <<<\n")

    results = []

    # Danh sach thuat toan can chay
    algorithms = [
        ("1. Greedy", solve_greedy),
        ("2. Brute Force", solve_bruteforce),
        ("3. Divide & Conquer", solve_divide_conquer),
    ]

    for name, func in algorithms:
        path, fame_val, cost, t = func(n, locations, cost_matrix, fame, budget)
        valid = validate_tour(path, n, cost_matrix, budget)
        results.append((name, path, fame_val, cost, t, valid))

        print_result(name, path, fame_val, cost, t, locations, budget)
        print(f"-> Tuyen hop le: {'Co' if valid else 'KHONG'}\n")

    # In bang tom tat so sanh
    print("\n=== TOM TAT SO SANH ===")
    print(f"{'Thuat toan':<22} {'Fame':>6} {'Cost':>12} {'Time (ms)':>10} {'Valid':>6}")
    print("-" * 60)
    for name, _, f, c, t, v in results:
        print(f"{name:<22} {f:>6} {c:>12,.0f} {t:>10.4f} {str(v):>6}")


def main():
    """
    Ham chinh: load du lieu va hien thi menu
    """
    data_path = os.path.join("tests", "input.txt")

    # Doc du lieu dau vao
    try:
        n, locations, cost_matrix, fame, budget = load_data(data_path)
        print(f"Da load du lieu thanh cong: N = {n}, Budget = {budget:,.0f} VND")
        print(f"Dia diem: {', '.join(locations)}\n")
    except Exception as e:
        print(f"[LOI] Khong the doc du lieu: {e}")
        return

    # Vong lap menu
    while True:
        print("\n================ TSP PROJECT ================")
        print("1. Chay Stage 1 - Greedy")
        print("2. Chay Stage 2 - Brute Force / Backtracking")
        print("3. Chay Stage 3 - Divide & Conquer")
        print("4. Benchmark ca 3 thuat toan")
        print("0. Thoat")
        print("=============================================")

        choice = input("Nhap lua chon: ").strip()

        if choice == "0":
            print("Tam biet!")
            break

        elif choice == "1":
            path, f, c, t = solve_greedy(n, locations, cost_matrix, fame, budget)
            print_result("GREEDY (FAME / COST)", path, f, c, t, locations, budget)

        elif choice == "2":
            path, f, c, t = solve_bruteforce(n, locations, cost_matrix, fame, budget)
            print_result("BRUTE FORCE / BACKTRACKING", path, f, c, t, locations, budget)

        elif choice == "3":
            path, f, c, t = solve_divide_conquer(n, locations, cost_matrix, fame, budget)
            print_result("DIVIDE & CONQUER", path, f, c, t, locations, budget)

        elif choice == "4":
            run_benchmark(n, locations, cost_matrix, fame, budget)

        else:
            print("Lua chon khong hop le, vui long nhap lai.")


if __name__ == "__main__":
    main()