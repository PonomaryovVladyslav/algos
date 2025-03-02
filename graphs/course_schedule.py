from collections import deque, defaultdict


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """
    Проверяет, можно ли пройти все курсы без циклов (BFS, алгоритм Kahn).

    🔹 Алгоритм (Топологическая сортировка O(n + e)):
    1️⃣ **Строим граф зависимостей** (adjacency list) и **считаем входящие рёбра**.
    2️⃣ **Запускаем BFS**:
       - Начинаем с курсов **без пред-реквизитов** (`in_degree == 0`).
       - Убираем курс, уменьшаем зависимости у соседей.
       - Если у соседа `in_degree == 0`, добавляем в очередь.
    3️⃣ **Если прошли все курсы → True, иначе → False**.

    🔹 Временная сложность: **O(n + e)** (узлы + рёбра).
    🔹 Пространственная сложность: **O(n + e)** (граф + очередь).

    :param num_courses: int - количество курсов.
    :param prerequisites: list[list[int]] - зависимости между курсами (a → b).
    :return: bool - можно ли пройти все курсы.
    """

    # 1️⃣ Строим граф зависимостей
    graph = defaultdict(list)
    in_degree = [0] * num_courses  # Количество входящих рёбер

    for course, prereq in prerequisites:
        graph[prereq].append(course)  # prereq → course
        in_degree[course] += 1

    # 2️⃣ Запускаем BFS (Kahn's Algorithm)
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    count = 0

    while queue:
        course = queue.popleft()
        count += 1  # Обработали курс

        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:  # Добавляем курс без зависимостей
                queue.append(neighbor)

    return count == num_courses  # Если прошли все курсы → True, иначе → False


# 🔹 Тестируем BFS (Kahn's Algorithm)
print(can_finish(2, [[1, 0]]))  # ✅ True
print(can_finish(2, [[1, 0], [0, 1]]))  # ✅ False


def can_finish_dfs(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """
    Проверяет, можно ли пройти все курсы без циклов (DFS).

    🔹 Алгоритм (DFS, поиск цикла O(n + e)):
    1️⃣ **Строим граф зависимостей** (adjacency list).
    2️⃣ Используем **DFS** с `visited`:
       - `0` - не посещен,
       - `1` - в обработке,
       - `2` - обработан.
    3️⃣ **Если нашли цикл (`visited == 1`) → False**.
    4️⃣ Если прошли все узлы → **True**.

    🔹 Временная сложность: **O(n + e)** (узлы + рёбра).
    🔹 Пространственная сложность: **O(n + e)** (граф + стек вызовов).

    :param num_courses: int - количество курсов.
    :param prerequisites: list[list[int]] - зависимости между курсами.
    :return: bool - можно ли пройти все курсы.
    """

    # 1️⃣ Строим граф
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # 2️⃣ DFS для поиска цикла
    visited = [0] * num_courses  # 0 - не посещен, 1 - в обработке, 2 - обработан

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
        return True

    # 3️⃣ Проверяем все курсы
    for course in range(num_courses):
        if visited[course] == 0:
            if not dfs(course):
                return False

    return True


# 🔹 Тестируем DFS
print(can_finish_dfs(2, [[1, 0]]))  # ✅ True
print(can_finish_dfs(2, [[1, 0], [0, 1]]))  # ✅ False
