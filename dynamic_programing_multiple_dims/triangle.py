def minimum_total(triangle: list[list[int]]) -> int:
    """
    Функция вычисляет **минимальную сумму пути** из **вершины** в **основание** треугольника.

    🔹 Алгоритм (Динамическое программирование O(n²)):
    1️⃣ Начинаем с **последней строки** (инициализация `dp`).
    2️⃣ Двигаемся **снизу вверх**, выбирая **минимальный путь** на каждом уровне:
       - `dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])`
    3️⃣ Итоговый ответ: `dp[0]` (минимальная сумма пути до вершины).

    🔹 Временная сложность: **O(n²)** — два вложенных цикла.
    🔹 Пространственная сложность: **O(n)** — используем `dp` размером `n` (одна строка).

    :param triangle: list[list[int]] - треугольная матрица с весами.
    :return: int - минимальная сумма пути.
    """

    if not triangle:
        return 0

    dp = triangle[-1][:]  # Начинаем с последней строки

    for i in range(len(triangle) - 2, -1, -1):  # Проходим снизу вверх
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])  # Обновляем dp

    return dp[0]  # Минимальная сумма пути до вершины


# 🔹 Тестируем
print(minimum_total([
     [2],
    [3, 4],
   [6, 5, 7],
  [4, 1, 8, 3]
]))  # ✅ 11

print(minimum_total([
    [-10]
]))  # ✅ -10
