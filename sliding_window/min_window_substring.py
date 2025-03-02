from collections import Counter

def min_window(s: str, t: str) -> str:
    """
    Находит минимальное подстроку `s`, содержащую все символы `t`.

    🔹 **Метод**: Sliding Window + HashMap (Counter)
    🔹 **Идея**:
       - Двигаем `right`, добавляем символы в окно.
       - Когда окно содержит `t`, двигаем `left`, сокращая окно.
       - Запоминаем минимальную подстроку.

    🔹 **Сложность**:
       - `O(n)`, один проход по `s`.
       - `O(1)`, т.к. символов всего 128 (ASCII).

    ✅ **Пример**:
       ```
       Вход: s = "ADOBECODEBANC", t = "ABC"
       Выход: "BANC"
       ```
    """
    if not s or not t:
        return ""

    target_count = Counter(t)  # Словарь нужных символов
    window_count = {}  # Словарь текущего окна

    left, right = 0, 0  # Два указателя окна
    required = len(target_count)  # Кол-во уникальных символов в t
    formed = 0  # Кол-во символов в окне, совпадающих с target_count
    min_len = float("inf")
    min_window = ""

    while right < len(s):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        if char in target_count and window_count[char] == target_count[char]:
            formed += 1

        # Когда найдено все, что нужно — сужаем окно
        while left <= right and formed == required:
            char = s[left]

            # Обновляем минимальное окно
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = s[left:right+1]

            window_count[char] -= 1
            if char in target_count and window_count[char] < target_count[char]:
                formed -= 1  # Если удалили нужный символ, уменьшаем formed

            left += 1  # Двигаем левую границу окна

        right += 1  # Двигаем правую границу окна

    return min_window

# 🔹 Тестовые примеры
print(min_window("ADOBECODEBANC", "ABC"))  # ✅ "BANC"
print(min_window("a", "a"))  # ✅ "a"
print(min_window("a", "aa"))  # ✅ ""
print(min_window("ab", "a"))  # ✅ "a"
print(min_window("abcdebdde", "bde"))  # ✅ "bdde"
