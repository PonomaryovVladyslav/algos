# Задача: Построить бинарное дерево по `preorder` (NLR) и `inorder` (LNR) обходам.
# Дано: два списка `preorder` и `inorder`, содержащие значения узлов.
# Нужно: восстановить бинарное дерево и вернуть его корень.

class TreeNode:
    """
    Класс узла бинарного дерева.
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """
    Функция строит бинарное дерево по `preorder` и `inorder` обходам.

    🔹 Временная сложность: O(n), так как мы проходим каждый узел ровно один раз.
    🔹 Пространственная сложность: O(n), так как создаем хеш-таблицу `inorder_index` и используем стек рекурсии.

    :param preorder: list[int] - список значений узлов в порядке `preorder` обхода.
    :param inorder: list[int] - список значений узлов в порядке `inorder` обхода.
    :return: TreeNode | None - корень восстановленного дерева.
    """

    if not preorder or not inorder:
        return None

    inorder_index: dict[int, int] = {val: idx for idx, val in enumerate(inorder)}  # O(n) хеш-таблица
    pre_idx: int = 0  # Глобальный индекс в `preorder`

    def helper(left: int, right: int) -> TreeNode | None:
        """
        Вспомогательная рекурсивная функция для построения поддерева.

        :param left: int - начальный индекс в `inorder`.
        :param right: int - конечный индекс в `inorder`.
        :return: TreeNode | None - корень текущего поддерева.
        """
        nonlocal pre_idx
        if left > right:
            return None

        root_val: int = preorder[pre_idx]  # Берём корень из `preorder`
        root: TreeNode = TreeNode(root_val)
        pre_idx += 1  # Двигаем индекс

        mid: int = inorder_index[root_val]  # Находим индекс в `inorder`
        root.left = helper(left, mid - 1)  # Рекурсия для левого поддерева
        root.right = helper(mid + 1, right)  # Рекурсия для правого поддерева

        return root

    return helper(0, len(inorder) - 1)


# 🔹 Тестируем
preorder: list[int] = [3, 9, 20, 15, 7]
inorder: list[int] = [9, 3, 15, 20, 7]

root: TreeNode = build_tree(preorder, inorder)


"""
🔹 Анализ сложности:

✅ Временная сложность: **O(n)**
- Мы проходим по каждому узлу **ровно один раз**.
- Используем **O(1) поиск индекса** через `dict`, что заменяет O(n) вызовы `list.index()`.

✅ Пространственная сложность: **O(n)**
- Используем хеш-таблицу `inorder_index` размером **O(n)**.
- Вызовы рекурсии требуют **O(H) памяти**, где `H` — высота дерева.
  - В сбалансированном дереве `H = log n`, в несбалансированном `H = n`.

📌 **Как работает алгоритм?**
1️⃣ **Берем корень из `preorder`** и находим его **индекс в `inorder`**.  
2️⃣ **Рекурсивно строим левое поддерево** (`inorder[:mid]`).  
3️⃣ **Рекурсивно строим правое поддерево** (`inorder[mid+1:]`).  
4️⃣ **Используем `dict` для быстрого поиска индексов** (O(1) вместо O(n)).  

💡 **Почему сначала строим левое поддерево?**
- В `preorder` **левое поддерево всегда перед правым**, поэтому `pre_idx` двигается **по порядку**.

"""
