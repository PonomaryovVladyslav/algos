def max_subarray_sum_circular(nums: list[int]) -> int:
    """
    Находит максимальную сумму подмассива в циклическом массиве.

    🔹 **Алгоритм**:
       - **Обычный Кадане (`kadane`)**: Находит максимальную подстроку.
       - **Кадане для минимума (`kadane(-nums)`)**: Находит минимальную подстроку.
       - **Два варианта ответа**:
         1. `max_subarray`: Обычная максимальная сумма.
         2. `total_sum - min_subarray`: Выбираем наибольший невыбранный кусок (цикличность).
       - Если `max_subarray < 0`, значит все числа отрицательные, тогда `max_subarray` — лучший ответ.

    🔹 **Временная сложность**:
       - `O(n)`, так как три линейных прохода.

    🔹 **Пространственная сложность**:
       - `O(1)`, так как нет доп. структуры данных.

    :param nums: list[int] - Входной массив.
    :return: int - Максимальная сумма подмассива (учитывая цикличность).
    """
    def kadane(arr):
        max_sum = cur_sum = arr[0]
        for num in arr[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
        return max_sum

    total_sum = sum(nums)
    max_subarray = kadane(nums)  # Обычная Кадане
    min_subarray = kadane([-num for num in nums])  # Находим минимальную сумму

    if max_subarray < 0:  # Если все элементы отрицательные, вернуть обычный Кадане
        return max_subarray

    return max(max_subarray, total_sum + min_subarray)  # total_sum - (-min_subarray)


# 🔹 Тесты
print(max_subarray_sum_circular([1, -2, 3, -2]))  # ✅ 3
print(max_subarray_sum_circular([5, -3, 5]))  # ✅ 10
print(max_subarray_sum_circular([-3, -2, -3]))  # ✅ -2
print(max_subarray_sum_circular([3, -1, 2, -1]))  # ✅ 4
print(max_subarray_sum_circular([10, -3, -2, 5, -3, 10]))  # ✅ 22
