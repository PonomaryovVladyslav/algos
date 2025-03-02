def summary_ranges(nums: list[int]) -> list[str]:
    """
    Генерирует компактное представление диапазонов для отсортированного списка уникальных чисел.

    🔹 **Алгоритм**:
       1️⃣ Итерируемся по `nums`, отслеживая начало диапазона `start`.
       2️⃣ Если находим разрыв (текущий элемент != предыдущий + 1), добавляем диапазон.
       3️⃣ В конце добавляем последний диапазон.

    🔹 **Временная сложность**:
       - `O(n)`, так как один проход по `nums`.

    🔹 **Пространственная сложность**:
       - `O(1)`, так как храним только результат.

    :param nums: list[int] - Отсортированный список уникальных чисел.
    :return: list[str] - Список диапазонов в строковом формате.
    """
    if not nums:
        return []

    result = []
    start = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:  # Разрыв в последовательности
            result.append(f"{start}->{nums[i - 1]}" if start != nums[i - 1] else f"{start}")
            start = nums[i]  # Новый диапазон

    # Добавляем последний диапазон
    result.append(f"{start}->{nums[-1]}" if start != nums[-1] else f"{start}")

    return result


# 🔹 Тесты
print(summary_ranges([0, 1, 2, 4, 5, 7]))  # ✅ ["0->2", "4->5", "7"]
print(summary_ranges([0, 2, 3, 4, 6, 8, 9]))  # ✅ ["0", "2->4", "6", "8->9"]
print(summary_ranges([]))  # ✅ []
print(summary_ranges([1]))  # ✅ ["1"]
print(summary_ranges([1, 2]))  # ✅ ["1->2"]
print(summary_ranges([-5, -4, -3, -1, 1, 2, 3, 5, 6, 7, 8, 10]))
# ✅ ["-5->-3", "-1", "1->3", "5->8", "10"]
