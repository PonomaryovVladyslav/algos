class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def set_next(self, next):
        self.next = next


def find_cycle(head: ListNode) -> bool:
    """
    Определяет наличие цикла в связном списке.

    🔹 **Алгоритм (Флойд "черепаха и заяц")**:
       1. Два указателя (`slow`, `fast`).
       2. `slow` движется на 1 шаг, `fast` на 2 шага.
       3. Если `fast` догонит `slow`, значит есть цикл.
       4. Если `fast` достигает `None`, цикла нет.

    🔹 **Временная сложность**:
       - `O(n)`, так как оба указателя проходят список не более одного раза.

    🔹 **Пространственная сложность**:
       - `O(1)`, так как используем только два указателя.

    :param head: ListNode - Голова списка.
    :return: bool - `True`, если есть цикл, иначе `False`.
    """
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True  # Обнаружен цикл

    return False  # Цикла нет


# Создание списка с циклом:
l1 = ListNode(3)
l2 = ListNode(2)
l3 = ListNode(0)
l4 = ListNode(-4)

l1.set_next(l2)
l2.set_next(l3)
l3.set_next(l4)
l4.set_next(l2)  # Цикл: l4 → l2

print(find_cycle(l1))  # ✅ True

# Тест без цикла
l5 = ListNode(1)
l6 = ListNode(2)
l5.set_next(l6)

print(find_cycle(l5))  # ✅ False
