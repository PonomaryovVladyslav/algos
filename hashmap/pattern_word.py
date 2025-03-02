def pattern_word(pattern: str, s: str) -> bool:
    """
    Проверяет, соответствует ли строка `s` шаблону `pattern`.

    🔹 **Алгоритм (O(n))**:
       1️⃣ Разбиваем `s` на слова `words`.
       2️⃣ Если длина `words` не совпадает с длиной `pattern`, возвращаем `False`.
       3️⃣ Используем два словаря (`letter_to_word` и `word_to_letter`) для хранения
          соответствий **букв** и **слов**.
       4️⃣ Проходим по `pattern` и `words` одновременно:
          - Если буква и слово уже связаны друг с другом, продолжаем.
          - Если буква или слово уже связаны с другим элементом, возвращаем `False`.
          - Добавляем соответствие в словари.
       5️⃣ Если прошли весь `pattern` без ошибок, возвращаем `True`.

    🔹 **Временная сложность**:
       - `O(n)`, где `n` — длина `pattern` (или `words`).

    🔹 **Пространственная сложность**:
       - `O(n)`, так как храним `n` пар в `letter_to_word` и `word_to_letter`.

    :param pattern: str - Шаблон из букв.
    :param s: str - Входная строка (слова, разделенные пробелами).
    :return: bool - `True`, если строка соответствует шаблону, иначе `False`.
    """
    words = s.split()
    if len(words) != len(pattern):
        return False

    letter_to_word = {}
    word_to_letter = {}

    for word, letter in zip(words, pattern):
        if (word in word_to_letter and letter != word_to_letter[word]) or \
           (letter in letter_to_word and word != letter_to_word[letter]):
            return False

        letter_to_word[letter] = word
        word_to_letter[word] = letter

    return True


# 🔹 Тесты
print(pattern_word("abba", "dog cat cat dog"))  # ✅ True
print(pattern_word("abba", "dog cat cat fish"))  # ✅ False
print(pattern_word("aaaa", "dog dog dog dog"))  # ✅ True
print(pattern_word("abba", "dog dog dog dog"))  # ✅ False
print(pattern_word("aaa", "aa aa aa aa"))  # ✅ False
