def find_longest_unique_subsequence(s: str) -> tuple[int, str]:
    """
    Находит самую длинную подстроку без повторяющихся символов.

    🔹 **Алгоритм (O(n))**:
       1️⃣ Используем технику "скользящего окна" с двумя указателями.
       2️⃣ `start` - начало текущего окна, `char_index` - словарь для хранения индексов символов.
       3️⃣ Проходим строку (`O(n)`) и:
           - Если символ уже есть в окне → сдвигаем `start` вперёд.
           - Обновляем индекс текущего символа.
           - Обновляем `max_length` и `longest_substr`, если текущая подстрока длиннее найденных ранее.
       4️⃣ Возвращаем `(максимальную длину, найденную подстроку)`.

    🔹 **Временная сложность**:
       - `O(n)`, так как каждый символ обрабатывается один раз.

    🔹 **Пространственная сложность**:
       - `O(1)`, так как `char_index` хранит максимум 256 символов.

    :param s: str - Исходная строка.
    :return: tuple[int, str] - Длина и сама подстрока без повторяющихся символов.
    """
    start = 0
    max_length = 0
    char_index = {}  # Храним индекс последнего появления символа
    longest_substr = ""

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1  # Сдвигаем левую границу окна

        char_index[char] = i  # Обновляем индекс символа
        current_length = i - start + 1

        if current_length > max_length:
            max_length = current_length
            longest_substr = s[start:i + 1]

    return max_length, longest_substr


# 🔹 Тесты
s1 = "abcabed"
s2 = "bbbbbb"
s3 = "pwwkew"

print(find_longest_unique_subsequence(s1))  # ✅ (5, "cabed")
print(find_longest_unique_subsequence(s2))  # ✅ (1, "b")
print(find_longest_unique_subsequence(s3))  # ✅ (3, "wke")
