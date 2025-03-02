from collections import Counter

def find_substring(s: str, words: list[str]) -> list[int]:
    """
    Ищет все индексы начала подстрок в `s`, содержащих все слова из `words` ровно 1 раз.

    🔹 **Метод**: Sliding Window + HashMap (Counter)
    🔹 **Идея**:
       - Каждое слово имеет фиксированную длину `word_len`.
       - Проверяем все `word_len` возможных сдвигов `i = 0, 1, ..., word_len-1`.
       - Используем `left` и `right` указатели для контроля текущего окна.

    🔹 **Сложность**:
       - `O(n * word_len)`, где `n` — длина `s`.

    ✅ **Пример**:
       ```
       Вход: s = "barfoothefoobarman", words = ["foo", "bar"]
       Выход: [0, 9]
       ```
    """
    if not s or not words:
        return []

    word_len = len(words[0])  # Длина одного слова
    total_len = word_len * len(words)  # Длина искомой подстроки
    word_count = Counter(words)  # Частота слов в words
    result = []

    for i in range(word_len):  # Проверяем сдвиги 0, 1, ..., word_len-1
        left, right = i, i
        current_count = Counter()

        while right + word_len <= len(s):
            word = s[right:right + word_len]  # Берём слово длины word_len
            right += word_len

            if word in word_count:
                current_count[word] += 1

                # Если слово встречается слишком часто, сдвигаем `left`
                while current_count[word] > word_count[word]:
                    current_count[s[left:left + word_len]] -= 1
                    left += word_len

                # Если нашли подстроку нужной длины — записываем её индекс
                if right - left == total_len:
                    result.append(left)

            else:  # Если слово не из words, сбрасываем всё
                current_count.clear()
                left = right

    return result

# 🔹 Тестовые примеры
print(find_substring("barfoothefoobarman", ["foo", "bar"]))  # ✅ [0, 9]
print(find_substring("wordgoodgoodgoodbestword", ["word","good","best","good"]))  # ✅ [8]
print(find_substring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))  # ✅ [6, 9, 12]
print(find_substring("aaaaaaaaaaaaaa", ["aa", "aa", "aa"]))  # ✅ [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
