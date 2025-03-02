def longest_common_substring(s1: str, s2: str) -> tuple[int, str]:
    """
    Функция находит **наибольшую общую подстроку** между `s1` и `s2`.

    🔹 Алгоритм (Динамическое программирование O(m * n)):
    1️⃣ Используем `dp[i][j]`, где `dp[i][j]` — длина LCS, заканчивающейся в `s1[i-1]` и `s2[j-1]`.
    2️⃣ Если `s1[i-1] == s2[j-1]`, увеличиваем длину подстроки `dp[i][j] = dp[i-1][j-1] + 1`.
    3️⃣ Обновляем `max_length` и `end_index`, если `dp[i][j]` стал больше `max_length`.
    4️⃣ Используем **две строки `prev` и `curr`** для оптимизации памяти (`O(n)`).
    5️⃣ Итоговая подстрока: `s1[end_index - max_length:end_index]`.

    🔹 Временная сложность: **O(m * n)** — два вложенных цикла.
    🔹 Пространственная сложность: **O(n)** — используем `prev` и `curr`.

    :param s1: str - первая строка.
    :param s2: str - вторая строка.
    :return: tuple[int, str] - длина наибольшей общей подстроки и сама подстрока.
    """

    m, n = len(s1), len(s2)
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    max_length = 0
    end_index = 0

    # Заполняем DP таблицу
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:  # Символы совпадают
                curr[j] = prev[j - 1] + 1
                if curr[j] > max_length:
                    max_length = curr[j]
                    end_index = i
            else:
                curr[j] = 0  # Разрыв подстроки

        prev, curr = curr, prev  # Обновляем строки (rolling DP)

    # Восстанавливаем подстроку
    longest_substring = s1[end_index - max_length:end_index]

    return max_length, longest_substring


# 🔹 Тестируем
s1 = "abcdef"
s2 = "zbcdf"
length, substring = longest_common_substring(s1, s2)
print(f"Длина: {length}, Подстрока: '{substring}'")  # ✅ Длина: 3, Подстрока: 'bcd'

s1 = "abcde"
s2 = "ace"
length, substring = longest_common_substring(s1, s2)
print(f"Длина: {length}, Подстрока: '{substring}'")  # ✅ Длина: 1, Подстрока: 'a'

s1 = "abcdxyz"
s2 = "xyzabcd"
length, substring = longest_common_substring(s1, s2)
print(f"Длина: {length}, Подстрока: '{substring}'")  # ✅ Длина: 4, Подстрока: 'abcd'

s1 = "abcdef"
s2 = "ghijkl"
length, substring = longest_common_substring(s1, s2)
print(f"Длина: {length}, Подстрока: '{substring}'")  # ✅ Длина: 0, Подстрока: ''
