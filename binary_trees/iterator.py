# Задача: Реализовать итератор для бинарного дерева поиска (BST).
# Дано: корень `root` бинарного дерева поиска.
# Нужно: создать класс `BSTIterator`, который поддерживает `next()` и `has_next()`.

class TreeNode:
    """
    Класс узла бинарного дерева.
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    """
    Итератор для BST (метод с предварительным `inorder` обходом).
    """
    def __init__(self, root: TreeNode):
        self.nodes: list[int] = []
        self.index: int = -1
        self._inorder(root)

    def _inorder(self, node: TreeNode | None) -> None:
        """
        Рекурсивный обход в `inorder` (LNR) и сохранение значений в `self.nodes`.
        """
        if node:
            self._inorder(node.left)
            self.nodes.append(node.val)
            self._inorder(node.right)

    def next(self) -> int:
        """
        Возвращает следующий минимальный элемент в BST.
        """
        self.index += 1
        return self.nodes[self.index]

    def has_next(self) -> bool:
        """
        Проверяет, есть ли следующий элемент.
        """
        return self.index + 1 < len(self.nodes)


# 🔹 Тестируем (метод с сохранением `inorder` обхода)
tree = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
iterator = BSTIterator(tree)

print(iterator.next())    # Ожидаемый результат: 3
print(iterator.next())    # Ожидаемый результат: 7
print(iterator.has_next()) # True
print(iterator.next())    # Ожидаемый результат: 9
print(iterator.has_next()) # True
print(iterator.next())    # Ожидаемый результат: 15
print(iterator.next())    # Ожидаемый результат: 20
print(iterator.has_next()) # False


class BSTIteratorOptimized:
    """
    Итератор для BST (метод с `stack` и `inorder` генерацией на лету).
    """
    def __init__(self, root: TreeNode):
        self.stack: list[TreeNode] = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node: TreeNode | None) -> None:
        """
        Добавляет в `stack` все левые узлы от `node`.
        """
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        Возвращает следующий минимальный элемент в BST.
        """
        node: TreeNode = self.stack.pop()
        if node.right:
            self._leftmost_inorder(node.right)
        return node.val

    def has_next(self) -> bool:
        """
        Проверяет, есть ли следующий элемент.
        """
        return len(self.stack) > 0


# 🔹 Тестируем (оптимизированный метод с `stack`)
iterator_optimized = BSTIteratorOptimized(tree)

print(iterator_optimized.next())    # Ожидаемый результат: 3
print(iterator_optimized.next())    # Ожидаемый результат: 7
print(iterator_optimized.has_next()) # True
print(iterator_optimized.next())    # Ожидаемый результат: 9
print(iterator_optimized.has_next()) # True
print(iterator_optimized.next())    # Ожидаемый результат: 15
print(iterator_optimized.next())    # Ожидаемый результат: 20
print(iterator_optimized.has_next()) # False


"""
Анализ сложности:
1. **Метод с предварительным `inorder` обходом:**
   - Временная сложность:
     - O(n) для предварительного обхода.
     - O(1) для `next()`.
   - Пространственная сложность: O(n) (храним все элементы).

2. **Метод с `stack` (генерация на лету):**
   - Временная сложность:
     - O(H) для `next()` в худшем случае (H - высота дерева).
     - O(1) в среднем.
   - Пространственная сложность: O(H) (глубина стека).

🔹 **Метод со стеком эффективнее** по памяти (O(H) вместо O(n)).
"""
