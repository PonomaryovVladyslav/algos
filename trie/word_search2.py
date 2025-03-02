class TrieNode:
    """ Узел Trie, содержащий ссылки на дочерние узлы и возможное слово. """

    def __init__(self):
        self.children = {}  # Дочерние узлы (буква -> узел)
        self.word = None  # Если узел — конец слова, здесь будет храниться слово


class Trie:
    """
    Реализация Trie (префиксного дерева) для хранения списка слов.

    Операции:
    - insert(word): добавляет слово в Trie.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """ Добавляет слово в Trie. """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Создаём новый узел
            node = node.children[char]  # Переход к следующему узлу
        node.word = word  # Сохраняем слово в конце пути


class Solution:
    """
    Решение задачи поиска слов на доске (Word Search II).

    Задача:
    - Дана двумерная сетка `board` с буквами.
    - Дано множество слов `words`.
    - Нужно найти все слова из `words`, которые можно составить,
      двигаясь по соседним буквам (горизонтально или вертикально).

    Решение:
    - Используем Trie для эффективного хранения `words`.
    - Запускаем DFS из каждой клетки доски.
    - По ходу DFS проверяем, есть ли путь в Trie.
    - Когда встречаем полное слово, добавляем его в `result`.

    Время: O(M * N * 4^L), где:
        - M, N — размеры доски
        - L — средняя длина слов
        - 4^L — максимальное количество путей в DFS (четыре направления)

    Пространство: O(W * L + M * N), где:
        - W — число слов
        - L — средняя длина слов
        - M * N — размер вспомогательного стека DFS.
    """

    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)  # Заполняем Trie

        rows, cols = len(board), len(board[0])
        result = set()  # Используем set, чтобы избежать дубликатов

        def dfs(r, c, node):
            """ Поиск слова из текущей позиции (r, c). """
            char = board[r][c]
            if char not in node.children:
                return  # Если нет такого пути в Trie, выходим

            node = node.children[char]
            if node.word:  # Нашли полное слово
                result.add(node.word)

            board[r][c] = "#"  # Помечаем как посещённую
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 4 направления
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, node)
            board[r][c] = char  # Восстанавливаем букву

        # Запускаем DFS из каждой клетки
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)

        return list(result)


# Пример входных данных
board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"]
]
words = ["oath", "pea", "eat", "rain"]

sol = Solution()
print(sol.findWords(board, words))  # ["oath", "eat"]
