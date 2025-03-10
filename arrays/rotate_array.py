# Задача: Повернуть массив вправо на `k` шагов.
# Дано: массив `nums` и число `k`.
# Нужно: изменить массив на месте так, чтобы элементы сдвинулись вправо на `k` позиций.

def rotate_array(nums: list[int], k: int) -> None:
    """
    Функция выполняет циклический сдвиг массива вправо на `k` шагов.

    :param nums: list[int] - список чисел.
    :param k: int - количество шагов сдвига.
    :return: None - изменение выполняется на месте.
    """

    n: int = len(nums)
    k %= n  # Если k > n, уменьшаем его (например, сдвиг на 10 в массиве длины 7 эквивалентен сдвигу на 3)

    def reverse(start: int, end: int) -> None:
        """Разворачивает часть массива между индексами start и end."""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # 1. Разворачиваем весь массив
    reverse(0, n - 1)
    # 2. Разворачиваем первые k элементов
    reverse(0, k - 1)
    # 3. Разворачиваем оставшуюся часть
    reverse(k, n - 1)


# 🔹 Тестируем
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate_array(nums, k)
print(nums)  # Ожидаемый результат: [5, 6, 7, 1, 2, 3, 4]

"""
Анализ сложности:
- Временная сложность: O(n), так как мы выполняем три разворота массива.
- Пространственная сложность: O(1), так как изменения выполняются на месте без доп. памяти.
"""
