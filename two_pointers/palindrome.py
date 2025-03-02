def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():  # Пропускаем не-алфавитные символы
            left += 1
        while left < right and not s[right].isalnum():  # Пропускаем не-алфавитные символы
            right -= 1

        if s[left].lower() != s[right].lower():  # Сравниваем в нижнем регистре
            return False

        left += 1
        right -= 1

    return True
print(is_palindrome("abcba"))