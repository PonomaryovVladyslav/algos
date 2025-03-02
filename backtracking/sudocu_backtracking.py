# Задача: Решить головоломку Судоку.
# Дано: `board` — 9x9 доска Судоку, где '.' обозначает пустые ячейки.
# Нужно: заполнить доску так, чтобы соблюдались правила Судоку.

def solve_sudoku(board: list[list[str]]) -> None:
    """
    Функция решает Судоку на месте, изменяя переданную `board`.

    :param board: list[list[str]] - 9x9 доска Судоку.
    :return: None (изменяет `board` на месте).
    """

    def is_valid(row: int, col: int, num: int) -> bool:
        """
        Проверяет, можно ли поставить число `num` в ячейку `board[row][col]`.

        :param row: int - строка доски.
        :param col: int - колонка доски.
        :param num: int - число для проверки (от 1 до 9).
        :return: bool - True, если число можно поставить, иначе False.
        """

        num = str(num)

        # Проверка строки и столбца
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        # Проверка 3x3 сектора
        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False

        return True

    def backtrack() -> bool:
        """
        Рекурсивный алгоритм для поиска решения Судоку.

        :return: bool - True, если Судоку решено, иначе False.
        """

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":  # Пустая ячейка
                    for num in range(1, 10):  # Пробуем числа от 1 до 9
                        if is_valid(row, col, num):
                            board[row][col] = str(num)  # Заполняем ячейку

                            if backtrack():  # Рекурсия для следующей ячейки
                                return True  # Если решено, возвращаем True

                            board[row][col] = "."  # Откат (Backtracking)

                    return False  # Если ни одно число не подходит, возвращаем False

        return True  # Если прошли все ячейки, значит Судоку решено

    backtrack()


# 🔹 Пример Судоку
sudoku_board: list[list[str]] = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

solve_sudoku(sudoku_board)

# 🔹 Выводим решение
for row in sudoku_board:
    print(" ".join(row))

"""
Анализ сложности:
- Временная сложность: O(9^(n*n)), где `n = 9` (из-за рекурсивного перебора всех возможных значений).
- Пространственная сложность: O(1), так как изменения выполняются на месте без дополнительной памяти.
"""
