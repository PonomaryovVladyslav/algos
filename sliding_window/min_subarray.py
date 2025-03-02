def min_subarray_len(target: int, nums: list[int]) -> int:
    """
    Находит минимальную длину подмассива, сумма которого ≥ target.

    🔹 **Метод**: Sliding Window (две границы `left`, `right`)
    🔹 **Идея**:
       - Двигаем `right`, пока сумма < target.
       - Когда сумма ≥ target, уменьшаем `left`, сокращая окно.
       - Запоминаем минимальную длину окна.

    🔹 **Сложность**:
       - `O(n)`, один проход (каждый элемент заходит и выходит 1 раз).
       - `O(1)`, константная память.

    ✅ **Пример**:
       ```
       Вход: target=7, nums=[2,3,1,2,4,3]
       Выход: 2 (подмассив [4,3])
       ```
    """
    left = 0
    window_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        window_sum += nums[right]  # Расширяем окно вправо

        while window_sum >= target:  # Когда сумма достигла target
            min_length = min(min_length, right - left + 1)
            window_sum -= nums[left]  # Уменьшаем окно слева
            left += 1

    return min_length if min_length != float('inf') else 0


# 🔹 Тестовые примеры
print(min_subarray_len(7, [2,3,1,2,4,3]))  # ✅ 2 ([4,3])
print(min_subarray_len(4, [1,4,4]))  # ✅ 1 ([4])
print(min_subarray_len(11, [1,1,1,1,1,1,1,1]))  # ✅ 0 (нет подмассива)
print(min_subarray_len(15, [5,1,3,5,10,7,4,9,2,8]))  # ✅ 2 ([10,7])
