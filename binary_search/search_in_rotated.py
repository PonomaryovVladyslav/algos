# Задача: Найти индекс `target` в отсортированном, но повернутом массиве.
# Дано: массив `nums`, отсортированный по возрастанию, но с возможным сдвигом (без дубликатов).
# Нужно: вернуть индекс `target`, если найден, иначе `-1`.

def search(nums: list[int], target: int) -> int:
    """
    Функция выполняет бинарный поиск в повернутом массиве.

    :param nums: list[int] - отсортированный, но повернутый массив.
    :param target: int - искомый элемент.
    :return: int - индекс `target` или `-1`, если не найден.
    """

    left, right = 0, len(nums) - 1  # Границы бинарного поиска

    while left <= right:
        mid = (left + right) // 2  # Средний индекс

        if nums[mid] == target:
            return mid  # Найден target

        # Определяем, какая половина отсортирована
        if nums[left] <= nums[mid]:  # Левая часть отсортирована
            if nums[left] <= target < nums[mid]:  # `target` в левой части
                right = mid - 1
            else:
                left = mid + 1
        else:  # Правая часть отсортирована
            if nums[mid] < target <= nums[right]:  # `target` в правой части
                left = mid + 1
            else:
                right = mid - 1

    return -1  # Если не найден


# 🔹 Тестируем
print(search([4, 5, 6, 7, 0, 1, 2], 0))  # Ожидаемый результат: 4
print(search([4, 5, 6, 7, 0, 1, 2], 3))  # Ожидаемый результат: -1
print(search([1], 0))  # Ожидаемый результат: -1
print(search([5, 6, 7, 0, 1, 2, 3, 4], 6))  # Ожидаемый результат: 1

"""
Анализ сложности:
- Временная сложность: O(log n), так как используется бинарный поиск.
- Пространственная сложность: O(1), так как не используется дополнительная память.
"""
