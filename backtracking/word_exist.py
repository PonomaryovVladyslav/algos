# Задача: Найти, существует ли слово `word` в двумерном массиве `board`.
# Дано: `board` - двумерный список символов и `word` - строка.
# Нужно: вернуть `True`, если слово можно составить из букв на доске,
# двигаясь по соседним клеткам (вверх, вниз, влево, вправо) без повторного использования одной клетки.

def exist(board: list[list[str]], word: str) -> bool:
    """
    Функция проверяет, можно ли найти слово `word` в `board` путем перемещения
    по соседним клеткам (вверх, вниз, влево, вправо) без повторного использования ячеек.

    :param board: list[list[str]] - двумерный список букв.
    :param word: str - слово, которое нужно найти.
    :return: bool - True, если слово найдено, иначе False.
    """

    rows, cols = len(board), len(board[0])  # Размеры доски

    def backtrack(r: int, c: int, index: int) -> bool:
        """
        Рекурсивная функция для поиска `word` в `board`.

        :param r: int - текущая строка.
        :param c: int - текущий столбец.
        :param index: int - текущий индекс в слове `word`.
        :return: bool - True, если найдено слово, иначе False.
        """

        if index == len(word):  # Если нашли всё слово
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False  # Вышли за границы или не совпадает буква

        # Помечаем ячейку как использованную, чтобы избежать повторного использования
        temp, board[r][c] = board[r][c], '#'

        # Проверяем 4 направления: вниз, вверх, вправо, влево
        found = (
            backtrack(r + 1, c, index + 1) or
            backtrack(r - 1, c, index + 1) or
            backtrack(r, c + 1, index + 1) or
            backtrack(r, c - 1, index + 1)
        )

        board[r][c] = temp  # Восстанавливаем букву после рекурсии
        return found

    # Запускаем поиск с каждой клетки доски
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and backtrack(r, c, 0):
                return True

    return False


# 🔹 Тестируем
board1 = [
  ['A', 'B', 'C', 'E'],
  ['S', 'F', 'C', 'S'],
  ['A', 'D', 'E', 'E']
]
word1 = "ABCCED"
word2 = "SEE"
word3 = "ABCB"

print(exist(board1, word1))  # Ожидаемый результат: True
print(exist(board1, word2))  # Ожидаемый результат: True
print(exist(board1, word3))  # Ожидаемый результат: False

"""
Анализ сложности:
- Временная сложность: O(m * n * 4^k), где `m × n` — размер доски, `k` — длина `word`.
- Пространственная сложность: O(k), так как глубина рекурсии ограничена `len(word)`.
"""
