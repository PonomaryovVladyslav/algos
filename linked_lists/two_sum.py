class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


def sum_two_ll(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Складывает два числа, представленных в виде перевёрнутых связанных списков.

    🔹 **Алгоритм**:
       1. Проходим по двум спискам, складываем соответствующие цифры + перенос.
       2. Если сумма >= 10, сохраняем `sum % 10`, а `carry = 1`.
       3. Если после завершения списков `carry == 1`, добавляем ещё один узел.

    🔹 **Сложность**:
       - `O(max(N, M))`, где `N` и `M` — длины списков.
       - `O(1)` доп. памяти, так как используем только несколько указателей.
    """

    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0  # Берём число из l1 или 0, если l1 кончился
        val2 = l2.val if l2 else 0  # Аналогично для l2
        total = val1 + val2 + carry

        carry = total // 10  # Перенос на следующий разряд
        curr.next = ListNode(total % 10)  # Записываем последнюю цифру в новый узел
        curr = curr.next

        if l1:
            l1 = l1.next  # Переход к следующему узлу l1
        if l2:
            l2 = l2.next  # Переход к следующему узлу l2

    return dummy.next


# 🔹 Создание тестовых списков
l11 = ListNode(2, ListNode(4, ListNode(3)))  # 342
l21 = ListNode(5, ListNode(6, ListNode(4, ListNode(1))))  # 1465

# 🔹 Сложение чисел
result = sum_two_ll(l11, l21)

# 🔹 Вывод результата
while result:
    print(result.val, end=" -> " if result.next else "")
    result = result.next
# Вывод: 7 -> 0 -> 8 -> 1  (342 + 1465 = 1807)
