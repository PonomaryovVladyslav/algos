def word_break(s: str, word_dict: list[str]) -> bool:
    """
    Функция проверяет, можно ли разбить строку `s` на слова из `word_dict`.

    🔹 Алгоритм (Динамическое программирование O(n²)):
    1️⃣ Используем булев массив `dp`, где `dp[i]` — можно ли разбить `s[:i]`.
    2️⃣ Инициализируем `dp[0] = True` (пустая строка всегда допустима).
    3️⃣ Перебираем `i` от 1 до `len(s)`:
        - Проверяем каждое `j` от 0 до `i`:
          - Если `dp[j] == True` и `s[j:i]` есть в `word_set`, то `dp[i] = True`.
    4️⃣ Итоговый ответ: `dp[len(s)]`.

    🔹 Временная сложность: **O(n²)** — два вложенных цикла.
    🔹 Пространственная сложность: **O(n)** — массив `dp`.

    :param s: str - входная строка.
    :param word_dict: list[str] - словарь допустимых слов.
    :return: bool - можно ли разбить строку на слова из `word_dict`.
    """

    word_set = set(word_dict)  # Преобразуем в множество для быстрого поиска
    dp = [False] * (len(s) + 1)
    dp[0] = True  # Пустая строка всегда валидна

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # Нашли разбиение, идём дальше

    return dp[len(s)]


# 🔹 Тестируем
print(word_break("leetcode", ["leet", "code"]))  # ✅ True
print(word_break("applepenapple", ["apple", "pen"]))  # ✅ True
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # ❌ False
print(word_break("aaaaaaa", ["aaaa", "aaa"]))  # ✅ True
print(word_break("abcd", ["a", "abc", "b", "cd"]))  # ✅ True
