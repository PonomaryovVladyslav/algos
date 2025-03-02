def insert_interval(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    """
    Вставляет новый интервал в список интервалов и объединяет пересекающиеся интервалы.

    🔹 **Алгоритм**:
       - **Шаг 1**: Добавляем все интервалы, которые идут до `new_interval` без изменений.
       - **Шаг 2**: Объединяем пересекающиеся интервалы с `new_interval`.
       - **Шаг 3**: Добавляем все оставшиеся интервалы после `new_interval`.

    🔹 **Временная сложность**:
       - `O(n)`, так как мы проходим по списку `intervals` один раз.

    🔹 **Пространственная сложность**:
       - `O(n)`, так как мы храним результат в отдельном списке.

    :param intervals: list[list[int]] - Отсортированные интервалы `[start, end]`.
    :param new_interval: list[int] - Новый интервал `[start, end]` для вставки.
    :return: list[list[int]] - Список объединённых интервалов.
    """
    result = []
    i = 0
    n = len(intervals)

    # 1️⃣ Добавляем все интервалы, которые идут ДО `new_interval`
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # 2️⃣ Объединяем пересекающиеся интервалы с `new_interval`
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)  # Добавляем объединённый интервал

    # 3️⃣ Добавляем оставшиеся интервалы
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


# 🔹 Тесты
print(insert_interval([[1, 3], [6, 9]], [2, 5]))  # ✅ [[1,5],[6,9]]
print(insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # ✅ [[1,2],[3,10],[12,16]]
print(insert_interval([], [5, 7]))  # ✅ [[5,7]]
print(insert_interval([[1, 5]], [2, 3]))  # ✅ [[1,5]]
print(insert_interval([[1, 5]], [6, 8]))  # ✅ [[1,5], [6,8]]
