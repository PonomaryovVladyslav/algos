def longest_substring(s: str) -> int:
    """
    Возвращает длину самой длинной подстроки без повторяющихся символов.

    🔹 **Метод**: Sliding Window (скользящее окно)
    🔹 **Идея**:
       - Используем **окно** (`start` → `i`), расширяя его вправо (`i`).
       - Если символ повторяется, **сдвигаем** `start` вправо.

    🔹 **Сложность**:
       - `O(n)`, где `n` — длина строки (один проход).
       - `O(1)` по памяти (максимум `26` букв алфавита).

    ✅ **Пример**:
       ```
       Вход: "abcabcbb"
       Выход: 3  (abc)
       ```
    """
    start = 0  # Левая граница окна
    max_len = 0
    char_index = {}  # Хранит индекс последнего появления символа

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1  # Перескакиваем повтор

        char_index[char] = i  # Обновляем индекс символа
        max_len = max(max_len, i - start + 1)  # Вычисляем максимум

    return max_len


# 🔹 Тестовые примеры
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = ""
s5 = " "
s6 = "dvdf"
s7 = "tmmzuxt"
s8 = "abccbaabccba"
s9 = "abccbaabccbaabccba"
s10 = "abccbaabccbaabccbaabccba"

print(longest_substring(s1))  # ✅ 3 ("abc")
print(longest_substring(s2))  # ✅ 1 ("b")
print(longest_substring(s3))  # ✅ 3 ("wke")
print(longest_substring(s4))  # ✅ 0 ("")
print(longest_substring(s5))  # ✅ 1 (" ")
print(longest_substring(s6))  # ✅ 3 ("vdf")
print(longest_substring(s7))  # ✅ 5 ("mzuxt")
print(longest_substring(s8))  # ✅ 3 ("abc")
print(longest_substring(s9))  # ✅ 3 ("abc")
print(longest_substring(s10))  # ✅ 3 ("abc")
