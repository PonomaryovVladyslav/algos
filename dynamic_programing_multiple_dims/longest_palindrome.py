def longest_palindrome_dp(s: str) -> str:
    """
    Функция находит **наибольшую палиндромную подстроку** в `s` с помощью динамического программирования.

    🔹 Алгоритм (Динамическое программирование O(n²)):
    1️⃣ Используем `dp[i][j]`, где `dp[i][j] = True`, если `s[i:j+1]` — палиндром.
    2️⃣ Все одиночные символы (`s[i]`) — палиндромы (`dp[i][i] = True`).
    3️⃣ Двухсимвольные подстроки (`s[i] == s[j]`) проверяем отдельно.
    4️⃣ Для подстрок длины 3 и больше: `dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]`
    5️⃣ Обновляем `start, max_length`, если найдена большая палиндромная подстрока.

    🔹 Временная сложность: **O(n²)** — два вложенных цикла.
    🔹 Пространственная сложность: **O(n²)** — `dp` таблица.

    :param s: str - входная строка.
    :return: str - наибольшая палиндромная подстрока.
    """

    n = len(s)
    if n == 0:
        return ""

    dp = [[False] * n for _ in range(n)]
    start, max_length = 0, 1

    # Все одиночные символы — палиндромы
    for i in range(n):
        dp[i][i] = True

    # Проверяем подстроки длины 2 и больше
    for length in range(2, n + 1):  # Длина палиндрома
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or dp[i + 1][j - 1]:  # Проверяем внутреннюю часть
                    dp[i][j] = True
                    start, max_length = i, length

    return s[start:start + max_length]


def longest_palindrome_expand(s: str) -> str:
    """
    Функция находит **наибольшую палиндромную подстроку** методом **расширения от центра**.

    🔹 Алгоритм (Expand Around Center O(n²)):
    1️⃣ Перебираем каждый символ `i` как потенциальный центр палиндрома.
    2️⃣ Проверяем два случая:
        - Нечётный палиндром (`aba`): расширяем от `s[i]`.
        - Чётный палиндром (`abba`): расширяем от `s[i]` и `s[i+1]`.
    3️⃣ Обновляем `longest`, если нашли более длинный палиндром.

    🔹 Временная сложность: **O(n²)** — два вложенных цикла.
    🔹 Пространственная сложность: **O(1)** — не используем доп. память.

    :param s: str - входная строка.
    :return: str - наибольшая палиндромная подстрока.
    """

    if not s:
        return ""

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # Вернуть найденный палиндром

    longest = ""
    for i in range(len(s)):
        # Для нечетных палиндромов (один центр)
        odd_palindrome = expand_around_center(i, i)
        # Для четных палиндромов (два центра)
        even_palindrome = expand_around_center(i, i + 1)
        # Выбираем максимальный по длине
        longest = max(longest, odd_palindrome, even_palindrome, key=len)

    return longest


# 🔹 Тестируем
print(longest_palindrome_dp("babad"))  # ✅ "bab" или "aba"
print(longest_palindrome_dp("cbbd"))   # ✅ "bb"
print(longest_palindrome_dp("a"))      # ✅ "a"
print(longest_palindrome_dp("ac"))     # ✅ "a" или "c"

print(longest_palindrome_expand("babad"))  # ✅ "bab" или "aba"
print(longest_palindrome_expand("cbbd"))   # ✅ "bb"
print(longest_palindrome_expand("a"))      # ✅ "a"
print(longest_palindrome_expand("ac"))     # ✅ "a" или "c"
