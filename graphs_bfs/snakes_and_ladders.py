from collections import deque

def snakes_and_ladders(board: list[list[int]]) -> int:
    """
    Находит минимальное количество ходов для достижения последней клетки в игре "Змеи и лестницы".

    🔹 **Алгоритм (BFS, O(n^2))**:
    1️⃣ Разворачиваем `board` в 1D массив `cells`, учитывая направление змейки.
    2️⃣ Запускаем BFS:
       - В `queue` храним `(позиция, шаги)`, начиная с `1`.
       - Бросаем кубик (1-6) и переходим на `next_pos`.
       - Если клетка содержит змею/лестницу, перемещаемся.
       - Если достигли `n*n`, возвращаем `шаги + 1`.
    3️⃣ Если не нашли путь, возвращаем `-1`.

    🔹 **Временная сложность**:
       - `O(n^2)`, так как BFS проходит все клетки `n^2` максимум один раз.

    🔹 **Пространственная сложность**:
       - `O(n^2)`, из-за хранения `cells` и `queue`.

    :param board: list[list[int]] - Игровая доска `n x n`.
    :return: int - Минимальное количество ходов или `-1`, если путь невозможен.
    """
    n = len(board)

    # 1. Разворачиваем board в 1D массив (Boustrophedon)
    cells = [-1] * (n * n + 1)
    idx = 1
    for r in range(n - 1, -1, -1):  # Двигаемся снизу вверх
        row = range(n) if (n - 1 - r) % 2 == 0 else range(n - 1, -1, -1)
        for c in row:
            cells[idx] = board[r][c]
            idx += 1

    # 2. BFS (поиск минимального пути)
    queue = deque([(1, 0)])  # (позиция, шаги)
    visited = set()

    while queue:
        pos, steps = queue.popleft()

        for dice in range(1, 7):  # Бросаем кубик (1-6)
            next_pos = pos + dice
            if next_pos > n * n:
                continue  # Выход за пределы доски

            if cells[next_pos] != -1:
                next_pos = cells[next_pos]  # Лестница или змея

            if next_pos == n * n:
                return steps + 1  # Достигли конца

            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, steps + 1))

    return -1  # Если не смогли добраться


# 🔹 Тест
board1 = [
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,35,-1,-1,13,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,15,-1,-1,-1,-1]
]

print(snakes_and_ladders(board1))  # ✅ 4
