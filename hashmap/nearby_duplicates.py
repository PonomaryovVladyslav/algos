def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    """
    Проверяет, содержит ли массив два одинаковых элемента,
    расположенных на расстоянии не более k.

    🔹 **Алгоритм (O(n))**:
       1️⃣ Создаем `index_map` для хранения **последнего индекса** каждого числа.
       2️⃣ Проходим по `nums`, проверяя, встречалось ли число ранее.
       3️⃣ Если `abs(i - j) <= k`, возвращаем `True`.
       4️⃣ В противном случае обновляем индекс в `index_map`.

    🔹 **Временная сложность**:
       - `O(n)`, так как мы проходим массив **один раз**.

    🔹 **Пространственная сложность**:
       - `O(n)`, так как в худшем случае `index_map` содержит **все числа массива**.

    :param nums: list[int] - Исходный массив чисел.
    :param k: int - Максимальное расстояние между одинаковыми числами.
    :return: bool - `True`, если найдено такое повторение, иначе `False`.
    """
    index_map = {}

    for i, num in enumerate(nums):
        if num in index_map and abs(i - index_map[num]) <= k:
            return True  # Найдено совпадение с |i - j| ≤ k

        index_map[num] = i  # Обновляем индекс последнего появления num

    return False


# 🔹 Тесты
print(contains_nearby_duplicate([1,2,3,1], 3))  # ✅ True
print(contains_nearby_duplicate([1,0,1,1], 1))  # ✅ True
print(contains_nearby_duplicate([1,2,3,1,2,3], 2))  # ✅ False
print(contains_nearby_duplicate([99, 99], 2))  # ✅ True
print(contains_nearby_duplicate([], 1))  # ✅ False
