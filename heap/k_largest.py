from heapq import heappush, heappop


def find_kth_largest(nums: list[int], k: int) -> int:
    """
    Находит `k`-й наибольший элемент в списке `nums` с помощью Min-Heap.

    🔹 **Алгоритм (Min Heap)**:
       - Используем Min Heap (`heapq`) размером `k`.
       - Перебираем все числа, добавляя их в кучу.
       - Если размер кучи превышает `k`, удаляем минимальный элемент (`heappop`).
       - В итоге, в куче остаётся `k` наибольших элементов, а `heap[0]` — `k`-й наибольший.

    🔹 **Временная сложность**:
       - `O(n log k)`, так как добавление в кучу (`heappush` / `heappop`) — `O(log k)`,
         а мы делаем это `n` раз.

    🔹 **Пространственная сложность**:
       - `O(k)`, так как в куче хранится `k` элементов.

    :param nums: list[int] - Входной список чисел.
    :param k: int - Порядковый номер наибольшего элемента.
    :return: int - `k`-й наибольший элемент в `nums`.
    """
    min_heap = []

    for num in nums:
        heappush(min_heap, num)
        if len(min_heap) > k:
            heappop(min_heap)  # Удаляем минимальный элемент, если размер > k

    return min_heap[0]  # Корень кучи — k-й наибольший элемент


# 🔹 Тесты
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # ✅ 5
print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # ✅ 4
print(find_kth_largest([1], 1))  # ✅ 1
print(find_kth_largest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 3))  # ✅ 8
