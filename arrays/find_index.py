# Задача: Найти индекс первого вхождения подстроки (needle) в строке (haystack).
# Если подстрока отсутствует, вернуть -1.
# Аналог метода str.find().

def find_index(haystack: str, needle: str) -> int:
    """
    Функция ищет первое вхождение подстроки needle в строке haystack.

    :param haystack: str - строка, в которой выполняется поиск.
    :param needle: str - подстрока, которую нужно найти.
    :return: int - индекс первого вхождения needle в haystack, либо -1, если needle не найден.
    """

    # Проходим по haystack, проверяя срез длиной needle
    for i in range(len(haystack) - len(needle) + 1):  # Останавливаемся, чтобы не выйти за границы
        if haystack[i:i + len(needle)] == needle:  # Если срез совпадает с needle
            return i  # Возвращаем индекс начала вхождения

    return -1  # Если подстрока не найдена, возвращаем -1


# Пример вызова функции
print(find_index("sadbutsad", "sad"))  # Ожидаемый результат: 0

"""
Анализ сложности:
- Временная сложность: O(n * m) в худшем случае (где n - длина haystack, m - длина needle).
  Хотя в среднем случае работает быстрее, из-за прерывания цикла при первом вхождении.
- Пространственная сложность: O(1), так как не используем дополнительную память.
"""
