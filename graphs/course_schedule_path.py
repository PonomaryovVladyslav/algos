from collections import deque, defaultdict


def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """
    Возвращает возможный порядок прохождения курсов без циклов (BFS, алгоритм Kahn).

    🔹 Алгоритм (Топологическая сортировка O(n + e)):
    1️⃣ **Строим граф зависимостей** (adjacency list) и **считаем входящие рёбра**.
    2️⃣ **Запускаем BFS**:
       - Начинаем с курсов **без пред-реквизитов** (`in_degree == 0`).
       - Убираем курс, уменьшаем зависимости у соседей.
       - Если у соседа `in_degree == 0`, добавляем в очередь.
    3️⃣ **Если прошли все курсы → список, иначе → []** (если цикл).

    🔹 Временная сложность: **O(n + e)** (узлы + рёбра).
    🔹 Пространственная сложность: **O(n + e)** (граф + очередь).

    :param num_courses: int - количество курсов.
    :param prerequisites: list[list[int]] - зависимости между курсами (a → b).
    :return: list[int] - порядок прохождения курсов или [] (если цикл).
    """

    # 1️⃣ Строим граф зависимостей
    graph = defaultdict(list)
    in_degree = [0] * num_courses  # Количество входящих рёбер

    for course, prereq in prerequisites:
        graph[prereq].append(course)  # prereq → course
        in_degree[course] += 1

    # 2️⃣ Запускаем BFS (Kahn's Algorithm)
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)  # Добавляем курс в порядок

        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:  # Добавляем курс без зависимостей
                queue.append(neighbor)

    return order if len(order) == num_courses else []  # Если цикл → []


# 🔹 Тестируем BFS (Kahn's Algorithm)
print(find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # ✅ [0, 1, 2, 3] или [0, 2, 1, 3]
print(find_order(2, [[1, 0], [0, 1]]))  # ✅ [] (Цикл)


def find_order_dfs(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """
    Возвращает возможный порядок прохождения курсов без циклов (DFS).

    🔹 Алгоритм (DFS, топологическая сортировка O(n + e)):
    1️⃣ **Строим граф зависимостей** (adjacency list).
    2️⃣ **DFS для топологической сортировки**:
       - Используем `visited`: `0` - не посещен, `1` - в обработке, `2` - обработан.
       - Если нашли цикл (`visited == 1`) → возвращаем `[]`.
       - Добавляем узел в `order` (по завершении DFS).
    3️⃣ **Разворачиваем стек → получаем порядок прохождения**.

    🔹 Временная сложность: **O(n + e)** (узлы + рёбра).
    🔹 Пространственная сложность: **O(n + e)** (граф + стек вызовов).

    :param num_courses: int - количество курсов.
    :param prerequisites: list[list[int]] - зависимости между курсами.
    :return: list[int] - порядок прохождения курсов или [] (если цикл).
    """

    # 1️⃣ Строим граф
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # 2️⃣ DFS для топологической сортировки
    visited = [0] * num_courses  # 0 - не посещен, 1 - в обработке, 2 - обработан
    order = []

    def dfs(course):
        if visited[course] == 1:  # 🔴 Цикл найден
            return False
        if visited[course] == 2:  # ✅ Уже обработан
            return True

        visited[course] = 1  # В процессе обработки
        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False

        visited[course] = 2  # Отмечаем как обработанный
        order.append(course)  # Добавляем в порядок
        return True

    # 3️⃣ Проверяем все курсы
    for course in range(num_courses):
        if visited[course] == 0:
            if not dfs(course):
                return []

    return order[::-1]  # Разворачиваем стек


# 🔹 Тестируем DFS
print(find_order_dfs(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # ✅ [0, 1, 2, 3] или [0, 2, 1, 3]
print(find_order_dfs(2, [[1, 0], [0, 1]]))  # ✅ [] (Цикл)
