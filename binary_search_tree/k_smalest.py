# Задача: Найти k-й наименьший элемент в бинарном дереве поиска (BST).
# Дано: корень `root` бинарного дерева поиска и число `k`.
# Нужно: вернуть `k`-й наименьший элемент (в порядке возрастания).

class TreeNode:
    """
    Класс узла бинарного дерева поиска (BST).
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: TreeNode, k: int) -> int:
    """
    Рекурсивный метод поиска k-го наименьшего элемента в BST (через inorder-проход).

    :param root: TreeNode - корень бинарного дерева поиска.
    :param k: int - номер наименьшего элемента (1-based index).
    :return: int - значение k-го наименьшего элемента.
    """

    count = 0
    result: int | None = None

    def inorder(node: TreeNode) -> None:
        nonlocal count, result
        if not node or result is not None:
            return

        inorder(node.left)  # Рекурсивный обход влево

        count += 1
        if count == k:  # Если нашли k-й элемент
            result = node.val
            return

        inorder(node.right)  # Рекурсивный обход вправо

    inorder(root)
    return result  # Гарантируется, что `k` валиден


# 🔹 Тестируем
tree = TreeNode(3,
    TreeNode(1, None, TreeNode(2)),
    TreeNode(4)
)

print(kth_smallest(tree, 1))  # Ожидаемый результат: 1
print(kth_smallest(tree, 2))  # Ожидаемый результат: 2
print(kth_smallest(tree, 3))  # Ожидаемый результат: 3
print(kth_smallest(tree, 4))  # Ожидаемый результат: 4


def kth_smallest_iterative(root: TreeNode, k: int) -> int:
    """
    Итеративный метод поиска k-го наименьшего элемента в BST (через стек).

    :param root: TreeNode - корень бинарного дерева поиска.
    :param k: int - номер наименьшего элемента (1-based index).
    :return: int - значение k-го наименьшего элемента.
    """

    stack: list[TreeNode] = []
    node: TreeNode | None = root

    while True:
        while node:
            stack.append(node)
            node = node.left  # Двигаемся влево

        node = stack.pop()  # Достаем узел
        k -= 1

        if k == 0:
            return node.val  # Нашли `k`-й элемент

        node = node.right  # Двигаемся вправо


# 🔹 Тестируем (итеративный метод)
print(kth_smallest_iterative(tree, 1))  # Ожидаемый результат: 1
print(kth_smallest_iterative(tree, 2))  # Ожидаемый результат: 2
print(kth_smallest_iterative(tree, 3))  # Ожидаемый результат: 3
print(kth_smallest_iterative(tree, 4))  # Ожидаемый результат: 4

"""
Анализ сложности:
- Временная сложность: O(H + k), где `H` — высота дерева, так как мы делаем `k` итераций.
  В сбалансированном дереве `H = log n`, в вырожденном `H = n`, так что в среднем O(log n + k).
- Пространственная сложность:
  - O(H) для рекурсивного метода (из-за глубины рекурсии).
  - O(H) для итеративного метода (из-за стека).
"""
