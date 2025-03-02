from collections import deque

# Задача: Найти максимальную глубину бинарного дерева.
# Дано: бинарное дерево с корнем `root`.
# Нужно: вернуть максимальную глубину (количество уровней).

class TreeNode:
    """
    Класс узла бинарного дерева.
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    """
    Функция находит максимальную глубину бинарного дерева (DFS, рекурсия).

    :param root: TreeNode - корень бинарного дерева.
    :return: int - максимальная глубина дерева.
    """

    if not root:
        return 0  # Если дерево пустое

    return 1 + max(max_depth(root.left), max_depth(root.right))  # Рекурсивный вызов


def max_depth_bfs(root: TreeNode) -> int:
    """
    Функция находит максимальную глубину бинарного дерева (BFS, итеративный метод).

    :param root: TreeNode - корень бинарного дерева.
    :return: int - максимальная глубина дерева.
    """

    if not root:
        return 0

    queue: deque[TreeNode] = deque([root])
    depth: int = 0

    while queue:
        for _ in range(len(queue)):  # Проходим по каждому узлу текущего уровня
            node: TreeNode = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth += 1  # Переход на новый уровень

    return depth


# 🔹 Тестируем
tree = TreeNode(3,
    TreeNode(9),
    TreeNode(20, TreeNode(15), TreeNode(7))
)

print(max_depth(tree))  # Ожидаемый результат: 3
print(max_depth_bfs(tree))  # Ожидаемый результат: 3

"""
Анализ сложности:
1. **DFS (рекурсия):**
   - Временная сложность: O(n), так как мы посещаем каждый узел ровно один раз.
   - Пространственная сложность: O(H), где `H` - высота дерева (глубина рекурсии).

2. **BFS (очередь):**
   - Временная сложность: O(n), так как каждый узел посещается один раз.
   - Пространственная сложность: O(m), где `m` — максимальное количество узлов на одном уровне (ширина дерева).

🔹 **DFS проще и рекурсивен**, а **BFS более естественен для итеративного решения**.
"""
