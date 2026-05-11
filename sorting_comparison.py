import random
import timeit


# Сортування вставками
# O(n^2)
def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# Сортування злиттям
# O(n log n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Генерація даних
def generate_data(n):
    return [random.randint(0, 10000) for _ in range(n)]

# Тестування часу
def test_algorithms():
    sizes = [100, 500, 1000, 5000]

    for n in sizes:
        data = generate_data(n)

        print(f"\n📊 Розмір масиву: {n}")

        # Insertion sort
        t1 = timeit.timeit(lambda: insertion_sort(data), number=3)

        # Merge sort
        t2 = timeit.timeit(lambda: merge_sort(data), number=3)

        # Timsort (sorted)
        t3 = timeit.timeit(lambda: sorted(data), number=3)

        print(f"Insertion sort: {t1:.6f} сек")
        print(f"Merge sort:     {t2:.6f} сек")
        print(f"Timsort:        {t3:.6f} сек")


if __name__ == "__main__":
    test_algorithms()