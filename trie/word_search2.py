class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Если здесь заканчивается слово, оно будет не None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word  # Сохраняем слово в конце пути


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)  # Заполняем Trie

        rows, cols = len(board), len(board[0])
        result = set()  # Используем set, чтобы избежать дубликатов

        def dfs(r, c, node):
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


board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
]
words = ["oath","pea","eat","rain"]

sol = Solution()
print(sol.findWords(board, words))  # ["oath", "eat"]
