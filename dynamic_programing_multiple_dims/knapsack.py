def knapsack(items: dict[str, tuple[int, int]], max_weight: int) -> tuple[int, list[str]]:
    """
    Функция решает задачу **0/1 рюкзака**: максимизировать стоимость предметов,
    помещённых в рюкзак, не превышая максимальный вес.

    🔹 Алгоритм (Динамическое программирование O(n * W)):
    1️⃣ Создаём `dp[i][j]`, где `dp[i][j]` — максимальная стоимость при `i` предметах и весе `j`.
    2️⃣ Базовый случай: `dp[0][j] = 0` (без предметов стоимость `0`).
    3️⃣ Для каждого предмета:
        - Если `j < item_weight`, переносим `dp[i-1][j]`.
        - Иначе берём максимум из:
          - `dp[i-1][j]` (не берём предмет).
          - `dp[i-1][j-item_weight] + item_value` (берём предмет).
    4️⃣ Восстанавливаем список взятых предметов.

    🔹 Временная сложность: **O(n * W)**, где `n` — число предметов, `W` — максимальный вес.
    🔹 Пространственная сложность: **O(n * W)** — `dp` таблица.

    :param items: dict[str, tuple[int, int]] - словарь {название: (вес, стоимость)}.
    :param max_weight: int - максимальный вес рюкзака.
    :return: tuple[int, list[str]] - максимальная стоимость и список предметов.
    """

    item_list = list(items.keys())  # Получаем список предметов
    n = len(item_list)

    # Создаём DP таблицу размером (n+1) x (max_weight+1)
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    # Заполняем DP таблицу
    for i in range(1, n + 1):
        item_name = item_list[i - 1]
        item_weight, item_value = items[item_name]

        for j in range(1, max_weight + 1):
            if j < item_weight:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_weight] + item_value)

    # Восстанавливаем список предметов
    total_value = dp[n][max_weight]
    items_taken = []
    i, j = n, max_weight

    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:  # Если предмет был взят
            items_taken.append(item_list[i - 1])
            j -= items[item_list[i - 1]][0]  # Вычитаем вес предмета
        i -= 1

    return total_value, items_taken


# 🔹 Тестируем
items = {
    "apple": (2, 100),
    "ring": (1, 10),
    "sword": (3, 40),
    "shield": (5, 30),
    "potion": (3, 20),
}

max_weight = 9
value, selected_items = knapsack(items, max_weight)

print(f"Items taken: {selected_items}\nTotal value: {value}")
