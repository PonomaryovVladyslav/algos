from collections import deque

# Задача: Найти сумму всех чисел, полученных из корня в лист.
# Дано: бинарное дерево `root`, где путь от корня до листа формирует число.
# Нужно: вернуть сумму всех таких чисел.

class TreeNode:
    """
    Класс узла бинарного дерева.
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def sum_numbers(root: TreeNode) -> int:
    """
    Функция вычисляет сумму всех чисел, полученных из корня в лист (DFS, рекурсия).

    🔹 Временная сложность: O(n), так как мы посещаем каждый узел ровно один раз.
    🔹 Пространственная сложность: O(H), где `H` — высота дерева (глубина рекурсии).

    :param root: TreeNode - корень бинарного дерева.
    :return: int - сумма всех чисел, полученных из корня в лист.
    """

    def dfs(node: TreeNode | None, current_sum: int) -> int:
        if not node:
            return 0

        current_sum = current_sum * 10 + node.val

        if not node.left and not node.right:  # Лист
            return current_sum

        return dfs(node.left, current_sum) + dfs(node.right, current_sum)

    return dfs(root, 0)


def sum_numbers_bfs(root: TreeNode) -> int:
    """
    Функция вычисляет сумму всех чисел, полученных из корня в лист (BFS, очередь).

    🔹 Временная сложность: O(n), так как мы посещаем каждый узел ровно один раз.
    🔹 Пространственная сложность: O(n), так как в худшем случае `queue` хранит все узлы уровня.

    :param root: TreeNode - корень бинарного дерева.
    :return: int - сумма всех чисел, полученных из корня в лист.
    """

    if not root:
        return 0

    queue: deque[tuple[TreeNode, int]] = deque([(root, 0)])
    total_sum: int = 0

    while queue:
        node, current_sum = queue.popleft()
        current_sum = current_sum * 10 + node.val

        if not node.left and not node.right:  # Лист
            total_sum += current_sum

        if node.left:
            queue.append((node.left, current_sum))
        if node.right:
            queue.append((node.right, current_sum))

    return total_sum


# 🔹 Тестируем
# Тест 1: 1 -> 2 (12), 1 -> 3 (13) → 12 + 13 = 25
tree = TreeNode(1, TreeNode(2), TreeNode(3))
print(sum_numbers(tree))  # Ожидаемый результат: 25
print(sum_numbers_bfs(tree))  # Ожидаемый результат: 25

# Тест 2: 4 -> 9 -> 5 (495), 4 -> 9 -> 1 (491), 4 -> 0 (40) → 495 + 491 + 40 = 1026
tree2 = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
print(sum_numbers(tree2))  # Ожидаемый результат: 1026
print(sum_numbers_bfs(tree2))  # Ожидаемый результат: 1026


"""
🔹 Сравнение методов:

1️⃣ `sum_numbers()` (DFS, рекурсия)
   - Временная сложность: O(n) — посещаем каждый узел ровно один раз.
   - Пространственная сложность: O(H) — глубина рекурсии (H = log n в сбалансированном дереве, H = n в худшем случае).

2️⃣ `sum_numbers_bfs()` (BFS, очередь)
   - Временная сложность: O(n) — посещаем каждый узел ровно один раз.
   - Пространственная сложность: O(n) — в худшем случае `queue` хранит все узлы уровня.

✅ Вывод:
   - **DFS проще и использует O(H) памяти** (лучше для глубоких деревьев).
   - **BFS использует O(n) памяти** (лучше для широких деревьев, избегает глубокой рекурсии).
"""
