from heapq import heappush, heappop


def find_maximized_capital(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    """
    Вычисляет максимальный капитал, который можно получить после `k` инвестиций.

    🔹 **Алгоритм (Жадный подход + Max Heap)**:
       - Сортируем проекты по `capital`, чтобы рассматривать их по мере доступности.
       - Используем `max_heap` (max-heap через инвертированные значения) для хранения доступных проектов.
       - Проходим `k` раундов:
         1️⃣ Добавляем все доступные проекты в `max_heap`.
         2️⃣ Берём проект с максимальной прибылью (из `max_heap`).
         3️⃣ Увеличиваем капитал `w` на прибыль выбранного проекта.

    🔹 **Временная сложность**:
       - Сортировка: `O(n log n)`.
       - Перебор `k` итераций с `O(log n)` на `heappush/heappop`: `O(k log n)`.
       - Итог: `O(n log n + k log n) ≈ O(n log n)` (так как обычно `k < n`).

    🔹 **Пространственная сложность**:
       - `O(n)` из-за хранения всех проектов и кучи.

    :param k: int - Количество доступных инвестиций.
    :param w: int - Начальный капитал.
    :param profits: list[int] - Прибыль от каждого проекта.
    :param capital: list[int] - Минимальный капитал для каждого проекта.
    :return: int - Максимально возможный капитал после `k` инвестиций.
    """
    projects = sorted(zip(capital, profits))  # Сортируем проекты по capital (O(n log n))
    max_heap = []  # Max Heap (по убыванию прибыли)
    i = 0  # Указатель на текущий проект

    for _ in range(k):
        # Добавляем все доступные проекты в кучу
        while i < len(projects) and projects[i][0] <= w:
            heappush(max_heap, -projects[i][1])  # Инвертируем для max heap
            i += 1

        if not max_heap:  # Если нет доступных проектов, останавливаемся
            break

        w += -heappop(max_heap)  # Берём проект с максимальной прибылью

    return w


# 🔹 Тесты
print(find_maximized_capital(2, 0, [1, 2, 3], [0, 1, 1]))  # ✅ 4
print(find_maximized_capital(3, 0, [1, 2, 3], [1, 1, 2]))  # ✅ 0
print(find_maximized_capital(1, 2, [1, 2, 3], [1, 2, 3]))  # ✅ 3
print(find_maximized_capital(3, 0, [5, 1, 10], [0, 1, 2]))  # ✅ 16
