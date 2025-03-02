def game_of_life(board: list[list[int]]) -> None:
    """
    Обновляет поле "Игра Жизнь" согласно правилам:
    1. Живая клетка (1) с <2 или >3 живыми соседями умирает.
    2. Живая клетка (1) с 2 или 3 соседями продолжает жить.
    3. Мёртвая клетка (0) с ровно 3 соседями оживает.

    🔹 Используется in-place обновление:
       - `-1` → живая клетка, которая умирает.
       - `2` → мёртвая клетка, которая оживает.

    🔹 **Сложность**:
       - `O(m * n)`, где `m × n` — размер доски.
       - `O(1)` доп. памяти (обновление в месте).
    """
    if not board or not board[0]:
        return

    m, n = len(board), len(board[0])

    def count_live_neighbors(r, c):
        """ Подсчёт живых соседей (учитывает -1 как живую). """
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        return sum(
            1 for dr, dc in directions if 0 <= r + dr < m and 0 <= c + dc < n and abs(board[r + dr][c + dc]) == 1)

    # 1. Обновляем состояния ячеек
    for i in range(m):
        for j in range(n):
            live_neighbors = count_live_neighbors(i, j)

            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[i][j] = -1  # Живая клетка умирает

            if board[i][j] == 0 and live_neighbors == 3:
                board[i][j] = 2  # Мёртвая клетка оживает

    # 2. Заменяем временные состояния
    for i in range(m):
        for j in range(n):
            if board[i][j] == -1:
                board[i][j] = 0
            elif board[i][j] == 2:
                board[i][j] = 1


# 🔹 Тест
board1 = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]

game_of_life(board1)

# 🔹 Ожидаемый результат:
# [[0, 0, 0],
#  [1, 0, 1],
#  [0, 1, 1],
#  [0, 1, 0]]

for row in board1:
    print(row)
