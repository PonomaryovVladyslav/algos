class TrieNode:
    def __init__(self):
        self.children = {}  # Ключи — буквы, значения — узлы TrieNode
        self.is_end = False  # Флаг конца слова

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Создаём новый узел
            node = node.children[char]  # Переход к следующему узлу
        node.is_end = True  # Устанавливаем флаг конца слова

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_end  # Проверяем флаг конца слова

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None  # Проверяем, есть ли узел с таким префиксом

    def _find(self, prefix: str) -> TrieNode:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None  # Префикс не найден
            node = node.children[char]  # Переход к следующему узлу
        return node  # Возвращаем последний найденный узел


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))    # True
print(trie.search("app"))      # False
print(trie.startsWith("app"))  # True
trie.insert("app")
print(trie.search("app"))      # True
