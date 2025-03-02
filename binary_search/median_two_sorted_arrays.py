# Задача: Найти медиану двух отсортированных массивов.
# Дано: два отсортированных массива `nums1` и `nums2`.
# Нужно: вернуть медиану объединенного массива (без его фактического объединения).

def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Функция находит медиану двух отсортированных массивов `nums1` и `nums2`.

    :param nums1: list[int] - первый отсортированный массив.
    :param nums2: list[int] - второй отсортированный массив.
    :return: float - медиана объединенного массива.
    """

    if len(nums1) > len(nums2):  # Гарантируем, что `nums1` короче `nums2`
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left_size = (m + n + 1) // 2  # Количество элементов в левой половине объединенного массива
    left, right = 0, m  # Бинарный поиск по `nums1`

    while left <= right:
        i = (left + right) // 2  # Разделяем `nums1`
        j = left_size - i  # Соответствующий раздел в `nums2`

        # Определяем граничные значения
        nums1_left = nums1[i - 1] if i > 0 else float('-inf')
        nums1_right = nums1[i] if i < m else float('inf')
        nums2_left = nums2[j - 1] if j > 0 else float('-inf')
        nums2_right = nums2[j] if j < n else float('inf')

        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            # Если общее количество элементов нечетное, медиана — максимум в левой половине
            if (m + n) % 2 == 1:
                return max(nums1_left, nums2_left)
            # Если четное — среднее двух центральных элементов
            return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2

        elif nums1_left > nums2_right:  # Двигаемся влево
            right = i - 1
        else:  # Двигаемся вправо
            left = i + 1

    raise ValueError("Некорректный ввод")  # Страховка (теоретически не должна срабатывать)


# 🔹 Тестируем
print(find_median_sorted_arrays([1, 3], [2]))  # Ожидаемый результат: 2.0
print(find_median_sorted_arrays([1, 2], [3, 4]))  # Ожидаемый результат: 2.5
print(find_median_sorted_arrays([0, 0], [0, 0]))  # Ожидаемый результат: 0.0
print(find_median_sorted_arrays([], [1]))  # Ожидаемый результат: 1.0
print(find_median_sorted_arrays([2], []))  # Ожидаемый результат: 2.0

"""
Анализ сложности:
- Временная сложность: O(log(min(m, n))), так как бинарный поиск выполняется по меньшему массиву.
- Пространственная сложность: O(1), так как не используется дополнительная память.
"""
