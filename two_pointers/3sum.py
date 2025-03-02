def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Найти все уникальные тройки чисел в массиве, сумма которых равна 0.

    Задача:
    - Дана последовательность целых чисел `nums`.
    - Найти все уникальные тройки (a, b, c), такие что a + b + c = 0.

    Вход:
    nums = [-1, 0, 1, 2, -1, -4]

    Выход:
    [[-1, -1, 2], [-1, 0, 1]]

    Решение:
    - Сортируем массив (O(n log n)).
    - Фиксируем первое число `nums[i]`, а два других ищем методом двух указателей (O(n^2)).
    - Пропускаем дубликаты, чтобы не добавлять одинаковые тройки.

    Время: O(n^2) — внешний цикл O(n) + два указателя O(n).
    Пространство: O(1) — если не считать результат, O(n) — если считать.
    """

    nums.sort()  # O(n log n) сортируем массив
    result = []

    for i in range(len(nums) - 2):
        # Пропускаем дубликаты (чтобы избежать одинаковых троек)
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1  # Два указателя

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Пропускаем одинаковые `left` и `right`
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1  # Нам нужно большее число
            else:
                right -= 1  # Нам нужно меньшее число

    return result


# Тесты
print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
print(three_sum([0, 0, 0, 0]))  # [[0, 0, 0]]
print(three_sum([-2, 0, 1, 1, 2]))  # [[-2, 0, 2], [-2, 1, 1]]
print(three_sum([]))  # []
print(three_sum([1, 2, -2, -1]))  # []
