from collections import deque

# Задача: Найти среднее значение каждого уровня бинарного дерева.
# Дано: бинарное дерево с корнем `root`.
# Нужно: вернуть список, где `i`-й элемент — это среднее значение узлов на `i`-м уровне.

class TreeNode:
    """
    Класс узла бинарного дерева.
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(root: TreeNode) -> list[float]:
    """
    Функция вычисляет среднее значение узлов на каждом уровне дерева.

    :param root: TreeNode - корень бинарного дерева.
    :return: list[float] - список средних значений на каждом уровне.
    """

    if not root:
        return []

    queue: deque[TreeNode] = deque([root])
    result: list[float] = []

    while queue:
        level_size: int = len(queue)  # Количество узлов на текущем уровне
        level_sum: float = 0  # Сумма значений узлов на уровне

        for _ in range(level_size):
            node: TreeNode = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_sum / level_size)  # Добавляем среднее значение уровня

    return result


# 🔹 Тестируем
tree = TreeNode(3,
    TreeNode(9),
    TreeNode(20, TreeNode(15), TreeNode(7))
)

print(average_of_levels(tree))  # Ожидаемый результат: [3.00000, 14.50000, 11.00000]

"""
Анализ сложности:
- Временная сложность: O(n), так как мы посещаем каждый узел ровно один раз.
- Пространственная сложность: O(m), где `m` — максимальное количество узлов на одном уровне (ширина дерева).
"""
