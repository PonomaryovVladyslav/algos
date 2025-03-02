brackets = {
    "}": "{",
    "]": "[",
    ")": "("
}

def is_valid_brackets(s: str) -> bool:
    """
    Проверяет, является ли строка `s` правильной скобочной последовательностью.

    🔹 **Метод**: Используем стек
    🔹 **Сложность**: O(n) — проходим по строке один раз
    🔹 **Память**: O(n) — стек может хранить все символы в худшем случае

    ✅ **Пример работы**:
       ```
       Вход: "(()())"  → Выход: True
       Вход: ")()())"  → Выход: False
       Вход: "))(("    → Выход: False
       Вход: "((()))"  → Выход: True
       ```
    """
    stack = []
    for char in s:
        if char in brackets.values():  # Открывающая скобка
            stack.append(char)
        elif char in brackets:  # Закрывающая скобка
            if not stack or stack[-1] != brackets[char]:  # Нет пары
                return False
            stack.pop()  # Удаляем пару

    return not stack  # Если стек пуст — последовательность правильная

# 🔹 Тестируем
s1 = "(()())"
s2 = ")()())"
s3 = "))(("
s4 = "((()))"
s5 = "{[()]}"
s6 = "{[(])}"  # ❌ Неверно: скобки не в правильном порядке
s7 = "{[()()]}"  # ✅ Верно
s8 = "[({})](())"

print(is_valid_brackets(s1))  # ✅ True
print(is_valid_brackets(s2))  # ❌ False
print(is_valid_brackets(s3))  # ❌ False
print(is_valid_brackets(s4))  # ✅ True
print(is_valid_brackets(s5))  # ✅ True
print(is_valid_brackets(s6))  # ❌ False
print(is_valid_brackets(s7))  # ✅ True
print(is_valid_brackets(s8))  # ✅ True
