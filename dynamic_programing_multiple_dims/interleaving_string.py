def is_interleave(s1: str, s2: str, s3: str) -> bool:
    """
    Функция проверяет, можно ли получить `s3`, чередуя символы `s1` и `s2`, сохраняя их порядок.

    🔹 Алгоритм (Динамическое программирование O(m * n)):
    1️⃣ Если `len(s1) + len(s2) != len(s3)`, возвращаем `False` (невозможно получить `s3`).
    2️⃣ Используем `dp[i][j]`, где `dp[i][j] = True`, если `s3[:i+j]` можно получить из `s1[:i]` и `s2[:j]`.
    3️⃣ Базовый случай: `dp[0][0] = True`, так как пустые строки дают пустую строку.
    4️⃣ Заполняем `dp` по следующим правилам:
        - `dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]` (если `s3` формируется только `s1`).
        - `dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]` (если `s3` формируется только `s2`).
        - `dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])`
    5️⃣ Итоговый ответ: `dp[m][n]`.

    🔹 Временная сложность: **O(m * n)** — двумерная `dp` таблица.
    🔹 Пространственная сложность: **O(m * n)** — используем `dp[m+1][n+1]`.

    :param s1: str - первая строка.
    :param s2: str - вторая строка.
    :param s3: str - результирующая строка.
    :return: bool - можно ли получить `s3` из `s1` и `s2`, сохраняя их порядок.
    """

    m, n = len(s1), len(s2)

    # Если длины не совпадают, сразу False
    if m + n != len(s3):
        return False

    # Создаём DP таблицу размером (m+1) x (n+1)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True  # Пустая строка образует пустую строку

    # Заполняем первую строку (только s1)
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

    # Заполняем первый столбец (только s2)
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

    # Заполняем оставшуюся таблицу
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                       (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

    return dp[m][n]


# 🔹 Тестируем
print(is_interleave("abc", "def", "adbcef"))  # ✅ True
print(is_interleave("abc", "def", "abdecf"))  # ❌ False
print(is_interleave("aab", "axy", "aaxaby"))  # ✅ True
print(is_interleave("abc", "xyz", "axycbz"))  # ❌ False
