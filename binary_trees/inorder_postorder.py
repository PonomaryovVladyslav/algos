# Задача: Построить бинарное дерево по `inorder` (LNR) и `postorder` (LRN) обходам.
# Дано: два списка `inorder` и `postorder`, содержащие значения узлов.
# Нужно: восстановить бинарное дерево и вернуть его корень.

class TreeNode:
    """
    Класс узла бинарного дерева.
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(inorder: list[int], postorder: list[int]) -> TreeNode | None:
    """
    Функция строит бинарное дерево по `inorder` и `postorder` обходам.

    :param inorder: list[int] - список значений узлов в порядке `inorder` обхода.
    :param postorder: list[int] - список значений узлов в порядке `postorder` обхода.
    :return: TreeNode | None - корень восстановленного дерева.
    """

    if not inorder or not postorder:
        return None

    inorder_index: dict[int, int] = {val: idx for idx, val in enumerate(inorder)}  # O(n) хеш-таблица
    post_idx: int = len(postorder) - 1  # Глобальный индекс в `postorder`

    def helper(left: int, right: int) -> TreeNode | None:
        """
        Вспомогательная рекурсивная функция для построения поддерева.

        :param left: int - начальный индекс в `inorder`.
        :param right: int - конечный индекс в `inorder`.
        :return: TreeNode | None - корень текущего поддерева.
        """
        nonlocal post_idx
        if left > right:
            return None

        root_val: int = postorder[post_idx]  # Берём корень из `postorder`
        root: TreeNode = TreeNode(root_val)
        post_idx -= 1  # Двигаем индекс

        mid: int = inorder_index[root_val]  # Находим индекс в `inorder`
        root.right = helper(mid + 1, right)  # Сначала строим правое поддерево!
        root.left = helper(left, mid - 1)  # Затем левое поддерево

        return root

    return helper(0, len(inorder) - 1)


# 🔹 Тестируем
inorder: list[int] = [9, 3, 15, 20, 7]
postorder: list[int] = [9, 15, 7, 20, 3]

root: TreeNode = build_tree(inorder, postorder)

"""
Анализ сложности:
- Временная сложность: O(n), так как мы проходим каждый узел один раз и используем `O(1)` поиск индекса через хеш-таблицу.
- Пространственная сложность: O(n), так как создаем хеш-таблицу `inorder_index` и используем стек рекурсии.

🔹 Этот метод **намного эффективнее**, чем простое нахождение индексов через `list.index()`, так как `dict` позволяет делать это за O(1).
"""
