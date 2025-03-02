class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head: ListNode, x: int) -> ListNode:
    """
    Разделяет список так, чтобы все узлы < x были перед узлами >= x,
    сохраняя порядок элементов.

    🔹 **Алгоритм**:
       - Создаём два списка: один для элементов `< x`, другой для `>= x`.
       - Проходим по списку и распределяем узлы в соответствующие списки.
       - Соединяем оба списка и возвращаем результат.

    🔹 **Сложность**:
       - `O(n)`, так как мы проходим по списку один раз.
       - `O(1)` по памяти (не учитывая выходной список).

    """

    before_dummy = ListNode(0)  # Начало списка < x
    after_dummy = ListNode(0)   # Начало списка >= x
    before = before_dummy
    after = after_dummy

    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next

    after.next = None  # Завершаем список >= x
    before.next = after_dummy.next  # Соединяем списки

    return before_dummy.next


# 🔹 Тестирование
def print_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values))


# Исходный список: 1 -> 4 -> 3 -> 2 -> 5 -> 2
head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))

print("Исходный список:")
print_list(head)

# Разбиваем относительно x = 3
new_head = partition(head, 3)

print("\nПосле разбиения (x=3):")
print_list(new_head)
