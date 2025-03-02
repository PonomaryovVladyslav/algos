# Задача: Найти первый и последний индексы `target` в отсортированном массиве `nums`.
# Дано: массив `nums`, отсортированный по возрастанию, и число `target`.
# Нужно: вернуть `[first, last]` — первый и последний индекс `target`, или `[-1, -1]`, если `target` отсутствует.

def search_range(nums: list[int], target: int) -> list[int]:
    """
    Функция находит первый и последний индекс `target` в `nums`.

    :param nums: list[int] - отсортированный список чисел.
    :param target: int - искомое число.
    :return: list[int] - `[first, last]` или `[-1, -1]`, если `target` отсутствует.
    """

    def find_first(nums: list[int], target: int) -> int:
        """Находит первый индекс `target` в `nums` с помощью бинарного поиска."""
        left, right = 0, len(nums) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:  # Ищем первое вхождение
                right = mid - 1
            else:
                left = mid + 1
            if nums[mid] == target:
                first = mid  # Запоминаем первый индекс
        return first

    def find_last(nums: list[int], target: int) -> int:
        """Находит последний индекс `target` в `nums` с помощью бинарного поиска."""
        left, right = 0, len(nums) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:  # Ищем последнее вхождение
                left = mid + 1
            else:
                right = mid - 1
            if nums[mid] == target:
                last = mid  # Запоминаем последний индекс
        return last

    first = find_first(nums, target)
    if first == -1:
        return [-1, -1]  # Если `target` не найден

    last = find_last(nums, target)
    return [first, last]


# 🔹 Тестируем
print(search_range([5, 7, 7, 8, 8, 10], 8))  # Ожидаемый результат: [3, 4]
print(search_range([5, 7, 7, 8, 8, 10], 6))  # Ожидаемый результат: [-1, -1]
print(search_range([], 0))  # Ожидаемый результат: [-1, -1]
print(search_range([1, 2, 3, 4, 5, 5, 5, 6, 7], 5))  # Ожидаемый результат: [4, 6]

"""
Анализ сложности:
- Временная сложность: O(log n), так как используется два бинарных поиска.
- Пространственная сложность: O(1), так как не используется дополнительная память.
"""
