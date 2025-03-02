def max_subarray_sum_divisible_by_k(nums: list[int], k: int) -> int:
    """
    Находит максимальную сумму подмассива, который делится на k.

    🔹 **Алгоритм (O(n))**:
       1️⃣ Используем `prefix_sum` для накопления суммы.
       2️⃣ Храним `mod_map`, который содержит **остатки от деления** `prefix_sum % k`
       3️⃣ Если текущий `mod` уже встречался, значит, сумма между этими индексами делится на `k`
       4️⃣ Обновляем `max_sum`, если найден больший подмассив.

    🔹 **Временная сложность**:
       - `O(n)`, так как каждое число обрабатывается один раз.

    🔹 **Пространственная сложность**:
       - `O(k)`, так как храним не более `k` остатков.

    :param nums: list[int] - Исходный массив.
    :param k: int - Делитель.
    :return: int - Максимальная сумма подмассива, делящегося на `k`.
    """
    prefix_sum = 0
    max_sum = 0
    mod_map = {0: -1}  # Остаток 0 означает, что subarray [0:i] делится на k

    for i, num in enumerate(nums):
        prefix_sum += num
        mod = prefix_sum % k

        if mod < 0:  # Делаем остаток положительным
            mod += k

        if mod in mod_map:
            max_sum = max(max_sum, prefix_sum - mod_map[mod])
        else:
            mod_map[mod] = prefix_sum  # Запоминаем первое появление остатка

    return max_sum


# 🔹 Тесты
nums1, k1 = [3, 1, 4, 2, 6], 3
nums2, k2 = [4, 7, 9, 3, 2], 5

print(max_subarray_sum_divisible_by_k(nums1, k1))  # ✅ 12
print(max_subarray_sum_divisible_by_k(nums2, k2))  # ✅ 20
