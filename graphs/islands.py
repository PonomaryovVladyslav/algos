from collections import deque


def num_islands(grid: list[list[str]]) -> int:
    """
    Подсчитывает количество островов в `grid` с помощью DFS.

    🔹 **Алгоритм (DFS, O(m * n))**:
    1️⃣ Обход сетки, ищем `1` (новый остров).
    2️⃣ Запускаем DFS от найденной клетки, помечая весь остров `0`.
    3️⃣ Увеличиваем счётчик островов (`count`).

    🔹 **Временная сложность**:
       - `O(m * n)`, так как каждую клетку посещаем один раз.

    🔹 **Пространственная сложность**:
       - `O(m * n)` в худшем случае (весь grid — один остров).

    :param grid: list[list[str]] - Двоичная матрица (`1` - суша, `0` - вода).
    :return: int - Количество островов.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # Помечаем клетку как посещённую
        dfs(r + 1, c)  # Вниз
        dfs(r - 1, c)  # Вверх
        dfs(r, c + 1)  # Вправо
        dfs(r, c - 1)  # Влево

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':  # Нашли новый остров
                count += 1
                dfs(r, c)  # Помечаем весь остров

    return count


# 🔹 Тест
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(num_islands(grid))  # ✅ 3


def num_islands_bfs(grid: list[list[str]]) -> int:
    """
    Подсчитывает количество островов в `grid` с помощью BFS.

    🔹 **Алгоритм (BFS, O(m * n))**:
    1️⃣ Обход сетки, ищем `1` (новый остров).
    2️⃣ Запускаем BFS от найденной клетки, помечая весь остров `0`.
    3️⃣ Увеличиваем счётчик островов (`count`).

    🔹 **Временная сложность**:
       - `O(m * n)`, так как каждую клетку посещаем один раз.

    🔹 **Пространственная сложность**:
       - `O(min(m, n))` (глубина очереди BFS).

    :param grid: list[list[str]] - Двоичная матрица (`1` - суша, `0` - вода).
    :return: int - Количество островов.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Вниз, вверх, вправо, влево

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':  # Новый остров
                count += 1
                queue = deque([(r, c)])
                grid[r][c] = '0'  # Помечаем как посещённое

                while queue:
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                            queue.append((nx, ny))
                            grid[nx][ny] = '0'  # Помечаем как посещённое

    return count


# 🔹 Тест
print(num_islands_bfs([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))  # ✅ 3
