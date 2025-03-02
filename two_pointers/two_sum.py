def two_sum(numbers: list[int], target: int) -> list[int]:
    """
    Найти два числа в отсортированном массиве, сумма которых равна `target`.
    Индексы должны начинаться с 1.

    Вход:
    numbers = [2, 7, 11, 15]
    target = 9

    Выход:
    [1, 2]  (так как 2 + 7 = 9)

    Решение:
    - Используем два указателя `left` (начало) и `right` (конец).
    - Если сумма меньше `target`, сдвигаем `left` вправо.
    - Если сумма больше `target`, сдвигаем `right` влево.
    - Если сумма равна `target`, возвращаем индексы (с учетом 1-based индексации).

    Время: O(n) — один проход по массиву.
    Пространство: O(1) — используем только указатели.
    """

    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # 1-based индексация
        elif current_sum < target:
            left += 1  # Увеличиваем сумму, сдвигая `left`
        else:
            right -= 1  # Уменьшаем сумму, сдвигая `right`

    return []  # Если решения нет


# Тесты
print(two_sum([2, 7, 11, 15], 9))  # [1, 2]
print(two_sum([1, 2, 3, 4, 4, 9, 11, 15], 8))  # [4, 5]
print(two_sum([1, 2, 3, 4, 5], 10))  # [] (Нет решения)
print(two_sum([1, 5, 10, 12, 14], 22))  # [3, 5]
