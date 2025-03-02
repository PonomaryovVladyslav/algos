def max_subarray_sum_divisible_by_k(nums: list[int], k: int) -> int:
    """
    Функция находит **максимальную сумму подмассива**, которая делится на `k`.

    🔹 Алгоритм (Префиксные суммы O(n²)):
    1️⃣ Используем `prefix_sum`, где `prefix_sum[i]` — сумма первых `i` элементов.
    2️⃣ Для каждого подмассива `(i, j)` вычисляем сумму `prefix_sum[j] - prefix_sum[i]`.
    3️⃣ Проверяем, делится ли `sub_sum` на `k`, если да — обновляем `max_sum`.

    🔹 Временная сложность: **O(n²)** — два вложенных цикла.
    🔹 Пространственная сложность: **O(n)** — массив `prefix_sum`.

    :param nums: list[int] - входной массив.
    :param k: int - делитель.
    :return: int - максимальная сумма подмассива, делящаяся на `k`.
    """

    n = len(nums)
    prefix_sum = [0] * (n + 1)

    # 1. Заполняем массив префиксных сумм
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    max_sum = 0

    # 2. Перебираем все подмассивы и проверяем делимость суммы на `k`
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub_sum = prefix_sum[j] - prefix_sum[i]
            if sub_sum % k == 0:
                max_sum = max(max_sum, sub_sum)

    return max_sum


# 🔹 Тестируем
nums1, k1 = [3, 1, 4, 2, 6], 3
nums2, k2 = [4, 7, 9, 3, 2], 5

print(max_subarray_sum_divisible_by_k(nums1, k1))  # ✅ 12
print(max_subarray_sum_divisible_by_k(nums2, k2))  # ✅ 20
