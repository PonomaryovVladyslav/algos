from collections import deque

# Задача: Выполнить обход бинарного дерева по уровням.
# Дано: бинарное дерево с корнем `root`.
# Нужно: вернуть список уровней, где каждый подсписок содержит узлы одного уровня.

class TreeNode:
    """
    Класс узла бинарного дерева.
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode) -> list[list[int]]:
    """
    Функция выполняет обход бинарного дерева по уровням (BFS).

    :param root: TreeNode - корень бинарного дерева.
    :return: list[list[int]] - список узлов, сгруппированных по уровням.
    """

    if not root:
        return []

    queue: deque[TreeNode] = deque([root])
    result: list[list[int]] = []

    while queue:
        level_size: int = len(queue)  # Количество узлов на текущем уровне
        level_nodes: list[int] = []  # Список значений узлов на этом уровне

        for _ in range(level_size):
            node: TreeNode = queue.popleft()
            level_nodes.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_nodes)  # Добавляем уровень в результат

    return result


# 🔹 Тестируем
tree = TreeNode(3,
    TreeNode(9),
    TreeNode(20, TreeNode(15), TreeNode(7))
)

print(level_order(tree))  # Ожидаемый результат: [[3], [9, 20], [15, 7]]

"""
Анализ сложности:
- Временная сложность: O(n), так как мы посещаем каждый узел ровно один раз.
- Пространственная сложность: O(m), где `m` — максимальное количество узлов на одном уровне (ширина дерева).
"""
