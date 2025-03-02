class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotate_right(head: ListNode, k: int) -> ListNode:
    """
    Сдвигает связный список вправо на `k` позиций.

    🔹 **Алгоритм**:
       1. Определяем длину списка `length` и находим хвост `tail`.
       2. Вычисляем реальное число сдвигов: `k = k % length`.
       3. Находим новый хвост (узел `length - k - 1`) и новую голову (`length - k`).
       4. Разрываем связь и соединяем конец с началом.

    🔹 **Сложность**:
       - `O(n)`, так как делаем 2 прохода.
       - `O(1)`, так как используем только несколько указателей.
    """

    if not head or not head.next or k == 0:
        return head

    # 1. Определяем длину списка
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # 2. Определяем реальный сдвиг
    k = k % length
    if k == 0:
        return head  # Никакого сдвига не нужно

    # 3. Найти новый хвост (узел `length - k - 1`) и новую голову (`length - k`)
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    new_head = new_tail.next  # Новая голова

    # 4. Разрываем связь, соединяем конец списка с началом
    new_tail.next = None
    tail.next = head  # Старый хвост указывает на старую голову

    return new_head


# 🔹 Функция для вывода списка
def print_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values) if values else "Empty list")


# 🔹 Тестовые примеры
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Исходный список:")
print_list(head1)
new_head1 = rotate_right(head1, 2)
print("После сдвига на 2:")
print_list(new_head1)  # 4 -> 5 -> 1 -> 2 -> 3

head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

print("\nИсходный список:")
print_list(head2)
new_head2 = rotate_right(head2, 4)
print("После сдвига на 4:")
print_list(new_head2)  # 3 -> 4 -> 5 -> 6 -> 1 -> 2
