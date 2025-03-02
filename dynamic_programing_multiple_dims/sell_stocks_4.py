def max_profit(k: int, prices: list[int]) -> int:
    """
    Функция вычисляет **максимальную прибыль** от **не более чем k сделок** (покупка-продажа).

    🔹 Алгоритм (Динамическое программирование O(k * n)):
    1️⃣ Если `k == 0` или `prices` пуст, возвращаем `0`.
    2️⃣ Если `k >= n/2`, это эквивалентно **бесконечным сделкам** → `O(n) решение`.
    3️⃣ Используем `dp[t][d]`, где:
       - `t` — номер транзакции (1 ≤ t ≤ k),
       - `d` — день (0 ≤ d < n),
       - `dp[t][d]` — максимальная прибыль после `t` сделок к `d`-му дню.
    4️⃣ Обновляем `dp[t][d]`:
       - `max_prev_buy = max(max_prev_buy, dp[t-1][d-1] - prices[d-1])`
       - `dp[t][d] = max(dp[t][d-1], prices[d] + max_prev_buy)`.
    5️⃣ Итоговый ответ: `dp[k][n-1]`.

    🔹 Временная сложность: **O(k * n)** — двойной цикл.
    🔹 Пространственная сложность: **O(k * n)** — `dp` таблица.

    :param k: int - максимальное количество сделок.
    :param prices: list[int] - массив цен.
    :return: int - максимальная прибыль от `k` сделок.
    """

    if not prices or k == 0:
        return 0

    n = len(prices)

    # Если k >= n/2, это равносильно неограниченным сделкам
    if k >= n // 2:
        return sum(max(prices[i+1] - prices[i], 0) for i in range(n - 1))

    dp = [[0] * n for _ in range(k + 1)]

    for t in range(1, k + 1):
        max_prev_buy = float('-inf')
        for d in range(1, n):
            max_prev_buy = max(max_prev_buy, dp[t-1][d-1] - prices[d-1])
            dp[t][d] = max(dp[t][d-1], prices[d] + max_prev_buy)

    return dp[k][n-1]


def max_profit_optimized(k: int, prices: list[int]) -> int:
    """
    Оптимизированная версия: **O(n) памяти**.

    🔹 Оптимизация:
    - Вместо `dp[k][n]`, используем `dp_prev[n]` и `dp_curr[n]`, обновляя их **справа налево**.

    🔹 Временная сложность: **O(k * n)** (двойной цикл).
    🔹 Пространственная сложность: **O(n)** (две строки `dp`).

    :param k: int - максимальное количество сделок.
    :param prices: list[int] - массив цен.
    :return: int - максимальная прибыль от `k` сделок.
    """

    if not prices or k == 0:
        return 0

    n = len(prices)

    if k >= n // 2:
        return sum(max(prices[i+1] - prices[i], 0) for i in range(n - 1))

    dp_prev = [0] * n
    dp_curr = [0] * n

    for t in range(1, k + 1):
        max_prev_buy = float('-inf')
        for d in range(1, n):
            max_prev_buy = max(max_prev_buy, dp_prev[d-1] - prices[d-1])
            dp_curr[d] = max(dp_curr[d-1], prices[d] + max_prev_buy)
        dp_prev, dp_curr = dp_curr, dp_prev  # Обновляем строки

    return dp_prev[n-1]


# 🔹 Тестируем
print(max_profit(2, [3, 2, 6, 5, 0, 3]))  # ✅ 7
print(max_profit(2, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))  # ✅ 13
print(max_profit(3, [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]))  # ✅ 16
print(max_profit(2, [3, 3, 5, 0, 0, 3, 1, 4]))  # ✅ 6

print(max_profit_optimized(2, [3, 2, 6, 5, 0, 3]))  # ✅ 7
print(max_profit_optimized(2, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))  # ✅ 13
print(max_profit_optimized(3, [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]))  # ✅ 16
print(max_profit_optimized(2, [3, 3, 5, 0, 0, 3, 1, 4]))  # ✅ 6
