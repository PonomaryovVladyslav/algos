# Задача: Полное выравнивание текста.
# Дано: список слов `words` и максимальная ширина строки `max_width`.
# Нужно: вернуть список строк, в которых слова распределены так, чтобы текст был полностью выровнен.

def text_justify(words: list[str], max_width: int) -> list[str]:
    """
    Функция выполняет полное выравнивание текста.

    :param words: list[str] - список слов.
    :param max_width: int - максимальная ширина строки.
    :return: list[str] - список строк с выровненным текстом.
    """

    result: list[str] = []  # Итоговый список строк
    line: list[str] = []  # Текущая строка
    line_length: int = 0  # Длина текущей строки без пробелов

    for word in words:
        # Проверяем, влезет ли текущее слово с пробелами в строку
        if line_length + len(word) + len(line) > max_width:
            # Распределяем пробелы по строке
            for i in range(max_width - line_length):  # Количество пробелов для добавления
                line[i % (len(line) - 1 or 1)] += " "  # Распределяем пробелы равномерно

            result.append("".join(line))  # Добавляем выровненную строку в результат
            line, line_length = [], 0  # Очищаем текущую строку

        line.append(word)  # Добавляем слово в строку
        line_length += len(word)  # Увеличиваем длину строки без пробелов

    # Обрабатываем последнюю строку (левое выравнивание)
    result.append(" ".join(line).ljust(max_width))

    return result


# 🔹 Тестируем
words1 = ["This", "is", "an", "example", "of", "text", "justification."]
max_width1 = 16
print("\n".join(text_justify(words1, max_width1)))

"""
Ожидаемый результат:
"This    is    an"
"example  of text"
"justification.  "
"""

"""
Анализ сложности:
- Временная сложность: O(n), так как мы проходим по всем словам и равномерно распределяем пробелы.
- Пространственная сложность: O(n), так как используем список `result` для хранения результата.
"""
