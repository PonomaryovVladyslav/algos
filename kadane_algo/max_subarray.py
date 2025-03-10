def max_subarray(nums: list[int]) -> int:
    """
    Находит подмассив с максимальной суммой с использованием алгоритма Кадане.

    🔹 **Алгоритм (Kadane's Algorithm)**:
       - Итерируемся по массиву и накапливаем `cur_sum` (текущая сумма).
       - Если `cur_sum` < 0, сбрасываем (`cur_sum = 0`), так как отрицательные суммы ухудшают результат.
       - Обновляем `max_sum` при каждом шаге.

    🔹 **Временная сложность**:
       - `O(n)`, так как один проход по массиву.

    🔹 **Пространственная сложность**:
       - `O(1)`, так как используются только 2 переменные (`cur_sum` и `max_sum`).

    :param nums: list[int] - Входной массив.
    :return: int - Максимальная сумма подмассива.
    """
    max_sum = float('-inf')  # Минимальное начальное значение
    cur_sum = 0

    for num in nums:
        cur_sum += num
        max_sum = max(max_sum, cur_sum)  # Обновляем максимум
        if cur_sum < 0:
            cur_sum = 0  # Если текущая сумма отрицательна — сбрасываем

    return max_sum


# 🔹 Тесты
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # ✅ 6
print(max_subarray([1]))  # ✅ 1
print(max_subarray([5, 4, -1, 7, 8]))  # ✅ 23
print(max_subarray([-1, -2, -3, -4]))  # ✅ -1 (возвращаем макс. число)
print(max_subarray([2, -1, 2, 3, 4, -5, 1]))  # ✅ 10
