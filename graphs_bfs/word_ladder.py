from collections import deque

def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    """
    Находит минимальное количество шагов для превращения `begin_word` в `end_word`
    через последовательные изменения одной буквы, где каждое промежуточное слово
    должно быть в `word_list`.

    🔹 **Алгоритм (BFS, O(n * m^2))**:
    1️⃣ Преобразуем `word_list` в `set(word_set)` для быстрого поиска.
    2️⃣ Запускаем BFS:
       - В `queue` храним `(слово, шаги)`, начиная с `begin_word`.
       - Меняем **каждую букву** на **все возможные буквы**.
       - Если слово есть в `word_set`, добавляем его в очередь и удаляем из множества.
    3️⃣ Если достигли `end_word`, возвращаем `steps`, иначе `0`.

    🔹 **Временная сложность**:
       - `O(n * m^2)`, где `n` — количество слов в `word_list`, `m` — длина слова.

    🔹 **Пространственная сложность**:
       - `O(n)`, так как храним `word_set` и `queue`.

    :param begin_word: str - Начальное слово.
    :param end_word: str - Целевое слово.
    :param word_list: list[str] - Список доступных слов.
    :return: int - Минимальное количество шагов или `0`, если путь невозможен.
    """
    word_set = set(word_list)  # Превращаем в set для быстрого поиска
    if end_word not in word_set:
        return 0  # Если целевого слова нет в словаре, путь невозможен

    queue = deque([(begin_word, 1)])  # (слово, шаги)
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    while queue:
        word, steps = queue.popleft()

        if word == end_word:
            return steps  # Достигли целевого слова

        # Генерируем все возможные слова, меняя одну букву
        for i in range(len(word)):
            for char in alphabet:
                if char != word[i]:  # Меняем только на другую букву
                    new_word = word[:i] + char + word[i+1:]

                    if new_word in word_set:
                        queue.append((new_word, steps + 1))
                        word_set.remove(new_word)  # Удаляем, чтобы избежать повторений

    return 0  # Если путь не найден

# 🔹 Тесты
print(ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # ✅ 5
print(ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # ✅ 0
