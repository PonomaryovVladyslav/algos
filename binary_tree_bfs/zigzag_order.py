from collections import deque

# Задача: Выполнить зигзагообразный обход бинарного дерева.
# Дано: бинарное дерево с корнем `root`.
# Нужно: вернуть список уровней, где узлы на каждом уровне записаны в чередующемся порядке.

class TreeNode:
    """
    Класс узла бинарного дерева.
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root: TreeNode) -> list[list[int]]:
    """
    Функция выполняет зигзагообразный обход бинарного дерева.

    :param root: TreeNode - корень бинарного дерева.
    :return: list[list[int]] - список уровней с чередующимися порядками.
    """

    if not root:
        return []

    queue: deque[TreeNode] = deque([root])
    result: list[list[int]] = []
    left_to_right: bool = True  # Флаг направления обхода

    while queue:
        level_size: int = len(queue)  # Количество узлов на текущем уровне
        level_nodes: deque[int] = deque()  # Двусторонняя очередь для порядка элементов

        for _ in range(level_size):
            node: TreeNode = queue.popleft()
            if left_to_right:
                level_nodes.append(node.val)  # Добавляем в конец (обычный порядок)
            else:
                level_nodes.appendleft(node.val)  # Добавляем в начало (обратный порядок)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level_nodes))
        left_to_right = not left_to_right  # Меняем направление обхода

    return result


# 🔹 Тестируем
tree = TreeNode(3,
    TreeNode(9),
    TreeNode(20, TreeNode(15), TreeNode(7))
)

print(zigzag_level_order(tree))  # Ожидаемый результат: [[3], [20, 9], [15, 7]]

"""
Анализ сложности:
- Временная сложность: O(n), так как мы посещаем каждый узел ровно один раз.
- Пространственная сложность: O(m), где `m` — максимальное количество узлов на одном уровне (ширина дерева).

🔹 Использование `deque` позволяет эффективно добавлять элементы **в начало** и **в конец** за O(1).
"""
