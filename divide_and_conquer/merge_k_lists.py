from heapq import heappush, heappop


# Задача: Слить `k` отсортированных односвязных списков в один отсортированный список.
# Дано: список `lists`, содержащий `k` отсортированных связных списков.
# Нужно: вернуть голову **отсортированного объединённого списка**.

class ListNode:
    """
    Класс узла односвязного списка.
    """
    def __init__(self, val: int = 0, next: "ListNode" | None = None):
        self.val = val
        self.next = next

    def __lt__(self, other: "ListNode") -> bool:
        """
        Определяем порядок для heapq (нужно для работы кучи).
        """
        return self.val < other.val


def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    """
    Функция объединяет `k` отсортированных списков в один отсортированный (использует `heapq`).

    🔹 Временная сложность: O(N log k), где `N` — общее количество элементов, `k` — количество списков.
    🔹 Пространственная сложность: O(k), так как в куче хранятся `k` узлов.

    :param lists: list[ListNode | None] - список `k` отсортированных списков.
    :return: ListNode | None - голова объединённого отсортированного списка.
    """

    heap: list[ListNode] = []

    # 1. Добавляем в кучу первый элемент каждого списка
    for l in lists:
        if l:
            heappush(heap, l)

    dummy: ListNode = ListNode(0)
    cur: ListNode = dummy

    # 2. Извлекаем минимальный элемент и добавляем следующий
    while heap:
        node: ListNode = heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heappush(heap, node.next)

    return dummy.next


def list_to_linked(lst: list[int]) -> ListNode | None:
    """
    Функция преобразует список в односвязный список.

    :param lst: list[int] - список значений.
    :return: ListNode | None - голова односвязного списка.
    """
    dummy: ListNode = ListNode()
    cur: ListNode = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def linked_to_list(head: ListNode | None) -> list[int]:
    """
    Функция преобразует односвязный список в обычный список.

    :param head: ListNode | None - голова односвязного списка.
    :return: list[int] - список значений.
    """
    result: list[int] = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# 🔹 Тестируем
lists = [
    list_to_linked([1, 4, 5]),
    list_to_linked([1, 3, 4]),
    list_to_linked([2, 6])
]

merged_head = merge_k_lists(lists)
print(linked_to_list(merged_head))  # ✅ Ожидаемый результат: [1, 1, 2, 3, 4, 4, 5, 6]


"""
🔹 Анализ сложности:

✅ Временная сложность: **O(N log k)**
   - `N` — общее количество узлов во всех списках.
   - `k` — количество входных списков.
   - Каждую операцию в куче выполняем за **O(log k)**, а вставляем **всего `N` узлов**.

✅ Пространственная сложность: **O(k)**
   - В куче **одновременно хранятся `k` узлов**.

📌 **Как работает `heapq`?**
1️⃣ **Добавляем первые элементы всех `k` списков** в кучу `heap`.  
2️⃣ **Извлекаем минимальный элемент**, добавляем его в результат.  
3️⃣ **Если у узла есть `next`**, добавляем его в кучу.  
4️⃣ **Повторяем, пока куча не пуста**.  

💡 **Почему используется `heapq`?**
- **Поддерживает минимум за O(1)**.
- **Вставка и удаление за O(log k)**.
- Работает **лучше, чем O(kN) при последовательном слиянии списков**.

"""
