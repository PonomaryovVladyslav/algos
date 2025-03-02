def max_profit(prices: list[int]) -> int:
    """
    Функция вычисляет **максимальную прибыль** от **не более чем двух сделок** (покупка-продажа).

    🔹 Алгоритм (Динамическое программирование O(n)):
    1️⃣ **Переменные:**
       - `first_buy`  → минимальная цена первой покупки.
       - `first_sell` → максимальная прибыль от первой сделки.
       - `second_buy` → минимальная цена после первой продажи.
       - `second_sell` → максимальная прибыль от двух сделок.
    2️⃣ **Проходим по `prices`** и обновляем переменные:
       - `first_buy = max(first_buy, -price)`
       - `first_sell = max(first_sell, first_buy + price)`
       - `second_buy = max(second_buy, first_sell - price)`
       - `second_sell = max(second_sell, second_buy + price)`
    3️⃣ Итоговый ответ: `second_sell`.

    🔹 Временная сложность: **O(n)** — один проход по массиву.
    🔹 Пространственная сложность: **O(1)** — используем только 4 переменные.

    :param prices: list[int] - массив цен.
    :return: int - максимальная прибыль от двух сделок.
    """

    if not prices:
        return 0

    first_buy, first_sell = float('-inf'), 0
    second_buy, second_sell = float('-inf'), 0

    for price in prices:
        first_buy = max(first_buy, -price)  # Покупаем дешевле
        first_sell = max(first_sell, first_buy + price)  # Продаем дороже
        second_buy = max(second_buy, first_sell - price)  # Вторая покупка
        second_sell = max(second_sell, second_buy + price)  # Вторая продажа

    return second_sell


# 🔹 Тестируем
print(max_profit([3, 3, 5, 0, 0, 3, 1, 4]))  # ✅ 6
print(max_profit([1, 2, 3, 4, 5]))  # ✅ 4
print(max_profit([7, 6, 4, 3, 1]))  # ✅ 0
print(max_profit([1, 4, 2, 7, 3, 6, 9, 0, 5]))  # ✅ 13
