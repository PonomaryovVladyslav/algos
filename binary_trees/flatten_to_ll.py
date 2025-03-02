# Задача: Преобразовать бинарное дерево в "связанный список" по порядку обхода в глубину (preorder).
# Дано: бинарное дерево с корнем `root`.
# Нужно: изменить структуру так, чтобы все узлы были связаны через `right`, а `left` был `None`.

class TreeNode:
    """
    Класс узла бинарного дерева.
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root: TreeNode) -> None:
    """
    Функция преобразует бинарное дерево в "связанный список" в порядке preorder (модифицирует на месте).

    :param root: TreeNode - корень бинарного дерева.
    """

    curr: TreeNode | None = root

    while curr:
        if curr.left:
            # Находим крайний правый узел в левом поддереве
            predecessor: TreeNode = curr.left
            while predecessor.right:
                predecessor = predecessor.right

            # Перемещаем `right` поддерево
            predecessor.right = curr.right
            curr.right = curr.left
            curr.left = None  # Обнуляем `left`

        curr = curr.right  # Переходим дальше


# 🔹 Исходное дерево:
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
tree = TreeNode(1,
    TreeNode(2, TreeNode(3), TreeNode(4)),
    TreeNode(5, None, TreeNode(6))
)

flatten(tree)

# 🔹 Выводим результат в виде списка
curr: TreeNode | None = tree
while curr:
    print(curr.val, end=" -> ")
    curr = curr.right
# Ожидаемый вывод: 1 -> 2 -> 3 -> 4 -> 5 -> 6

"""
Анализ сложности:
- Временная сложность: O(n), так как мы проходим по каждому узлу только один раз.
- Пространственная сложность: O(1), так как изменение происходит на месте (in-place).

🔹 Этот метод использует **Morris Traversal**, избегая рекурсии и дополнительной памяти.
"""
