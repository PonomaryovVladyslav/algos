def set_zeros(matrix: list[list[int]]) -> None:
    """
    Обнуляет строки и столбцы, содержащие хотя бы один `0`.

    🔹 **Алгоритм (O(m × n))**:
       1. Определяем, какие строки и столбцы содержат `0`.
       2. Обнуляем соответствующие строки и столбцы.

    🔹 **Сложность**:
       - `O(m × n)` по времени (проходим по всей матрице).
       - `O(m + n)` по памяти (используем множества для хранения индексов).
    """
    zero_rows = set()
    zero_cols = set()

    # 1. Запоминаем, где есть `0`
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # 2. Обнуляем строки
    for row in zero_rows:
        for j in range(len(matrix[0])):
            matrix[row][j] = 0

    # 3. Обнуляем столбцы
    for col in zero_cols:
        for i in range(len(matrix)):
            matrix[i][col] = 0


# 🔹 Тест
matrix1 = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]

set_zeros(matrix1)

# 🔹 Ожидаемый результат:
# [[0, 0, 0, 0],
#  [0, 4, 5, 0],
#  [0, 3, 1, 0]]

for row in matrix1:
    print(row)
