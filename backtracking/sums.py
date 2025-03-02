# Задача: Найти все уникальные комбинации чисел, сумма которых равна `target`.
# Дано: список `candidates`, содержащий уникальные положительные числа, и `target`.
# Нужно: вернуть все возможные комбинации, где числа могут использоваться многократно.

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """
    Функция находит все возможные комбинации чисел из `candidates`,
    сумма которых равна `target`. Одно и то же число можно использовать многократно.

    :param candidates: list[int] - список возможных чисел.
    :param target: int - целевая сумма.
    :return: list[list[int]] - список всех возможных комбинаций.
    """

    result: list[list[int]] = []  # Итоговый список комбинаций

    def backtrack(start: int, path: list[int], total: int) -> None:
        """
        Рекурсивная функция для поиска всех возможных комбинаций.

        :param start: int - индекс, с которого начинаем перебор.
        :param path: list[int] - текущая комбинация чисел.
        :param total: int - текущая сумма чисел в `path`.
        """

        if total == target:  # Если сумма достигла `target`
            result.append(path[:])  # Добавляем копию комбинации
            return
        if total > target:  # Если превысили `target`, прерываем ветку
            return

        for i in range(start, len(candidates)):  # Перебираем числа
            path.append(candidates[i])  # Добавляем число в комбинацию
            backtrack(i, path, total + candidates[i])  # Повторное использование числа
            path.pop()  # Откат (backtracking)

    backtrack(0, [], 0)
    return result


# 🔹 Тестируем
print(combination_sum([2, 3, 6, 7], 7))
# Ожидаемый результат: [[2,2,3], [7]]

print(combination_sum([2, 3, 5], 8))
# Ожидаемый результат: [[2,2,2,2], [2,3,3], [3,5]]

print(combination_sum([2], 1))
# Ожидаемый результат: []

"""
Анализ сложности:
- Временная сложность: O(2^t), где `t` — целевой `target`, так как каждый элемент можно использовать многократно.
- Пространственная сложность: O(n), так как глубина рекурсии ограничена размером `target / min(candidates)`.
"""
