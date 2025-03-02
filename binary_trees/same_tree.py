from collections import deque


# Задача: Проверить, являются ли два бинарных дерева идентичными.
# Дано: два корня `p` и `q` бинарных деревьев.
# Нужно: вернуть `True`, если они идентичны по структуре и значениям узлов.

class TreeNode:
    """
    Класс узла бинарного дерева.
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """
    Функция проверяет, являются ли два бинарных дерева идентичными (DFS, рекурсия).

    🔹 Временная сложность: O(n), так как мы посещаем каждый узел ровно один раз.
    🔹 Пространственная сложность: O(H), где `H` — глубина дерева (глубина рекурсии).

    :param p: TreeNode - корень первого дерева.
    :param q: TreeNode - корень второго дерева.
    :return: bool - `True`, если деревья идентичны, иначе `False`.
    """

    if not p and not q:
        return True  # Оба дерева пустые
    if not p or not q or p.val != q.val:
        return False  # Либо структура разная, либо значения не совпадают

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def is_same_tree_bfs(p: TreeNode, q: TreeNode) -> bool:
    """
    Функция проверяет, являются ли два бинарных дерева идентичными (BFS, очередь).

    🔹 Временная сложность: O(n), так как мы посещаем каждый узел ровно один раз.
    🔹 Пространственная сложность: O(n), так как в худшем случае `queue` хранит все узлы уровня.

    :param p: TreeNode - корень первого дерева.
    :param q: TreeNode - корень второго дерева.
    :return: bool - `True`, если деревья идентичны, иначе `False`.
    """

    queue: deque[tuple[TreeNode | None, TreeNode | None]] = deque([(p, q)])

    while queue:
        node_p, node_q = queue.popleft()

        if not node_p and not node_q:
            continue  # Оба пустые — пропускаем
        if not node_p or not node_q or node_p.val != node_q.val:
            return False  # Либо структура разная, либо значения не совпадают

        queue.append((node_p.left, node_q.left))
        queue.append((node_p.right, node_q.right))

    return True


# 🔹 Тестируем
tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
tree3 = TreeNode(1, TreeNode(2))
tree4 = TreeNode(1, None, TreeNode(2))

print(is_same_tree(tree1, tree2))  # Ожидаемый результат: True
print(is_same_tree(tree1, tree3))  # Ожидаемый результат: False
print(is_same_tree(tree3, tree4))  # Ожидаемый результат: False

print(is_same_tree_bfs(tree1, tree2))  # Ожидаемый результат: True
print(is_same_tree_bfs(tree1, tree3))  # Ожидаемый результат: False
print(is_same_tree_bfs(tree3, tree4))  # Ожидаемый результат: False


"""
🔹 Сравнение методов:

1️⃣ `is_same_tree()` (DFS, рекурсия)
   - Временная сложность: O(n) — посещаем каждый узел ровно один раз.
   - Пространственная сложность: O(H) — глубина рекурсии (H = log n в сбалансированном дереве, H = n в худшем случае).

2️⃣ `is_same_tree_bfs()` (BFS, очередь)
   - Временная сложность: O(n) — посещаем каждый узел ровно один раз.
   - Пространственная сложность: O(n) — в худшем случае `queue` хранит все узлы уровня.

✅ Вывод:
   - **DFS проще и использует O(H) памяти** (лучше для глубоких деревьев).
   - **BFS использует O(n) памяти** (лучше для широких деревьев, так как избегает глубокой рекурсии).
"""
