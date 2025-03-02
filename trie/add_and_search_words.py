class TrieNode:
    def __init__(self):
        self.children = {}  # O(1) память на хранение ссылок на потомков
        self.is_end = False  # Флаг конца слова


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        """Добавляет слово в Trie.
        Временная сложность: O(m)
        Пространственная сложность: O(n * m) (где n — кол-во слов, m — средняя длина слова)
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # O(1) вставка в HashMap
            node = node.children[char]  # O(1) доступ
        node.is_end = True

    def search(self, word: str) -> bool:
        """Ищет слово в Trie с возможностью использования '.'
        Временная сложность: O(26^m) в худшем случае, O(m) в среднем случае
        Пространственная сложность: O(m) (глубина стека в рекурсии)
        """
        return self._dfs(word, 0, self.root)

    def _dfs(self, word: str, index: int, node: TrieNode) -> bool:
        """Рекурсивный DFS-поиск по Trie."""
        if index == len(word):
            return node.is_end

        char = word[index]

        if char == ".":  # Wildcard (перебираем все возможные пути)
            for child in node.children.values():  # O(26) максимум
                if self._dfs(word, index + 1, child):
                    return True
        elif char in node.children:  # Обычный поиск буквы O(1)
            return self._dfs(word, index + 1, node.children[char])

        return False


# 🔹 Тестирование
wd = WordDictionary()
wd.add_word("bad")
wd.add_word("dad")
wd.add_word("mad")

print(wd.search("pad"))  # ❌ False
print(wd.search("bad"))  # ✅ True
print(wd.search(".ad"))  # ✅ True (".ad" совпадает с "bad", "dad", "mad")
print(wd.search("b.."))  # ✅ True ("b.." совпадает с "bad")
