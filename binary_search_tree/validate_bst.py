# Задача: Проверить, является ли бинарное дерево поиска (BST) корректным.
# Дано: корень `root` бинарного дерева.
# Нужно: вернуть `True`, если это корректное BST, иначе `False`.

class TreeNode:
    """
    Класс узла бинарного дерева поиска (BST).
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode) -> bool:
    """
    Функция проверяет, является ли дерево `root` корректным BST (метод с диапазонами значений).

    :param root: TreeNode - корень бинарного дерева.
    :return: bool - `True`, если `root` - корректный BST, иначе `False`.
    """

    def validate(node: TreeNode, min_val: float, max_val: float) -> bool:
        """
        Рекурсивная проверка узла BST.

        :param node: TreeNode - текущий узел.
        :param min_val: float - минимально допустимое значение (левая граница).
        :param max_val: float - максимально допустимое значение (правая граница).
        :return: bool - `True`, если узел соблюдает правила BST.
        """
        if not node:
            return True

        if not (min_val < node.val < max_val):  # Нарушение свойства BST
            return False

        return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

    return validate(root, float('-inf'), float('inf'))


# 🔹 Тестируем (метод с диапазонами значений)
# Верное BST
tree1 = TreeNode(2, TreeNode(1), TreeNode(3))
print(is_valid_bst(tree1))  # Ожидаемый результат: True

# Неверное BST
tree2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(is_valid_bst(tree2))  # Ожидаемый результат: False


def is_valid_bst_inorder(root: TreeNode) -> bool:
    """
    Функция проверяет, является ли дерево `root` корректным BST (метод с inorder обходом).

    :param root: TreeNode - корень бинарного дерева.
    :return: bool - `True`, если `root` - корректный BST, иначе `False`.
    """

    prev: float = float('-inf')

    def inorder(node: TreeNode) -> bool:
        """
        Рекурсивный inorder обход для проверки BST.

        :param node: TreeNode - текущий узел.
        :return: bool - `True`, если узлы идут в порядке возрастания.
        """
        nonlocal prev
        if not node:
            return True

        if not inorder(node.left):  # Левое поддерево
            return False

        if node.val <= prev:  # Если порядок нарушен
            return False
        prev = node.val  # Запоминаем предыдущий узел

        return inorder(node.right)  # Правое поддерево

    return inorder(root)


# 🔹 Тестируем (метод с inorder обходом)
print(is_valid_bst_inorder(tree1))  # Ожидаемый результат: True
print(is_valid_bst_inorder(tree2))  # Ожидаемый результат: False

"""
Анализ сложности:
1. **Метод с диапазонами значений:**
   - Временная сложность: O(n), так как каждый узел посещается ровно один раз.
   - Пространственная сложность: O(H), где `H` - высота дерева (глубина рекурсии).

2. **Метод с inorder обходом:**
   - Временная сложность: O(n), так как мы проходим по всем узлам.
   - Пространственная сложность: O(H), так как используется стек рекурсии.

🔹 Метод с диапазонами значений **более естественен** для проверки BST, но **метод с inorder обходом** интуитивно показывает отсортированность значений.
"""
