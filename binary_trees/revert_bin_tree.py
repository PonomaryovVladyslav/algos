from collections import deque


# Задача: Инвертировать бинарное дерево (зеркальное отражение).
# Дано: корень `root` бинарного дерева.
# Нужно: вернуть инвертированное дерево.

class TreeNode:
    """
    Класс узла бинарного дерева.
    """

    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode) -> TreeNode | None:
    """
    Функция инвертирует бинарное дерево (DFS, рекурсия).

    🔹 Временная сложность: O(n), так как посещаем каждый узел ровно один раз.
    🔹 Пространственная сложность: O(H), где `H` — высота дерева (глубина рекурсии).

    :param root: TreeNode - корень бинарного дерева.
    :return: TreeNode | None - инвертированное бинарное дерево.
    """

    if not root:
        return None  # Если пустое дерево

    root.left, root.right = root.right, root.left  # Меняем местами

    invert_tree(root.left)  # Инвертируем левое поддерево
    invert_tree(root.right)  # Инвертируем правое поддерево

    return root


def invert_tree_bfs(root: TreeNode) -> TreeNode | None:
    """
    Функция инвертирует бинарное дерево (BFS, итеративный метод).

    🔹 Временная сложность: O(n), так как мы посещаем каждый узел ровно один раз.
    🔹 Пространственная сложность: O(n), так как в худшем случае в `queue` окажется весь уровень.

    :param root: TreeNode - корень бинарного дерева.
    :return: TreeNode | None - инвертированное бинарное дерево.
    """

    if not root:
        return None

    queue: deque[TreeNode] = deque([root])

    while queue:
        node: TreeNode = queue.popleft()
        node.left, node.right = node.right, node.left  # Меняем местами

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root


# 🔹 Тестируем
tree = TreeNode(4,
                TreeNode(2, TreeNode(1), TreeNode(3)),
                TreeNode(7, TreeNode(6), TreeNode(9))
                )

# Инвертируем с помощью DFS
inverted_tree_dfs = invert_tree(tree)

# Инвертируем с помощью BFS (новое дерево)
tree = TreeNode(4,
                TreeNode(2, TreeNode(1), TreeNode(3)),
                TreeNode(7, TreeNode(6), TreeNode(9))
                )
inverted_tree_bfs = invert_tree_bfs(tree)

"""
🔹 Сравнение методов:

1️⃣ `invert_tree()` (DFS, рекурсивный)
   - Временная сложность: O(n) — посещаем каждый узел ровно один раз.
   - Пространственная сложность: O(H) — глубина рекурсии (H = log n в сбалансированном дереве, H = n в худшем случае).

2️⃣ `invert_tree_bfs()` (BFS, очередь)
   - Временная сложность: O(n) — посещаем каждый узел ровно один раз.
   - Пространственная сложность: O(n) — в худшем случае храним весь уровень в `queue`.

✅ Вывод:
   - **DFS проще и использует O(H) памяти** (лучше для глубоких деревьев).
   - **BFS использует O(n) памяти** (лучше для сбалансированных деревьев).
"""
