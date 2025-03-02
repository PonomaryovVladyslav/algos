def find_longest_valid_brackets(s: str) -> int:
    """
    Находит длину самой длинной правильной последовательности скобок.

    🔹 **Метод**: Используем стек для отслеживания открывающих скобок и начала некорректных последовательностей.
    🔹 **Сложность**: O(n) — один проход по строке.
    🔹 **Память**: O(n) — в худшем случае стек может содержать все открытые скобки.

    ✅ **Пример работы**:
       ```
       Вход: "(()())" → Выход: 6
       Вход: ")()())" → Выход: 4
       Вход: "))((" → Выход: 0
       ```
    """
    stack = []
    longest = 0
    start = -1  # Последняя позиция некорректной закрывающей скобки

    for i, char in enumerate(s):
        if char == "(":  
            stack.append(i)  # Запоминаем индекс открывающей скобки
        else:
            if stack:
                stack.pop()  # Закрываем последнюю открытую скобку
                if stack:
                    longest = max(longest, i - stack[-1])  # Длина между текущей и последней в стеке
                else:
                    longest = max(longest, i - start)  # Длина между текущей и началом
            else:
                start = i  # Обновляем начальный индекс для следующей последовательности

    return longest

# 🔹 Тестируем
print(find_longest_valid_brackets("(()())"))  # ✅ 6
print(find_longest_valid_brackets(")()())"))  # ✅ 4
print(find_longest_valid_brackets("))(("))    # ✅ 0
print(find_longest_valid_brackets("()(()"))   # ✅ 2
print(find_longest_valid_brackets("()()()"))  # ✅ 6
