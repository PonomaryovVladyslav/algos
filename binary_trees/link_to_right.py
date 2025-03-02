from collections import deque

# Задача: Связать соседние узлы на одном уровне в бинарном дереве.
# Дано: бинарное дерево, где каждый узел имеет `next` (указывает на соседа справа).
# Нужно: заполнить `next` для всех узлов (использовать O(1) доп. памяти).

class Node:
    """
    Класс узла бинарного дерева с указателем `next`.
    """
    def __init__(self, val: int = 0, left: "Node" = None, right: "Node" = None, next: "Node" = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: Node) -> Node:
    """
    Функция связывает все узлы одного уровня через `next` (BFS, очередь).

    🔹 Временная сложность: O(n), так как мы посещаем каждый узел ровно один раз.
    🔹 Пространственная сложность: O(n), так как в худшем случае (широкое дерево) очередь хранит все узлы на уровне.

    :param root: Node - корень бинарного дерева.
    :return: Node - корень дерева с обновленными `next`.
    """

    if not root:
        return None

    queue: deque[Node] = deque([root])

    while queue:
        prev: Node | None = None
        for _ in range(len(queue)):  # Обрабатываем узлы уровня
            node: Node = queue.popleft()

            if prev:
                prev.next = node  # Связываем соседние узлы
            prev = node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        node.next = None  # Последний элемент указывает на NULL

    return root


# 🔹 Тестируем (метод BFS)
tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
connected_tree = connect(tree)


def connect_optimized(root: Node) -> Node:
    """
    Функция связывает все узлы одного уровня через `next` (O(1) памяти, без очереди).

    🔹 Временная сложность: O(n), так как мы обходим каждый узел ровно один раз.
    🔹 Пространственная сложность: O(1), так как используем только несколько дополнительных указателей.

    :param root: Node - корень бинарного дерева.
    :return: Node - корень дерева с обновленными `next`.
    """

    if not root:
        return None

    leftmost: Node | None = root  # Начинаем с корня

    while leftmost:  # Пока есть узлы на текущем уровне
        dummy: Node = Node(0)
        prev: Node = dummy
        current: Node | None = leftmost

        while current:  # Обход узлов уровня
            if current.left:
                prev.next = current.left
                prev = prev.next
            if current.right:
                prev.next = current.right
                prev = prev.next

            current = current.next  # Двигаемся по уровню

        leftmost = dummy.next  # Переходим на следующий уровень

    return root


"""
🔹 Сравнение двух методов:

1️⃣ `connect()` (BFS с очередью)
   - Временная сложность: O(n) — посещаем каждый узел один раз.
   - Пространственная сложность: O(n) — в худшем случае храним весь уровень в `queue`.

2️⃣ `connect_optimized()` (без доп. памяти)
   - Временная сложность: O(n) — посещаем каждый узел один раз.
   - Пространственная сложность: O(1) — используем только несколько переменных.

✅ Вывод:
   - `connect_optimized()` лучше для **больших деревьев**, так как использует **O(1) памяти**.
   - `connect()` проще в реализации и читабельнее.
"""
