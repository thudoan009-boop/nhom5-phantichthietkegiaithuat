
import random
import time
import csv
import statistics


def partition(a, low, high):
    pivot = a[high]
    i = low - 1

    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def quick_sort_iterative(a):
    if len(a) < 2:
        return

    stack = [(0, len(a) - 1)]

    while stack:
        low, high = stack.pop()

        while low < high:
            p = partition(a, low, high)

            # Xử lý phần nhỏ hơn ngay, lưu phần lớn hơn vào stack
            if p - low < high - p:
                if p + 1 < high:
                    stack.append((p + 1, high))
                high = p - 1
            else:
                if low < p - 1:
                    stack.append((low, p - 1))
                low = p + 1


def make_data(n, data_type, seed=42):
    if data_type == "Ngau nhien":
        rng = random.Random(seed)
        return [rng.randint(0, 100000) for _ in range(n)]
    if data_type == "Tang dan":
        return list(range(n))
    if data_type == "Giam dan":
        return list(range(n, 0, -1))
    raise ValueError("Loai du lieu khong hop le")


def main():
    sizes = [1000, 2000, 4000, 8000, 16000]
    data_types = ["Ngau nhien", "Tang dan", "Giam dan"]
    repeats = 3
    results = []

    for data_type in data_types:
        for n in sizes:
            times = []

            for run in range(repeats):
                data = make_data(n, data_type, seed=42 + run)

                start = time.perf_counter()
                quick_sort_iterative(data)
                elapsed = time.perf_counter() - start

                assert data == sorted(data), "Ket qua sap xep sai!"
                times.append(elapsed)

            avg_time = statistics.mean(times)
            results.append({
                "Loai du lieu": data_type,
                "Kich thuoc n": n,
                "Thoi gian trung binh (giay)": avg_time,
                "So lan lap": repeats
            })

            print(
                f"{data_type:12} | n={n:5} | "
                f"trung binh={avg_time:.6f} giay"
            )

    with open(
        "benchmark_quicksort.csv",
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print("\nDa luu ket qua vao benchmark_quicksort.csv")


if __name__ == "__main__":
    main()
