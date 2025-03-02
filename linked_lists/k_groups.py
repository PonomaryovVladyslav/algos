class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head: ListNode, k: int) -> ListNode:
    """
    Разворачивает связанный список группами по `k` узлов.

    🔹 **Алгоритм**:
       1. Подсчитываем длину списка.
       2. Итерируемся, пока хватает `k` узлов для разворота.
       3. Разворачиваем текущие `k` узлов.
       4. Соединяем развернутую группу с предыдущей и следующей частью.
       5. Повторяем процесс, пока остаётся `k` узлов.

    🔹 **Временная сложность**:
       - `O(n)`, так как каждый узел обрабатывается дважды (подсчет + разворот).

    🔹 **Пространственная сложность**:
       - `O(1)`, так как используем константную дополнительную память.

    :param head: ListNode - Голова списка.
    :param k: int - Размер групп для разворота.
    :return: ListNode - Новая голова списка.
    """
    def reverse(first, last):
        prev, curr = None, first
        while curr != last:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    dummy = ListNode(0, head)
    prev_group = dummy
    curr = head

    # Считаем длину списка
    length = 0
    while curr:
        length += 1
        curr = curr.next

    curr = head
    while length >= k:
        next_group = curr
        for _ in range(k):
            next_group = next_group.next

        # Разворачиваем k-узловую группу
        new_head = reverse(curr, next_group)

        # Подключаем перевёрнутый кусок
        prev_group.next = new_head
        curr.next = next_group

        # Подготовка к следующей группе
        prev_group = curr
        curr = next_group
        length -= k

    return dummy.next


# Функция для создания связного списка из списка Python
def list_to_linked(lst):
    dummy = ListNode()
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

# Функция для вывода связного списка
def linked_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Тестовые примеры
head = list_to_linked([1, 2, 3, 4, 5, 6, 7, 8])
k = 3
new_head = reverse_k_group(head, k)
print(linked_to_list(new_head))  # ✅ [3, 2, 1, 6, 5, 4, 7, 8]

head = list_to_linked([1, 2, 3, 4, 5])
k = 2
new_head = reverse_k_group(head, k)
print(linked_to_list(new_head))  # ✅ [2, 1, 4, 3, 5]

head = list_to_linked([1])
k = 1
new_head = reverse_k_group(head, k)
print(linked_to_list(new_head))  # ✅ [1]

head = list_to_linked([1, 2, 3, 4, 5])
k = 3
new_head = reverse_k_group(head, k)
print(linked_to_list(new_head))  # ✅ [3, 2, 1, 4, 5]
