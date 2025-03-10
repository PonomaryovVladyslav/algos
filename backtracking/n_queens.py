# Задача: Найти количество решений задачи N-ферзей.
# Дано: число `n`, представляющее размер шахматной доски `n x n`.
# Нужно: вернуть количество возможных расстановок `n` ферзей так, чтобы они не били друг друга.

def total_n_queens(n: int) -> int:
    """
    Функция вычисляет количество возможных расстановок `n` ферзей на `n x n` доске.

    :param n: int - размер шахматной доски (и количество ферзей).
    :return: int - количество возможных расстановок.
    """

    def backtrack(row: int, cols: set[int], diag1: set[int], diag2: set[int]) -> int:
        """
        Рекурсивная функция для поиска всех возможных расстановок ферзей.

        :param row: int - текущая строка, где размещаем ферзя.
        :param cols: set[int] - множество занятых колонок.
        :param diag1: set[int] - множество занятых диагоналей (row + col).
        :param diag2: set[int] - множество занятых диагоналей (row - col).
        :return: int - количество возможных расстановок с текущими ограничениями.
        """

        if row == n:  # Если удалось разместить `n` ферзей, засчитываем решение
            return 1

        count: int = 0
        for col in range(n):  # Пробуем поставить ферзя в каждую колонку текущей строки
            if col in cols or (row + col) in diag1 or (row - col) in diag2:
                continue  # Если ферзи бьют друг друга, пропускаем

            # Размещаем ферзя
            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)

            count += backtrack(row + 1, cols, diag1, diag2)  # Рекурсивный вызов для следующей строки

            # Убираем ферзя (backtracking)
            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)

        return count

    return backtrack(0, set(), set(), set())


# 🔹 Тестируем
print(total_n_queens(4))  # Ожидаемый результат: 2
print(total_n_queens(8))  # Ожидаемый результат: 92

"""
Анализ сложности:
- Временная сложность: O(n!), так как в худшем случае мы пробуем все возможные расстановки.
- Пространственная сложность: O(n), так как мы храним три множества (`cols`, `diag1`, `diag2`) для ограничений.
"""
