# Задача: Построить Quad-Tree по заданной бинарной матрице `grid`.
# Дано: `grid` — квадратная матрица `n x n`, где `grid[i][j]` — 0 или 1.
# Нужно: вернуть корень Quad-Tree, представляющий эту матрицу.

class Node:
    """
    Класс узла Quad-Tree.
    """

    def __init__(
            self,
            val: bool,
            is_leaf: bool,
            top_left: "Node" | None = None,
            top_right: "Node" | None = None,
            bottom_left: "Node" | None = None,
            bottom_right: "Node" | None = None
    ):
        self.val = val
        self.is_leaf = is_leaf
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right


def construct(grid: list[list[int]]) -> Node:
    """
    Функция строит Quad-Tree из бинарной матрицы `grid`.

    🔹 Временная сложность: O(n²) в худшем случае (если нет однородных областей).
    🔹 Пространственная сложность: O(n²) в худшем случае (если все листовые узлы уникальны).

    :param grid: list[list[int]] - бинарная матрица `n x n`.
    :return: Node - корень Quad-Tree.
    """

    def is_uniform(r1: int, c1: int, r2: int, c2: int) -> tuple[bool, int | None]:
        """
        Проверяет, является ли область `grid[r1:r2, c1:c2]` однородной.

        :return: (True, value) - если все элементы одинаковы.
                 (False, None) - если есть смешанные значения.
        """
        val = grid[r1][c1]
        for r in range(r1, r2):
            for c in range(c1, c2):
                if grid[r][c] != val:
                    return False, None
        return True, val  # Возвращаем (is_leaf, значение)

    def build(r1: int, c1: int, r2: int, c2: int) -> Node:
        """
        Рекурсивно строит Quad-Tree.

        :param r1: int - начальная строка.
        :param c1: int - начальный столбец.
        :param r2: int - конечная строка.
        :param c2: int - конечный столбец.
        :return: Node - узел Quad-Tree.
        """
        uniform, val = is_uniform(r1, c1, r2, c2)
        if uniform:
            return Node(val == 1, True)  # Лист (is_leaf=True)

        mid_r, mid_c = (r1 + r2) // 2, (c1 + c2) // 2

        return Node(
            True, False,  # Внутренний узел (is_leaf=False)
            build(r1, c1, mid_r, mid_c),  # Верх-лево
            build(r1, mid_c, mid_r, c2),  # Верх-право
            build(mid_r, c1, r2, mid_c),  # Низ-лево
            build(mid_r, mid_c, r2, c2)  # Низ-право
        )

    return build(0, 0, len(grid), len(grid))


# 🔹 Тестируем
grid = [
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0]
]

quad_tree = construct(grid)


# Функция для вывода структуры Quad-Tree
def serialize(node: Node | None) -> list | None:
    """
    Функция сериализует Quad-Tree в список.

    :param node: Node | None - корень Quad-Tree.
    :return: list - сериализованный список.
    """
    if not node:
        return None
    if node.is_leaf:
        return [1 if node.val else 0, 1]  # [val, is_leaf]
    return [0, 0, serialize(node.top_left), serialize(node.top_right),
            serialize(node.bottom_left), serialize(node.bottom_right)]


print(serialize(quad_tree))  # Выводит структуру Quad-Tree

"""
🔹 Анализ сложности:

✅ Временная сложность: **O(n²)** в худшем случае.
   - Если `grid` состоит из **разных значений**, мы обрабатываем все `n²` ячеек.
   - В среднем случае быстрее, если есть **однородные области**.

✅ Пространственная сложность: **O(n²)** в худшем случае.
   - Если все элементы **разные**, создаётся `n²` листовых узлов.
   - Если `grid` состоит из **единичного значения**, занимаем **O(1)** памяти.

📌 **Как работает алгоритм?**
1️⃣ **Проверяем, является ли текущая область однородной**.  
   - Если да → создаём **листовой узел**.  
   - Если нет → **разбиваем область на 4 части**.  
2️⃣ **Рекурсивно строим Quad-Tree** для 4 квадрантов.  
3️⃣ **Возвращаем корень дерева**.

💡 **Когда Quad-Tree полезен?**
- **Сжатие изображений** (например, для чёрно-белых карт).  
- **Геопространственные структуры** (например, разбиение карт).  
- **Иерархическое хранение данных** (например, индексация 2D-объектов).  

"""
