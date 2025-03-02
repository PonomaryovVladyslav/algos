# Задача: Отсортировать односвязный список.
# Дано: `head` — голова односвязного списка.
# Нужно: вернуть голову **отсортированного списка**.

class ListNode:
    """
    Класс узла односвязного списка.
    """
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next


def sort_list(head: ListNode) -> ListNode | None:
    """
    Функция сортирует односвязный список (использует сортировку слиянием).

    🔹 Временная сложность: O(n log n), так как используем сортировку слиянием.
    🔹 Пространственная сложность: O(log n), так как выполняем рекурсивные вызовы.

    :param head: ListNode - голова несортированного списка.
    :return: ListNode | None - голова отсортированного списка.
    """

    if not head or not head.next:
        return head  # Если список пустой или состоит из 1 элемента

    # 1. Разделяем список на две части (ищем середину)
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid: ListNode = slow.next
    slow.next = None  # Разрываем связь (делаем два списка)

    # 2. Рекурсивно сортируем левую и правую половины
    left: ListNode = sort_list(head)
    right: ListNode = sort_list(mid)

    # 3. Сливаем две отсортированные половины
    return merge(left, right)


def merge(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """
    Функция сливает два отсортированных списка.

    🔹 Временная сложность: O(n), так как проходим по каждому узлу один раз.
    🔹 Пространственная сложность: O(1), так как используем только указатели.

    :param l1: ListNode | None - голова первого списка.
    :param l2: ListNode | None - голова второго списка.
    :return: ListNode | None - голова объединённого отсортированного списка.
    """

    dummy: ListNode = ListNode(0)
    cur: ListNode = dummy

    while l1 and l2:
        if l1.val < l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next

    cur.next = l1 if l1 else l2  # Добавляем оставшиеся элементы
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
head1 = list_to_linked([4, 2, 1, 3])
sorted_head1 = sort_list(head1)
print(linked_to_list(sorted_head1))  # ✅ Ожидаемый результат: [1, 2, 3, 4]

head2 = list_to_linked([-1, 5, 3, 4, 0])
sorted_head2 = sort_list(head2)
print(linked_to_list(sorted_head2))  # ✅ Ожидаемый результат: [-1, 0, 3, 4, 5]


"""
🔹 Анализ сложности:

✅ Временная сложность: **O(n log n)**
   - Используем **разделяй и властвуй** (сортировку слиянием).
   - Разбиваем список **log n раз**, а слияние каждого уровня занимает **O(n)**.
   - Итоговая сложность: **O(n log n)**.

✅ Пространственная сложность: **O(log n)**
   - Рекурсивная глубина **log n** (из-за разбиения).
   - Слияние занимает **O(1)** дополнительной памяти.

📌 **Как работает алгоритм?**
1️⃣ **Разделяем список** на две половины (используем два указателя `slow` и `fast`).  
2️⃣ **Рекурсивно сортируем** левую и правую половину.  
3️⃣ **Объединяем отсортированные списки** с помощью двух указателей.

💡 **Почему сортировка слиянием?**
- Работает за **O(n log n)** в **среднем и худшем случае**.
- **Идеально подходит** для **связных списков**, так как не требует случайного доступа.

"""
