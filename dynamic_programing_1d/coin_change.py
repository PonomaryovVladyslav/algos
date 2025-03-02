def coin_change(coins: list[int], amount: int) -> int:
    """
    Функция для нахождения минимального количества монет для суммы `amount`.

    🔹 Алгоритм:
    1️⃣ Создаём массив `dp`, где `dp[i]` — минимальное количество монет для суммы `i`.
    2️⃣ Инициализируем `dp` бесконечностями (`float('inf')`), так как изначально сумма считается недостижимой.
    3️⃣ `dp[0] = 0`, так как для суммы `0` монеты не нужны.
    4️⃣ Для каждой монеты `coin` из списка `coins`:
        - Проходим по `dp[i]`, начиная с `i = coin`, и обновляем `dp[i]`:
          `dp[i] = min(dp[i], dp[i - coin] + 1)`
        - Это означает, что мы либо оставляем старое значение `dp[i]`, либо используем текущую монету.
    5️⃣ Если `dp[amount] == float('inf')`, то сумму нельзя набрать, возвращаем `-1`.

    🔹 Временная сложность: **O(n * m)**, где `n = amount`, `m = len(coins)`.
    🔹 Пространственная сложность: **O(n)**, так как используется массив `dp` размером `amount + 1`.

    :param coins: list[int] - список доступных номиналов монет.
    :param amount: int - целевая сумма.
    :return: int - минимальное количество монет для составления `amount`, либо -1, если невозможно.
    """

    # 1. Инициализируем массив dp (бесконечностями)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 можно собрать без монет

    # 2. Перебираем монеты
    for coin in coins:
        for i in range(coin, amount + 1):  # Обновляем значения dp[i]
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # 3. Если `amount` нельзя набрать — возвращаем -1
    return dp[amount] if dp[amount] != float('inf') else -1


# 🔹 Тестируем
print(coin_change([1, 2, 5], 11))  # 3 (5 + 5 + 1)
print(coin_change([2], 3))  # -1 (невозможно)
print(coin_change([1], 0))  # 0 (ноль монет)
print(coin_change([1, 2, 5], 100))  # 20 (100 = 5*20)
