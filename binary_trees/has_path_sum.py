from collections import deque

# Задача: Проверить, существует ли путь от корня до листа с суммой `targetSum`.
# Дано: бинарное дерево с корнем `root` и целевая сумма `targetSum`.
# Нужно: вернуть `True`, если существует путь от корня к листу, сумма значений которого равна `targetSum`.

class TreeNode:
    """
    Класс узла бинарного дерева.
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: TreeNode, target_sum: int) -> bool:
    """
    Функция проверяет, существует ли путь от корня до листа с суммой `target_sum` (DFS, рекурсия).

    :param root: TreeNode - корень бинарного дерева.
    :param target_sum: int - целевая сумма пути.
    :return: bool - `True`, если путь существует, иначе `False`.
    """

    if not root:
        return False

    # Если это листовой узел и сумма совпадает
    if not root.left and not root.right:
        return root.val == target_sum

    # Рекурсивно проверяем левое и правое поддерево
    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(root.right, target_sum - root.val)


# 🔹 Создаём тестовое дерево:
#     5
#    / \
#   4   8
#  /   / \
# 11  13  4
# /  \      \
#7    2      1
tree = TreeNode(5,
    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
    TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
)

print(has_path_sum(tree, 22))  # Ожидаемый результат: True (путь 5->4->11->2)
print(has_path_sum(tree, 26))  # Ожидаемый результат: True (путь 5->8->13)
print(has_path_sum(tree, 27))  # Ожидаемый результат: False


def has_path_sum_bfs(root: TreeNode, target_sum: int) -> bool:
    """
    Функция проверяет, существует ли путь от корня до листа с суммой `target_sum` (BFS, очередь).

    :param root: TreeNode - корень бинарного дерева.
    :param target_sum: int - целевая сумма пути.
    :return: bool - `True`, если путь существует, иначе `False`.
    """

    if not root:
        return False

    queue: deque[tuple[TreeNode, int]] = deque([(root, target_sum)])

    while queue:
        node, curr_sum = queue.popleft()

        # Если дошли до листа и сумма совпадает
        if not node.left and not node.right and node.val == curr_sum:
            return True

        if node.left:
            queue.append((node.left, curr_sum - node.val))
        if node.right:
            queue.append((node.right, curr_sum - node.val))

    return False


# 🔹 Тестируем BFS-метод
print(has_path_sum_bfs(tree, 22))  # Ожидаемый результат: True
print(has_path_sum_bfs(tree, 26))  # Ожидаемый результат: True
print(has_path_sum_bfs(tree, 27))  # Ожидаемый результат: False

"""
Анализ сложности:
1. **DFS (рекурсия):**
   - Временная сложность: O(n), так как мы посещаем каждый узел один раз.
   - Пространственная сложность: O(H), где `H` - высота дерева (глубина рекурсии).

2. **BFS (очередь):**
   - Временная сложность: O(n), так как мы обходим каждый узел ровно один раз.
   - Пространственная сложность: O(m), где `m` — максимальное количество узлов на одном уровне (ширина дерева).

🔹 **DFS проще и рекурсивен**, а **BFS более естественен для итеративного решения**.
"""
