from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        """
        Класс для представления узла в неориентированном графе.

        :param val: int - значение узла.
        :param neighbors: list[Node] - список соседних узлов.
        """
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node) -> Node:
    """
    Функция клонирует неориентированный граф **с помощью BFS**.

    🔹 Алгоритм (поиск в ширину O(n + e)):
    1️⃣ Используем **hash-map (`visited`)**, где:
       - `ключ` — оригинальный узел,
       - `значение` — клонированный узел.
    2️⃣ Начинаем с `node`, создаем его копию и добавляем в `visited`.
    3️⃣ Используем **очередь (`queue`)** для обхода графа.
    4️⃣ Для каждого узла:
       - **Копируем соседей** и добавляем в `visited` (если их еще нет).
       - **Связываем соседей** с клонированным узлом.
    5️⃣ Итог: возвращаем `visited[node]` (корневой узел клона).

    🔹 Временная сложность: **O(n + e)** (узлы + рёбра).
    🔹 Пространственная сложность: **O(n)** (для `visited` и `queue`).

    :param node: Node - начальный узел графа.
    :return: Node - корневой узел клонированного графа.
    """

    if not node:
        return None

    # Хэш-таблица для хранения соответствия старых и новых узлов
    visited = {}

    # Создаём копию начального узла
    queue = deque([node])
    visited[node] = Node(node.val)

    while queue:
        old_node = queue.popleft()

        # Клонируем соседей
        for neighbor in old_node.neighbors:
            if neighbor not in visited:
                visited[neighbor] = Node(neighbor.val)
                queue.append(neighbor)  # Добавляем новый узел в очередь
            visited[old_node].neighbors.append(visited[neighbor])  # Добавляем клон соседа

    return visited[node]  # Возвращаем клон исходного узла


# 🔹 Создание графа 1 -- 2
#                      |    |
#                      4 -- 3
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

cloned = clone_graph(node1)
print(cloned.val)  # ✅ 1
print([n.val for n in cloned.neighbors])  # ✅ [2, 4]


def clone_graph_dfs(node: Node) -> Node:
    """
    Функция клонирует неориентированный граф **с помощью DFS**.

    🔹 Алгоритм (поиск в глубину O(n + e)):
    1️⃣ Используем **hash-map (`visited`)** для хранения копий узлов.
    2️⃣ Запускаем **рекурсивный `dfs(old_node)`**, который:
       - Создаёт копию `old_node`,
       - Рекурсивно копирует его соседей,
       - Добавляет соседей в `neighbors` клона.
    3️⃣ Итог: `visited[node]` содержит копию графа.

    🔹 Временная сложность: **O(n + e)** (узлы + рёбра).
    🔹 Пространственная сложность: **O(n)** (для `visited` + стек вызовов).

    :param node: Node - начальный узел графа.
    :return: Node - корневой узел клонированного графа.
    """

    if not node:
        return None

    visited = {}

    def dfs(old_node):
        if old_node in visited:
            return visited[old_node]

        # Клонируем узел
        cloned_node = Node(old_node.val)
        visited[old_node] = cloned_node

        # Рекурсивно копируем соседей
        for neighbor in old_node.neighbors:
            cloned_node.neighbors.append(dfs(neighbor))

        return cloned_node

    return dfs(node)


cloned_dfs = clone_graph_dfs(node1)
print(cloned_dfs.val)  # ✅ 1
print([n.val for n in cloned_dfs.neighbors])  # ✅ [2, 4]
