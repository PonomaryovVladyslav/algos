from heapq import heappush, heappop


def k_smallest_pairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    """
    Находит `k` наименьших пар `(nums1[i], nums2[j])` по их сумме.

    🔹 **Алгоритм (Min Heap)**:
       - Используем Min Heap (`heapq`) для хранения `k` наименьших пар.
       - Инициализируем кучу первыми `min(k, len(nums1))` парами `(nums1[i], nums2[0])`.
       - Каждый раз извлекаем минимальную сумму и добавляем следующую возможную пару `(nums1[i], nums2[j+1])`.

    🔹 **Временная сложность**:
       - `O(k log k)`, так как в куче `k` элементов, и мы `k` раз делаем `heappop` / `heappush` (`log k`).

    🔹 **Пространственная сложность**:
       - `O(k)`, так как храним `k` элементов в куче.

    :param nums1: list[int] - Первый отсортированный массив.
    :param nums2: list[int] - Второй отсортированный массив.
    :param k: int - Количество наименьших пар.
    :return: list[list[int]] - Список из `k` наименьших пар.
    """
    if not nums1 or not nums2 or k == 0:
        return []

    min_heap = []
    result = []

    # Инициализируем heap первыми `min(k, len(nums1))` парами (nums1[i], nums2[0])
    for i in range(min(k, len(nums1))):
        heappush(min_heap, (nums1[i] + nums2[0], i, 0))  # (сумма, индекс в nums1, индекс в nums2)

    while min_heap and len(result) < k:
        _, i, j = heappop(min_heap)
        result.append([nums1[i], nums2[j]])

        if j + 1 < len(nums2):  # Добавляем следующую пару `(nums1[i], nums2[j+1])`
            heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return result


# 🔹 Тесты
print(k_smallest_pairs([1, 7, 11], [2, 4, 6], 3))  # ✅ [[1,2], [1,4], [1,6]]
print(k_smallest_pairs([1, 1, 2], [1, 2, 3], 2))  # ✅ [[1,1], [1,1]]
print(k_smallest_pairs([1, 2], [3], 3))  # ✅ [[1,3], [2,3]]
print(k_smallest_pairs([1, 2, 3], [4, 5, 6], 5))  # ✅ [[1,4], [1,5], [1,6], [2,4], [2,5]]
