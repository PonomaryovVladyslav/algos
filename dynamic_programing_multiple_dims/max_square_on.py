def maximal_square_optimized(matrix: list[list[int]]) -> int:
    """
    Функция находит **размер наибольшего квадратного подмассива** с `1` в матрице `matrix`
    с использованием оптимизированного динамического программирования.

    🔹 Алгоритм (Оптимизированное DP O(m * n) с O(n) памяти):
    1️⃣ Используем **одну строку `prev`** вместо `dp[m][n]`, чтобы уменьшить память с O(m * n) до O(n).
    2️⃣ `prev[j]` хранит значения предыдущей строки, `curr[j]` — текущей.
    3️⃣ Если `matrix[i][j] == 1`, обновляем `curr[j]`:
        - `curr[j] = min(prev[j], curr[j-1], prev[j-1]) + 1`
    4️⃣ `max_side` отслеживает наибольшую сторону квадрата.
    5️⃣ Итоговый ответ: `max_side ** 2`.

    🔹 Временная сложность: **O(m * n)** — двойной цикл.
    🔹 Пространственная сложность: **O(n)** — используем `prev` и `curr`.

    :param matrix: list[list[int]] - бинарная матрица `m x n` (0 и 1).
    :return: int - площадь наибольшего квадратного подмассива.
    """

    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    prev = [0] * (n + 1)  # Храним только одну строку
    max_side = 0

    # Заполняем DP строку
    for i in range(m):
        curr = [0] * (n + 1)  # Текущая строка
        for j in range(1, n + 1):
            if matrix[i][j - 1] == 1:
                curr[j] = min(prev[j], curr[j - 1], prev[j - 1]) + 1
                max_side = max(max_side, curr[j])
        prev = curr  # Обновляем строку

    return max_side ** 2


# 🔹 Тестируем
matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1]
]

print(maximal_square_optimized(matrix))  # ✅ 4

matrix2 = [
    [0, 1],
    [1, 0]
]

print(maximal_square_optimized(matrix2))  # ✅ 1

matrix3 = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

print(maximal_square_optimized(matrix3))  # ✅ 9
