
def partition(a, low, high):
    pivot = a[high]
    i = low - 1

    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


# Test ham PARTITION
a = [7, 2, 9, 4, 5, 1, 8]

p = partition(a, 0, len(a) - 1)

print("Mang sau partition:", a)
print("Vi tri pivot:", p)


def quick_sort(a, low, high):
    if low < high:
        p = partition(a, low, high)

        quick_sort(a, low, p - 1)
        quick_sort(a, p + 1, high)


# Test Quick Sort
a = [7, 2, 9, 4, 5, 1, 8]

quick_sort(a, 0, len(a) - 1)

print("Mang sau khi sap xep:", a)



import random
import time

sizes = [1000, 2000, 4000, 8000, 16000]

print("Kich thuoc n | Thoi gian (giay)")
print("-" * 35)

for n in sizes:
    data = [random.randint(0, 100000) for _ in range(n)]

    start = time.perf_counter()

    quick_sort(data, 0, len(data) - 1)

    end = time.perf_counter()

    print(f"{n:12d} | {end - start:.6f}")
