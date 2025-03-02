class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_duplicates(head: ListNode) -> ListNode:
    """
    Удаляет все узлы, имеющие дубликаты, из отсортированного связного списка.

    🔹 **Алгоритм**:
       - Используем фиктивный узел `dummy` перед `head` для удобства работы.
       - Проходим по списку:
         - Если встречаем дубликаты (`val == next.val`), пропускаем все такие узлы.
         - Если нет дубликатов, просто двигаемся дальше.
       - В конце возвращаем `dummy.next`.

    🔹 **Сложность**:
       - `O(n)`, так как мы проходим по списку один раз.
       - `O(1)` по памяти (не учитывая выходной список).
    """

    dummy = ListNode(0, head)  # Фиктивный узел перед head
    prev = dummy
    current = head

    while current:
        if current.next and current.val == current.next.val:  # Если есть дубликаты
            while current.next and current.val == current.next.val:
                current = current.next  # Пропускаем все одинаковые узлы
            prev.next = current.next  # Удаляем всю группу дубликатов
        else:
            prev = prev.next  # Двигаем prev вперёд
        current = current.next  # Двигаем current

    return dummy.next


# 🔹 Функция для вывода списка
def print_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values) if values else "Empty list")


# 🔹 Тестовые примеры
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
head2 = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
head3 = ListNode(1, ListNode(1))

print("Исходный список:")
print_list(head1)
new_head1 = delete_duplicates(head1)
print("После удаления дубликатов:")
print_list(new_head1)  # 1 -> 2 -> 5

print("\nИсходный список:")
print_list(head2)
new_head2 = delete_duplicates(head2)
print("После удаления дубликатов:")
print_list(new_head2)  # 2 -> 3

print("\nИсходный список:")
print_list(head3)
new_head3 = delete_duplicates(head3)
print("После удаления дубликатов:")
print_list(new_head3)  # Empty list
