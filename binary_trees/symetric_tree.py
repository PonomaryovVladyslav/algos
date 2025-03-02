from collections import deque


# Задача: Проверить, является ли бинарное дерево зеркально симметричным.
# Дано: корень `root` бинарного дерева.
# Нужно: вернуть `True`, если дерево симметрично, иначе `False`.

class TreeNode:
    """
    Класс узла бинарного дерева.
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: TreeNode) -> bool:
    """
    Функция проверяет, является ли бинарное дерево зеркально симметричным (DFS, рекурсия).

    🔹 Временная сложность: O(n), так как мы посещаем каждый узел ровно один раз.
    🔹 Пространственная сложность: O(H), где `H` — глубина дерева (глубина рекурсии).

    :param root: TreeNode - корень бинарного дерева.
    :return: bool - `True`, если дерево симметрично, иначе `False`.
    """

    if not root:
        return True

    def is_mirror(left: TreeNode | None, right: TreeNode | None) -> bool:
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    return is_mirror(root.left, root.right)


def is_symmetric_bfs(root: TreeNode) -> bool:
    """
    Функция проверяет, является ли бинарное дерево зеркально симметричным (BFS, очередь).

    🔹 Временная сложность: O(n), так как мы посещаем каждый узел ровно один раз.
    🔹 Пространственная сложность: O(n), так как в худшем случае `queue` хранит все узлы уровня.

    :param root: TreeNode - корень бинарного дерева.
    :return: bool - `True`, если дерево симметрично, иначе `False`.
    """

    if not root:
        return True

    queue: deque[tuple[TreeNode | None, TreeNode | None]] = deque([(root.left, root.right)])

    while queue:
        left, right = queue.popleft()

        if not left and not right:
            continue
        if not left or not right or left.val != right.val:
            return False

        queue.append((left.left, right.right))
        queue.append((left.right, right.left))

    return True


# 🔹 Тестируем
tree1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
tree2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))

print(is_symmetric(tree1))  # Ожидаемый результат: True
print(is_symmetric(tree2))  # Ожидаемый результат: False

print(is_symmetric_bfs(tree1))  # Ожидаемый результат: True
print(is_symmetric_bfs(tree2))  # Ожидаемый результат: False


"""
🔹 Сравнение методов:

1️⃣ `is_symmetric()` (DFS, рекурсия)
   - Временная сложность: O(n) — посещаем каждый узел ровно один раз.
   - Пространственная сложность: O(H) — глубина рекурсии (H = log n в сбалансированном дереве, H = n в худшем случае).

2️⃣ `is_symmetric_bfs()` (BFS, очередь)
   - Временная сложность: O(n) — посещаем каждый узел ровно один раз.
   - Пространственная сложность: O(n) — в худшем случае `queue` хранит все узлы уровня.

✅ Вывод:
   - **DFS проще и использует O(H) памяти** (лучше для глубоких деревьев).
   - **BFS использует O(n) памяти** (лучше для широких деревьев, избегает глубокой рекурсии).
"""
