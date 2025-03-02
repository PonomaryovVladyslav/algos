class TrieNode:
    """ Узел Trie, содержащий ссылки на дочерние узлы и флаг конца слова. """

    def __init__(self):
        self.children = {}  # Словарь дочерних узлов (буква -> узел)
        self.is_end = False  # Флаг конца слова


class Trie:
    """
    Реализация префиксного дерева (Trie) для хранения и поиска слов.

    Операции:
    - insert(word): добавляет слово в Trie.
    - search(word): проверяет, есть ли слово в Trie.
    - starts_with(prefix): проверяет, начинается ли слово с prefix.

    Примеры использования:
    >>> trie = Trie()
    >>> trie.insert("apple")
    >>> trie.search("apple")  # True
    >>> trie.search("app")  # False
    >>> trie.starts_with("app")  # True
    >>> trie.insert("app")
    >>> trie.search("app")  # True
    """

    def __init__(self):
        """ Инициализация Trie с корневым узлом. """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Добавляет слово в Trie.

        Время: O(m), где m - длина слова.
        Пространство: O(m), если слово ранее отсутствовало в Trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Создаём новый узел
            node = node.children[char]  # Переход к следующему узлу
        node.is_end = True  # Отмечаем конец слова

    def search(self, word: str) -> bool:
        """
        Проверяет, содержится ли слово в Trie.

        Время: O(m), где m - длина слова.
        Пространство: O(1), так как не создаём новые узлы.
        """
        node = self._find(word)
        return node is not None and node.is_end  # Проверяем, является ли узел концом слова

    def starts_with(self, prefix: str) -> bool:
        """
        Проверяет, начинается ли хотя бы одно слово в Trie с prefix.

        Время: O(m), где m - длина prefix.
        Пространство: O(1), так как не создаём новые узлы.
        """
        return self._find(prefix) is not None  # Проверяем, есть ли узел с таким префиксом

    def _find(self, prefix: str) -> TrieNode:
        """
        Вспомогательная функция, находит узел, соответствующий последнему символу prefix.

        Время: O(m), где m - длина prefix.
        Пространство: O(1), так как не создаём новые узлы.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None  # Префикс не найден
            node = node.children[char]  # Переход к следующему узлу
        return node  # Возвращаем последний найденный узел


# Тестирование
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # True
print(trie.search("app"))  # False
print(trie.starts_with("app"))  # True
trie.insert("app")
print(trie.search("app"))  # True
