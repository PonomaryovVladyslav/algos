from collections import defaultdict, deque


def calc_equation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    """
    Решает задачу о вычислении дробей через граф и DFS.

    🔹 **Алгоритм (Граф + DFS, O(n + q))**:
    1️⃣ **Построение взвешенного графа** (словарь словарей `{a: {b: value}}`).
    2️⃣ **DFS для поиска пути от `start` к `end`**:
       - Если `start == end` → `1.0`.
       - Рекурсивно переходим к соседям, умножая коэффициенты.
       - Если не нашли путь → `-1.0`.
    3️⃣ **Обрабатываем запросы (`queries`) и возвращаем результаты**.

    🔹 **Временная сложность**:
       - **Построение графа:** `O(n)`, где `n` — число уравнений.
       - **Поиск (DFS):** `O(q * n)`, где `q` — число запросов (в худшем случае перебираем все рёбра).
       - **Итого:** `O(n + q * n)`, но обычно гораздо быстрее (`O(n + q)`).

    🔹 **Пространственная сложность**:
       - **Граф:** `O(n)`.
       - **Рекурсивный стек DFS:** `O(n)`.
       - **Итого:** `O(n)`.

    :param equations: list[list[str]] - пары отношений, например, [["a", "b"], ["b", "c"]].
    :param values: list[float] - коэффициенты отношений, например, [2.0, 3.0].
    :param queries: list[list[str]] - запросы, например, [["a", "c"], ["b", "a"]].
    :return: list[float] - результаты запросов, например, [6.0, 0.5].
    """

    # 1️⃣ Построение графа
    graph = defaultdict(dict)

    for (a, b), value in zip(equations, values):
        graph[a][b] = value
        graph[b][a] = 1 / value  # Обратное отношение

    # 2️⃣ DFS для поиска пути
    def dfs(start, end, visited):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0
        visited.add(start)

        for neighbor, weight in graph[start].items():
            if neighbor not in visited:
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return result * weight  # Умножаем коэффициенты на пути

        return -1.0

    # 3️⃣ Обрабатываем все запросы
    return [dfs(c, d, set()) for c, d in queries]


# 🔹 Тестируем DFS
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

print(calc_equation(equations, values, queries))  # ✅ [6.0, 0.5, -1.0, 1.0, -1.0]


def calc_equation_bfs(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    """
    Решает задачу о вычислении дробей через граф и BFS.

    🔹 **Алгоритм (Граф + BFS, O(n + q))**:
    1️⃣ **Построение графа**.
    2️⃣ **BFS для поиска пути от `start` к `end`**:
       - Используем очередь `deque([(node, product)])`, где `product` — накопленный коэффициент.
       - Если нашли `end` → возвращаем `product`.
       - Если не нашли → `-1.0`.
    3️⃣ **Обрабатываем запросы (`queries`) и возвращаем результаты**.

    🔹 **Временная сложность**:
       - **Построение графа:** `O(n)`.
       - **Поиск (BFS):** `O(q * n)`, где `q` — число запросов.
       - **Итого:** `O(n + q * n)`, но обычно гораздо быстрее (`O(n + q)`).

    🔹 **Пространственная сложность**:
       - **Граф:** `O(n)`.
       - **Очередь BFS:** `O(n)`.
       - **Итого:** `O(n)`.

    :param equations: list[list[str]] - пары отношений.
    :param values: list[float] - коэффициенты отношений.
    :param queries: list[list[str]] - запросы.
    :return: list[float] - результаты запросов.
    """

    # 1️⃣ Построение графа
    graph = defaultdict(dict)

    for (a, b), value in zip(equations, values):
        graph[a][b] = value
        graph[b][a] = 1 / value

    # 2️⃣ BFS для поиска пути
    def bfs(start, end):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0

        queue = deque([(start, 1.0)])  # (узел, накопленный коэффициент)
        visited = set()

        while queue:
            node, product = queue.popleft()
            if node == end:
                return product  # Нашли путь

            visited.add(node)

            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    queue.append((neighbor, product * weight))

        return -1.0  # Не нашли путь

    # 3️⃣ Обрабатываем все запросы
    return [bfs(c, d) for c, d in queries]


# 🔹 Тестируем BFS
print(calc_equation_bfs(equations, values, queries))  # ✅ [6.0, 0.5, -1.0, 1.0, -1.0]
