def spiral_order(matrix: list[list[int]]) -> list[int]:
    """
    Возвращает элементы матрицы, обходя её по спирали.

    🔹 **Алгоритм (O(m × n))**:
       1. Двигаемся **вправо**, затем **вниз**, **влево** и **вверх**.
       2. Постепенно уменьшаем границы (`top`, `bottom`, `left`, `right`).
       3. Повторяем, пока не выйдем за границы.

    🔹 **Сложность**:
       - `O(m × n)` по времени (каждый элемент посещаем 1 раз).
       - `O(1)` по памяти (используем только `result`).

    ✅ **Пример 1**:
       ```
       Вход: [[1,2,3],
              [4,5,6],
              [7,8,9]]

       Выход: [1, 2, 3, 6, 9, 8, 7, 4, 5]
       ```
    ✅ **Пример 2**:
       ```
       Вход: [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]]

       Выход: [1,2,3,4,8,12,11,10,9,5,6,7]
       ```
    """
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while left <= right and top <= bottom:
        # Двигаемся вправо →
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Двигаемся вниз ↓
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Двигаемся влево ← (если есть строки)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Двигаемся вверх ↑ (если есть колонки)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


# 🔹 Тест 1 (3x3 матрица)
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(spiral_order(matrix1))  # ✅ [1, 2, 3, 6, 9, 8, 7, 4, 5]

# 🔹 Тест 2 (3x4 матрица)
matrix2 = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
]
print(spiral_order(matrix2))  # ✅ [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
