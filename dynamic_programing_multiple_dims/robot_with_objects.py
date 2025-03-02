def unique_paths_with_obstacles(grid: list[list[int]]) -> int:
    """
    Функция вычисляет **количество уникальных путей** от `grid[0][0]` до `grid[m-1][n-1]`,
    двигаясь только **вниз** или **вправо**, с учётом препятствий (`1`).

    🔹 Алгоритм (Динамическое программирование O(m * n)):
    1️⃣ Если `grid[0][0] == 1` или `grid[m-1][n-1] == 1`, пути нет → `return 0`
    2️⃣ Используем `dp[i][j]`, где `dp[i][j]` — количество путей до `grid[i][j]`.
    3️⃣ `dp[0][0] = 1` (начальная точка).
    4️⃣ Заполняем первую строку и первый столбец (если нет препятствий).
    5️⃣ Для всех `grid[i][j] == 0`:
       `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
    6️⃣ Итоговый ответ: `dp[m-1][n-1]`.

    🔹 Временная сложность: **O(m * n)** — двойной цикл.
    🔹 Пространственная сложность: **O(m * n)** — `dp` таблица.

    :param grid: list[list[int]] - `m x n` матрица (0 — свободно, 1 — препятствие).
    :return: int - количество уникальных путей.
    """

    m, n = len(grid), len(grid[0])

    # Если начальная или конечная точка заблокирована — нет пути
    if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
        return 0

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1  # Начальная точка

    # Заполняем первый столбец
    for i in range(1, m):
        if grid[i][0] == 0:
            dp[i][0] = dp[i - 1][0]

    # Заполняем первую строку
    for j in range(1, n):
        if grid[0][j] == 0:
            dp[0][j] = dp[0][j - 1]

    # Заполняем оставшуюся матрицу
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 0:  # Если нет препятствия
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]  # Количество путей до финиша


def unique_paths_with_obstacles_optimized(grid: list[list[int]]) -> int:
    """
    Оптимизированная версия: используем **один массив `dp` (O(n) памяти)**.

    🔹 Оптимизация:
    - Вместо `dp[m][n]`, используем `dp[n]`, обновляя значения **справа налево**.
    - `dp[j]` хранит количество путей до `grid[i][j]`.

    🔹 Временная сложность: **O(m * n)** (двойной цикл).
    🔹 Пространственная сложность: **O(n)** (один массив `dp`).

    :param grid: list[list[int]] - `m x n` матрица (0 — свободно, 1 — препятствие).
    :return: int - количество уникальных путей.
    """

    m, n = len(grid), len(grid[0])

    if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
        return 0

    dp = [0] * n
    dp[0] = 1  # Начальная точка

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[j] = 0  # Если препятствие, обнуляем путь
            elif j > 0:
                dp[j] += dp[j - 1]  # dp[j] = dp[j] (сверху) + dp[j-1] (слева)

    return dp[-1]  # Количество путей до (m-1, n-1)


# 🔹 Тестируем
print(unique_paths_with_obstacles([
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
]))  # ✅ 2

print(unique_paths_with_obstacles([
  [0, 1],
  [0, 0]
]))  # ✅ 1

print(unique_paths_with_obstacles([
  [1, 0]
]))  # ✅ 0

print(unique_paths_with_obstacles_optimized([
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
]))  # ✅ 2

print(unique_paths_with_obstacles_optimized([
  [0, 1],
  [0, 0]
]))  # ✅ 1

print(unique_paths_with_obstacles_optimized([
  [1, 0]
]))  # ✅ 0
