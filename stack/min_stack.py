class MinStack:
    """
    Реализация стека с дополнительной поддержкой получения минимума за O(1).

    🔹 **Методы**:
        - `push(val)`: Добавляет элемент в стек.
        - `pop()`: Удаляет верхний элемент.
        - `top()`: Возвращает верхний элемент.
        - `get_min()`: Возвращает минимальный элемент.

    🔹 **Структуры**:
        - `stack`: Основной стек (содержит все элементы).
        - `min_stack`: Дополнительный стек (содержит только минимумы).

    🔹 **Сложность**:
        - `O(1)` — вставка (`push`), удаление (`pop`), поиск (`top`), минимум (`get_min`).
        - `O(n)` — память (из-за `min_stack`).

    ✅ **Пример работы**:
       ```
       minstack = MinStack()
       minstack.push(1)
       minstack.push(3)
       minstack.push(2)
       minstack.pop()
       print(minstack.get_min())  # Выведет 1
       ```
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """ Добавляет элемент в стек и обновляет min_stack. """
        self.stack.append(val)
        # Если min_stack пуст или val <= текущего минимума
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """ Удаляет верхний элемент из стека и min_stack (если он был минимумом). """
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:  # Если удаляем минимум
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        """ Возвращает верхний элемент стека (или None, если стек пуст). """
        return self.stack[-1] if self.stack else None

    def get_min(self) -> int:
        """ Возвращает минимальный элемент в стеке. """
        return self.min_stack[-1] if self.min_stack else None


# 🔹 Тестируем MinStack
minstack = MinStack()
minstack.push(1)
minstack.push(3)
minstack.push(2)
minstack.pop()
print(minstack.get_min())  # ✅ 1
