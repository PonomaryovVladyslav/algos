def longest_consecutive(nums: list[int]) -> int:
    """
    Находит длину самой длинной последовательной подпоследовательности.

    🔹 **Алгоритм (O(n))**:
       1️⃣ Используем `set`, чтобы проверять наличие чисел за O(1).
       2️⃣ Перебираем все числа, но начинаем последовательность только если `num - 1` отсутствует в `set`.
       3️⃣ Если `num` является началом последовательности, проверяем, есть ли `num + 1, num + 2, ...` в `set` и считаем её длину.
       4️⃣ Обновляем `max_length`, если найдена более длинная последовательность.

    🔹 **Временная сложность**:
       - `O(n)`, так как каждое число обрабатывается один раз.

    🔹 **Пространственная сложность**:
       - `O(n)`, так как храним `set` с `n` числами.

    :param nums: list[int] - Массив чисел.
    :return: int - Длина самой длинной последовательной подпоследовательности.
    """
    if not nums:
        return 0

    num_set = set(nums)  # O(n) добавляем все числа в set
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:  # Начало новой последовательности
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:  # Проверяем следующие числа
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length


# 🔹 Тесты
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # ✅ 4 (1, 2, 3, 4)
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))  # ✅ 9 (0, 1, 2, 3, 4, 5, 6, 7, 8)
print(longest_consecutive([]))  # ✅ 0
print(longest_consecutive([1,2,3,4,5,6,7,8,9,10]))  # ✅ 10
print(longest_consecutive([10,9,8,7,6,5,4,3,2,1]))  # ✅ 10
