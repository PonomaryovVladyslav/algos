class TreeNode:
    """
    Класс узла бинарного дерева.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Находит наименьшего общего предка (LCA) двух узлов `p` и `q` в бинарном дереве.

    Алгоритм:
    1. Если `root` равен `None`, `p` или `q` — возвращаем `root` (база рекурсии).
    2. Рекурсивно ищем `p` и `q` в левом и правом поддереве.
    3. Если `p` и `q` находятся в разных поддеревьях, то `root` — LCA.
    4. Если `p` и `q` находятся только в одном поддереве, LCA — в этом поддереве.

    Входные данные:
    - root: Корень бинарного дерева.
    - p, q: Узлы, для которых ищем общего предка.

    Выход:
    - Узел `TreeNode`, являющийся LCA.

    Время: O(N), где N — количество узлов (полный обход дерева в худшем случае).
    Пространство: O(H), где H — высота дерева (глубина рекурсии в худшем случае).
    """

    if not root or root == p or root == q:
        return root  # База рекурсии

    left = lowest_common_ancestor(root.left, p, q)  # Ищем в левом поддереве
    right = lowest_common_ancestor(root.right, p, q)  # Ищем в правом поддереве

    if left and right:
        return root  # Если `p` и `q` в разных поддеревьях, `root` — LCA

    return left if left else right  # LCA в одном из поддеревьев


# Тестовый пример:
#        3
#       / \
#      5   1
#     / \  / \
#    6   2 0  8
#       / \
#      7   4
tree = TreeNode(3,
    TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
    TreeNode(1, TreeNode(0), TreeNode(8))
)

# Тест 1: LCA(5, 1) = 3
p = tree.left  # Узел 5
q = tree.right  # Узел 1
print(lowest_common_ancestor(tree, p, q).val)  # 3

# Тест 2: LCA(5, 4) = 5
p = tree.left  # Узел 5
q = tree.left.right.right  # Узел 4
print(lowest_common_ancestor(tree, p, q).val)  # 5
