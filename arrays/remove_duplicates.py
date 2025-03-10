# Задача: Удаление дубликатов из отсортированного массива.
# Дано: отсортированный список `nums`.
# Нужно: удалить дубликаты на месте так, чтобы каждый элемент встречался только один раз,
# и вернуть количество уникальных элементов `k`. Остальная часть `nums` может быть изменена.

def remove_duplicates(nums: list[int]) -> int:
    """
    Функция удаляет дубликаты из отсортированного списка.

    :param nums: list[int] - отсортированный список чисел.
    :return: int - количество уникальных элементов (k).
    """

    if not nums:
        return 0  # Если массив пуст, возвращаем 0

    k: int = 1  # Первый уникальный элемент уже на месте

    # Проходим по массиву, начиная со второго элемента
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:  # Если нашли новый уникальный элемент
            nums[k] = nums[i]  # Перемещаем его вперед
            k += 1  # Увеличиваем счетчик уникальных элементов

    return k  # Возвращаем количество уникальных элементов


# 🔹 Тестируем
nums = [1, 1, 2, 3, 3]
l = remove_duplicates(nums)
print(l, nums[:l])  # Ожидаемый результат: 3, [1, 2, 3]

"""
Анализ сложности:
- Временная сложность: O(n), так как мы проходим массив один раз.
- Пространственная сложность: O(1), так как изменения выполняются на месте без доп. памяти.
"""
