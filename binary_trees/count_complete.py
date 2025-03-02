# Задача: Подсчитать количество узлов в полном бинарном дереве.
# Дано: бинарное дерево с корнем `root`.
# Нужно: вернуть общее количество узлов в дереве.

class TreeNode:
    """
    Класс узла бинарного дерева.
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def count_nodes(root: TreeNode) -> int:
    """
    Функция подсчитывает количество узлов в полном бинарном дереве.

    :param root: TreeNode - корень бинарного дерева.
    :return: int - количество узлов в дереве.
    """

    if not root:
        return 0

    left_height: int = 0
    right_height: int = 0
    left: TreeNode | None = root
    right: TreeNode | None = root

    # Подсчитываем высоту левого и правого поддерева
    while left:
        left = left.left
        left_height += 1

    while right:
        right = right.right
        right_height += 1

    if left_height == right_height:  # Если дерево полное
        return (1 << left_height) - 1  # 2^height - 1

    return 1 + count_nodes(root.left) + count_nodes(root.right)


# 🔹 Тестируем
tree = TreeNode(1,
    TreeNode(2, TreeNode(4), TreeNode(5)),
    TreeNode(3, TreeNode(6))
)

print(count_nodes(tree))  # Ожидаемый результат: 6

"""
Анализ сложности:
- Временная сложность: O(log^2 n), так как:
  - O(log n) уходит на вычисление высоты.
  - O(log n) вызовов рекурсии в худшем случае (половина поддеревьев).
  - Итоговая сложность: O(log n * log n).
- Пространственная сложность: O(log n), так как рекурсия углубляется на высоту дерева.

🔹 Этот алгоритм **эффективнее O(n)** при полном дереве, так как использует **свойство высоты**.
"""
