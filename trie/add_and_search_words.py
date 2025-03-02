class TrieNode:
    def __init__(self):
        self.children = {}  # Ключи — буквы, значения — узлы TrieNode
        self.is_end = False  # Флаг конца слова


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Создаём новый узел
            node = node.children[char]  # Переход к следующему узлу
        node.is_end = True  # Устанавливаем флаг конца слова

    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.root)  # Запускаем DFS от корня

    def _dfs(self, word: str, index: int, node: TrieNode) -> bool:
        if index == len(word):
            return node.is_end  # Если дошли до конца, проверяем, является ли узел концом слова

        char = word[index]

        if char == ".":  # Обрабатываем wildcard '.'
            for child in node.children.values():  # Проверяем все возможные буквы
                if self._dfs(word, index + 1, child):
                    return True
        else:  # Обычный поиск буквы
            if char in node.children:
                return self._dfs(word, index + 1, node.children[char])

        return False  # Если совпадения не найдены

wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
print(wd.search("pad"))  # False
print(wd.search("bad"))  # True
print(wd.search(".ad"))  # True (".ad" совпадает с "bad", "dad", "mad")
print(wd.search("b.."))  # True ("b.." совпадает с "bad")
