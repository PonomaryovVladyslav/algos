def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Объединяет пересекающиеся интервалы.

    🔹 **Алгоритм**:
       1️⃣ Сортируем интервалы по начальному значению.
       2️⃣ Проходим по отсортированным интервалам:
          - Если текущий интервал пересекается с последним в `merged`, объединяем.
          - Иначе, добавляем как новый интервал.

    🔹 **Временная сложность**:
       - `O(n log n)`, так как требуется сортировка.
       - `O(n)`, так как один проход по отсортированному списку.

    🔹 **Пространственная сложность**:
       - `O(n)`, так как создаём новый список.

    :param intervals: list[list[int]] - Список интервалов `[start, end]`.
    :return: list[list[int]] - Список объединённых интервалов.
    """
    if not intervals:
        return []

    # 1️⃣ Сортируем по начальному значению (O(n log n))
    intervals.sort()

    merged = [intervals[0]]  # Начинаем с первого интервала

    for start, end in intervals[1:]:
        last_end = merged[-1][1]  # Конец последнего интервала в `merged`

        if start <= last_end:  # Пересечение → объединяем
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])  # Нет пересечения → новый интервал

    return merged


# 🔹 Тесты
print(merge_intervals([[1, 4], [5, 6]]))  # ✅ [[1, 4], [5, 6]]
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # ✅ [[1, 6], [8, 10], [15, 18]]
print(merge_intervals([[1, 4], [4, 5]]))  # ✅ [[1, 5]]
print(merge_intervals([[1, 10], [2, 6], [8, 10], [15, 18]]))  # ✅ [[1, 10], [15, 18]]
print(merge_intervals([]))  # ✅ []
print(merge_intervals([[1, 5]]))  # ✅ [[1, 5]]
