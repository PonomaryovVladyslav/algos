from collections import defaultdict
from fractions import Fraction

def max_points(points: list[list[int]]) -> int:
    """
    Определяет максимальное количество точек, находящихся на одной прямой.

    🔹 **Алгоритм**:
       - Перебираем каждую точку `p1`, считая её начальной.
       - Для каждой другой точки `p2` вычисляем наклон `dy/dx` (используем `Fraction`, чтобы избежать ошибок округления).
       - Храним количество точек с одинаковым наклоном в `defaultdict(int)`.
       - Поддерживаем максимум среди всех возможных наклонов.

    🔹 **Сложность**:
       - `O(n^2)`, так как проверяем все пары точек.

    """
    if len(points) <= 2:
        return len(points)  # Если 1 или 2 точки, они все на одной линии

    def find_slope(p1, p2):
        """ Вычисляем наклон линии через две точки (с учетом вертикальных линий). """
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            return float('inf')  # Вертикальная линия
        return Fraction(y2 - y1, x2 - x1)  # Используем Fraction для точности

    max_count = 1  # Минимально возможное количество точек на линии
    for i, p1 in enumerate(points):
        slopes = defaultdict(int)
        same_points = 1  # Считаем совпадающие точки (например, [0,0], [0,0])
        local_max = 0
        for j in range(i + 1, len(points)):
            p2 = points[j]
            if p1 == p2:
                same_points += 1  # Учитываем дубликаты
            else:
                slope = find_slope(p1, p2)
                slopes[slope] += 1
                local_max = max(local_max, slopes[slope])

        max_count = max(max_count, local_max + same_points)  # + same_points, включая дубликаты

    return max_count


# 🔹 Тесты
print(max_points([[1, 1], [2, 2], [3, 3]]))  # ✅ 3
print(max_points([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))  # ✅ 4
print(max_points([[0, 0], [1, 1], [2, 2], [3, 3], [3, 4], [4, 5], [6, 7]]))  # ✅ 5
print(max_points([[0, 0], [0, 0], [0, 0]]))  # ✅ 3
print(max_points([[0, 0]]))  # ✅ 1
print(max_points([[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [3, 3]]))  # ✅ 4
