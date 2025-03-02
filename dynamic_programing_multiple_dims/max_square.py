def maximal_square_dp(matrix: list[list[int]]) -> int:
    """
    Функция находит **размер наибольшего квадратного подмассива** с `1` в матрице `matrix`.

    🔹 Алгоритм (Динамическое программирование O(m * n)):
    1️⃣ Используем `dp[i][j]`, где `dp[i][j]` — сторона наибольшего квадрата,
       заканчивающегося в `matrix[i][j]`.
    2️⃣ Если `matrix[i][j] == 1`, то:
        - `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`
    3️⃣ `max_side` отслеживает наибольшую сторону квадрата.
    4️⃣ Итоговый ответ: `max_side ** 2`.

    🔹 Временная сложность: **O(m * n)** — двойной цикл.
    🔹 Пространственная сложность: **O(m * n)** — `dp` таблица.

    :param matrix: list[list[int]] - бинарная матрица `m x n` (0 и 1).
    :return: int - площадь наибольшего квадратного подмассива.
    """

    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_side = 0

    # Заполняем DP таблицу
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1  # Граница всегда 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                max_side = max(max_side, dp[i][j])

    return max_side ** 2


# 🔹 Тестируем
matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1]
]

print(maximal_square_dp(matrix))  # ✅ 4

matrix2 = [
    [0, 1],
    [1, 0]
]

print(maximal_square_dp(matrix2))  # ✅ 1

matrix3 = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

print(maximal_square_dp(matrix3))  # ✅ 9
