class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    """
    Удаляет `n`-й узел с конца в односвязном списке.

    🔹 **Алгоритм (метод двух указателей)**:
       1. Создаём фиктивный узел `dummy` перед `head` для удобства.
       2. Двигаем `fast` на `n + 1` шагов вперёд.
       3. Двигаем `fast` и `slow`, пока `fast` не достигнет конца.
       4. `slow` оказывается перед удаляемым узлом → удаляем `slow.next`.

    🔹 **Сложность**:
       - `O(n)`, так как мы проходим по списку один раз.
       - `O(1)`, так как используем только два указателя.
    """

    dummy = ListNode(0, head)  # Фиктивный узел перед head
    fast = slow = dummy

    # 1. Двигаем fast на n+1 шагов вперёд
    for _ in range(n + 1):
        fast = fast.next

    # 2. Двигаем fast и slow, пока fast не достигнет конца
    while fast:
        fast = fast.next
        slow = slow.next

    # 3. Удаляем slow.next (n-й узел с конца)
    slow.next = slow.next.next

    return dummy.next


# 🔹 Функция для вывода списка
def print_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values) if values else "Empty list")


# 🔹 Тестовые примеры
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
head3 = ListNode(1)

print("Исходный список:")
print_list(head1)
new_head1 = remove_nth_from_end(head1, 2)
print("После удаления 2-го с конца:")
print_list(new_head1)  # 1 -> 2 -> 3 -> 5

print("\nИсходный список:")
print_list(head2)
new_head2 = remove_nth_from_end(head2, 4)
print("После удаления 4-го с конца:")
print_list(new_head2)  # 2 -> 3 -> 4

print("\nИсходный список:")
print_list(head3)
new_head3 = remove_nth_from_end(head3, 1)
print("После удаления 1-го с конца:")
print_list(new_head3)  # Empty list
