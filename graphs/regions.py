from collections import deque


def solve(board: list[list[str]]) -> None:
    """
    Захватывает окружённые 'O', заменяя их на 'X' с помощью BFS.

    🔹 **Алгоритм (BFS, O(m * n))**:
    1️⃣ Помечаем все 'O' на границах временным символом 'T'.
    2️⃣ Обрабатываем их BFS, распространяя 'T' на соседние 'O'.
    3️⃣ Обходим всю доску, заменяя:
       - Оставшиеся 'O' на 'X' (захват),
       - 'T' обратно в 'O' (не окружённые).

    🔹 **Временная сложность**:
       - `O(m * n)`, так как каждая клетка посещается один раз.

    🔹 **Пространственная сложность**:
       - `O(min(m, n))`, так как в очереди хранятся границы.

    :param board: list[list[str]] - Игровая доска.
    :return: None (модифицирует board на месте)
    """
    if not board:
        return

    rows, cols = len(board), len(board[0])
    queue = deque()

    # 1. Находим все "O" на границах и заменяем на временный символ "T"
    for r in range(rows):
        for c in [0, cols - 1]:  # Левая и правая границы
            if board[r][c] == "O":
                queue.append((r, c))

    for c in range(cols):
        for r in [0, rows - 1]:  # Верхняя и нижняя границы
            if board[r][c] == "O":
                queue.append((r, c))

    # BFS - помечаем все связанные с границей "O" как "T"
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        r, c = queue.popleft()
        if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
            board[r][c] = "T"  # Временно помечаем как не окружённое "O"
            for dr, dc in directions:
                queue.append((r + dr, c + dc))

    # 2. Обновляем board
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":  # Захватываем окруженные регионы
                board[r][c] = "X"
            elif board[r][c] == "T":  # Возвращаем "O", которые не окружены
                board[r][c] = "O"


# 🔹 Тест
board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]

solve(board)
for row in board:
    print(row)


def solve_dfs(board: list[list[str]]) -> None:
    """
    Захватывает окружённые 'O', заменяя их на 'X' с помощью DFS.

    🔹 **Алгоритм (DFS, O(m * n))**:
    1️⃣ Помечаем все 'O' на границах временным символом 'T'.
    2️⃣ Обрабатываем их DFS, распространяя 'T' на соседние 'O'.
    3️⃣ Обходим всю доску, заменяя:
       - Оставшиеся 'O' на 'X' (захват),
       - 'T' обратно в 'O' (не окружённые).

    🔹 **Временная сложность**:
       - `O(m * n)`, так как каждая клетка посещается один раз.

    🔹 **Пространственная сложность**:
       - `O(m * n)` в худшем случае (глубина рекурсии).

    :param board: list[list[str]] - Игровая доска.
    :return: None (модифицирует board на месте)
    """
    if not board:
        return

    rows, cols = len(board), len(board[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
            return
        board[r][c] = "T"  # Временно помечаем
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # 1. Ищем все "O" на границах и запускаем DFS
    for r in range(rows):
        for c in [0, cols - 1]:  # Левая и правая границы
            if board[r][c] == "O":
                dfs(r, c)

    for c in range(cols):
        for r in [0, rows - 1]:  # Верхняя и нижняя границы
            if board[r][c] == "O":
                dfs(r, c)

    # 2. Обновляем board
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "T":
                board[r][c] = "O"
