def is_palindrome(x: int) -> bool:
    """
    Проверяет, является ли число палиндромом (читается одинаково справа и слева).

    🔹 **Алгоритм**:
       - Отрицательные числа **не** могут быть палиндромами.
       - Разворачиваем число, создавая `reversed_x`, аналогично перевороту строки.
       - Если исходное число `x` совпадает с перевёрнутым, оно палиндром.

    🔹 **Сложность**:
       - `O(log n)`, так как число делится на `10` на каждой итерации.
    """
    if x < 0:
        return False  # Отрицательные числа не могут быть палиндромами

    original = x
    reversed_x = 0

    while x > 0:
        reversed_x = reversed_x * 10 + x % 10  # Добавляем последнюю цифру
        x //= 10  # Убираем последнюю цифру

    return original == reversed_x


# 🔹 Тесты
print(is_palindrome(121))  # ✅ True
print(is_palindrome(-121))  # ✅ False
print(is_palindrome(10))  # ✅ False
print(is_palindrome(1221))  # ✅ True
print(is_palindrome(0))  # ✅ True
print(is_palindrome(123321))  # ✅ True
