# Задача: Найти минимальную разницу между любыми двумя узлами в бинарном дереве поиска (BST).
# Дано: корень `root` бинарного дерева поиска.
# Нужно: вернуть минимальную абсолютную разницу между значениями двух узлов.

class TreeNode:
    """
    Класс узла бинарного дерева поиска (BST).
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def get_minimum_difference(root: TreeNode) -> int:
    """
    Функция вычисляет минимальную разницу между любыми двумя узлами BST (рекурсивный inorder).

    :param root: TreeNode - корень бинарного дерева поиска.
    :return: int - минимальная абсолютная разница между значениями узлов.
    """

    min_diff: int = float('inf')
    prev: int | None = None

    def inorder(node: TreeNode) -> None:
        """
        Обход дерева в порядке inorder (LNR), чтобы получить отсортированные элементы BST.

        :param node: TreeNode - текущий узел.
        """
        nonlocal min_diff, prev
        if not node:
            return

        inorder(node.left)  # Левое поддерево

        if prev is not None:
            min_diff = min(min_diff, node.val - prev)  # Обновляем разницу
        prev = node.val  # Обновляем предыдущий узел

        inorder(node.right)  # Правое поддерево

    inorder(root)
    return min_diff


# 🔹 Тестируем
tree = TreeNode(4,
    TreeNode(2, TreeNode(1), TreeNode(3)),
    TreeNode(6)
)

print(get_minimum_difference(tree))  # Ожидаемый результат: 1


def get_minimum_difference_iterative(root: TreeNode) -> int:
    """
    Функция вычисляет минимальную разницу между любыми двумя узлами BST (итеративный inorder).

    :param root: TreeNode - корень бинарного дерева поиска.
    :return: int - минимальная абсолютная разница между значениями узлов.
    """

    min_diff: int = float('inf')
    prev: int | None = None
    stack: list[TreeNode] = []
    node: TreeNode | None = root

    while stack or node:
        while node:
            stack.append(node)
            node = node.left  # Двигаемся влево

        node = stack.pop()  # Достаем узел

        if prev is not None:
            min_diff = min(min_diff, node.val - prev)  # Обновляем разницу
        prev = node.val  # Запоминаем предыдущий узел

        node = node.right  # Двигаемся вправо

    return min_diff


# 🔹 Тестируем (итеративный метод)
print(get_minimum_difference_iterative(tree))  # Ожидаемый результат: 1

"""
Анализ сложности:
- Временная сложность: O(n), так как мы посещаем каждый узел ровно один раз (inorder обход).
- Пространственная сложность:
  - O(H) для рекурсивного метода (глубина рекурсии).
  - O(H) для итеративного метода (из-за стека).
  В сбалансированном дереве `H = log n`, в вырожденном `H = n`, так что в среднем O(log n).
"""
