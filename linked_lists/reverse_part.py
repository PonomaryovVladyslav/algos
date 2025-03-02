class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    """
    Разворачивает часть списка от `left` до `right` (1-based index).

    🔹 **Алгоритм**:
       1. Используем фиктивный узел `dummy` перед `head`.
       2. Доходим до узла **перед `left`** (`prev`).
       3. Разворачиваем `right - left + 1` узлов **в месте**.
       4. Соединяем развернутый участок со списком.

    🔹 **Сложность**:
       - `O(n)`, так как мы проходим по списку максимум 2 раза.
       - `O(1)`, так как используется только несколько указателей.
    """

    if not head or left == right:
        return head  # Ничего не меняем

    dummy = ListNode(0, head)  # Фиктивный узел перед head
    prev = dummy

    # 1. Доходим до узла перед `left`
    for _ in range(left - 1):
        prev = prev.next

    # 2. Разворачиваем часть списка
    reverse_start = prev.next  # Узел, с которого начнется разворот
    curr = reverse_start.next  # Следующий узел

    for _ in range(right - left):
        reverse_start.next = curr.next  # Переставляем ссылку
        curr.next = prev.next  # Меняем направление
        prev.next = curr  # Двигаем prev.next на новый узел
        curr = reverse_start.next  # Переходим к следующему узлу

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
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

print("Исходный список:")
print_list(head1)
new_head1 = reverse_between(head1, 2, 4)
print("После разворота [2,4]:")
print_list(new_head1)  # 1 -> 4 -> 3 -> 2 -> 5

print("\nИсходный список:")
print_list(head2)
new_head2 = reverse_between(head2, 1, 3)
print("После разворота [1,3]:")
print_list(new_head2)  # 3 -> 2 -> 1 -> 4 -> 5 -> 6
