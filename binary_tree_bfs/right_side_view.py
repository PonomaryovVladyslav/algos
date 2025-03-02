from collections import deque

# Задача: Найти видимые узлы при просмотре бинарного дерева справа.
# Дано: бинарное дерево с корнем `root`.
# Нужно: вернуть список значений узлов, которые видны справа.

class TreeNode:
    """
    Класс узла бинарного дерева.
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: TreeNode) -> list[int]:
    """
    Функция возвращает список узлов, видимых при просмотре бинарного дерева справа (BFS).

    :param root: TreeNode - корень бинарного дерева.
    :return: list[int] - список видимых узлов.
    """

    if not root:
        return []

    queue: deque[TreeNode] = deque([root])
    result: list[int] = []

    while queue:
        level_size: int = len(queue)  # Количество узлов на текущем уровне
        for i in range(level_size):
            node: TreeNode = queue.popleft()
            if i == level_size - 1:  # Последний узел уровня (справа)
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


# 🔹 Тестируем (метод BFS)
tree = TreeNode(1,
    TreeNode(2, None, TreeNode(5)),
    TreeNode(3, None, TreeNode(4))
)

print(right_side_view(tree))  # Ожидаемый результат: [1, 3, 4]


def right_side_view_dfs(root: TreeNode) -> list[int]:
    """
    Функция возвращает список узлов, видимых при просмотре бинарного дерева справа (DFS).

    :param root: TreeNode - корень бинарного дерева.
    :return: list[int] - список видимых узлов.
    """

    result: list[int] = []

    def dfs(node: TreeNode, level: int) -> None:
        """
        Обход дерева в глубину (DFS), начиная с правых узлов.

        :param node: TreeNode - текущий узел.
        :param level: int - текущий уровень дерева.
        """
        if not node:
            return

        if level == len(result):  # Если это первый узел на уровне (самый правый)
            result.append(node.val)

        dfs(node.right, level + 1)  # Сначала идем вправо
        dfs(node.left, level + 1)  # Затем влево

    dfs(root, 0)
    return result


# 🔹 Тестируем (метод DFS)
print(right_side_view_dfs(tree))  # Ожидаемый результат: [1, 3, 4]

"""
Анализ сложности:
1. **Метод BFS (по уровням с очередью):**
   - Временная сложность: O(n), так как посещаем каждый узел ровно один раз.
   - Пространственная сложность: O(m), где `m` — максимальное количество узлов на одном уровне (ширина дерева).

2. **Метод DFS (обход в глубину с рекурсией):**
   - Временная сложность: O(n), так как проходим по каждому узлу один раз.
   - Пространственная сложность: O(H), где `H` — высота дерева (глубина рекурсии).
     В сбалансированном дереве `H = log n`, в вырожденном `H = n`, так что в среднем O(log n).

🔹 **Метод DFS часто быстрее**, так как он не требует хранения всех узлов уровня.
"""
