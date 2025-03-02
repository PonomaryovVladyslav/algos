# Задача: Найти `target` в отсортированной матрице.
# Дано: `matrix` (m x n), где каждая строка отсортирована слева направо,
# а первый элемент каждой строки больше последнего элемента предыдущей строки.
# Нужно: вернуть `True`, если `target` найден, иначе `False`.

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """
    Функция выполняет бинарный поиск `target` в `matrix`.

    :param matrix: list[list[int]] - отсортированная матрица размером `m x n`.
    :param target: int - искомое число.
    :return: bool - `True`, если `target` найден, иначе `False`.
    """

    if not matrix or not matrix[0]:  # Проверка на пустую матрицу
        return False

    m, n = len(matrix), len(matrix[0])  # Размеры матрицы
    left, right = 0, m * n - 1  # Индексы для бинарного поиска

    while left <= right:
        mid = (left + right) // 2
        row, col = divmod(mid, n)  # row = mid // n, col = mid % n

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# 🔹 Тестируем
matrix1 = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
print(search_matrix(matrix1, 3))  # Ожидаемый результат: True
print(search_matrix(matrix1, 13))  # Ожидаемый результат: False

matrix2 = [[1]]
print(search_matrix(matrix2, 1))  # Ожидаемый результат: True
print(search_matrix(matrix2, 2))  # Ожидаемый результат: False

"""
Анализ сложности:
- Временная сложность: O(log(m * n)), так как применяется бинарный поиск по всей матрице.
- Пространственная сложность: O(1), так как не используется дополнительная память.
"""
