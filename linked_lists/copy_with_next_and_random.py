class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head: Node) -> Node:
    """
    Клонирует связанный список с произвольными указателями.

    🔹 **Алгоритм (O(1) памяти, O(n) времени)**:
       1. **Вставляем копии узлов**: `A → A' → B → B' → C → C'`
       2. **Обновляем `random` указатели**: `A'.random = A.random.next`
       3. **Разъединяем списки**: `A → B → C` и `A' → B' → C'`

    🔹 **Временная сложность**:
       - `O(n)`, так как мы трижды проходим по списку.

    🔹 **Пространственная сложность**:
       - `O(1)`, так как не используем дополнительную хеш-таблицу.

    :param head: Node - Голова исходного списка.
    :return: Node - Голова клонированного списка.
    """
    if not head:
        return None

    # 1. Вставляем копии узлов после оригиналов
    current = head
    while current:
        new_node = Node(current.val, current.next, None)
        current.next = new_node
        current = new_node.next

    # 2. Обновляем `random` указатели для новых узлов
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # 3. Разъединяем оригинальный и клонированный списки
    current = head
    new_head = head.next
    copy = new_head
    while current:
        current.next = copy.next
        current = current.next
        if copy.next:
            copy.next = copy.next.next
            copy = copy.next

    return new_head
