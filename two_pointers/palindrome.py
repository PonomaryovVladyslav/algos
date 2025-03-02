def is_palindrome(s: str) -> bool:
    """
    Проверить, является ли строка палиндромом (игнорируя пробелы, знаки препинания и регистр).

    Палиндром — это строка, которая читается одинаково слева направо и справа налево.

    Вход:
    s = "A man, a plan, a canal: Panama"

    Выход:
    True  (Игнорируем знаки, регистр: "amanaplanacanalpanama" == "amanaplanacanalpanama")

    Решение:
    - Используем два указателя `left` (с начала) и `right` (с конца).
    - Пропускаем не-буквенно-цифровые символы.
    - Сравниваем символы без учета регистра.

    Время: O(n) — один линейный проход по строке.
    Пространство: O(1) — используем только указатели.
    """

    left, right = 0, len(s) - 1

    while left < right:
        # Пропускаем не-буквенно-цифровые символы
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        # Сравниваем символы в нижнем регистре
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Тесты
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False
print(is_palindrome(" "))  # True (пустая строка)
print(is_palindrome("abcba"))  # True
print(is_palindrome("No 'x' in Nixon"))  # True
