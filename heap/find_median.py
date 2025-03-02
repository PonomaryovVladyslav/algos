from heapq import heappush, heappop


class MedianFinder:
    """
    Класс для нахождения медианы потока чисел.

    🔹 **Алгоритм (O(log n) на вставку, O(1) на поиск медианы)**:
       - Используем две кучи:
         1️⃣ `max_heap` (левая половина) хранит отрицательные значения, имитируя max heap.
         2️⃣ `min_heap` (правая половина) хранит положительные значения, являясь min heap.
       - Вставляем в `max_heap`, затем переносим наименьший элемент в `min_heap`.
       - Если `min_heap` больше `max_heap`, балансируем обратно.

    🔹 **Временная сложность**:
       - `add_num`: O(log n) за счёт вставки в кучу.
       - `find_median`: O(1), так как медиана извлекается мгновенно.

    🔹 **Пространственная сложность**:
       - `O(n)`, так как храним все числа.

    """

    def __init__(self):
        self.max_heap = []  # Левая половина (max heap через отрицательные значения)
        self.min_heap = []  # Правая половина (min heap)

    def add_num(self, num: int) -> None:
        """
        Добавляет число в структуру данных.

        :param num: int - Число для добавления.
        """
        heappush(self.max_heap, -num)  # Добавляем в max heap (инвертируя знак)

        # Перемещаем макс. элемент из max_heap в min_heap для балансировки
        heappush(self.min_heap, -heappop(self.max_heap))

        # Поддерживаем `max_heap` больше либо равным по размеру `min_heap`
        if len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self) -> float:
        """
        Возвращает текущую медиану.

        :return: float - Медиана текущего набора чисел.
        """
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]  # Число из max_heap
        return (-self.max_heap[0] + self.min_heap[0]) / 2  # Среднее двух центральных


# 🔹 Тесты
mf = MedianFinder()
mf.add_num(1)
mf.add_num(2)
print(mf.find_median())  # ✅ 1.5
mf.add_num(3)
print(mf.find_median())  # ✅ 2
mf.add_num(4)
print(mf.find_median())  # ✅ 2.5
mf.add_num(5)
print(mf.find_median())  # ✅ 3
