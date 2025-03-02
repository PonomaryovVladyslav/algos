from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Группирует слова, которые являются анаграммами.

    🔹 **Алгоритм (O(n * k log k))**:
    1️⃣ Создаём `defaultdict(list)`, где ключом будет отсортированное слово, а значением — список анаграмм.
    2️⃣ Перебираем слова `strs`:
       - Сортируем буквы в слове (`sorted_word = "".join(sorted(word))`).
       - Добавляем `word` в `anagram_map[sorted_word]`.
    3️⃣ Возвращаем `list(anagram_map.values())`, т.е. группы анаграмм.

    🔹 **Временная сложность**:
       - `O(n * k log k)`, где `n` — количество слов, `k` — средняя длина слова.

    🔹 **Пространственная сложность**:
       - `O(n * k)`, так как храним все слова и их ключи.

    :param strs: list[str] - Список слов.
    :return: list[list[str]] - Список групп анаграмм.
    """
    anagram_map = defaultdict(list)

    for word in strs:
        sorted_word = "".join(sorted(word))  # Преобразуем слово в сортированный ключ
        anagram_map[sorted_word].append(word)  # Группируем анаграммы

    return list(anagram_map.values())  # Возвращаем сгруппированные анаграммы

# 🔹 Тесты
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# ✅ [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

print(group_anagrams([""]))
# ✅ [[""]]

print(group_anagrams(["a"]))
# ✅ [["a"]]
