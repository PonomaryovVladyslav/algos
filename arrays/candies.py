# Задача: Раздача конфет детям в зависимости от их рейтингов.
# Дано: список рейтингов детей, где каждый ребенок должен получить как минимум 1 конфету.
# Условия раздачи:
# 1. Дети с более высоким рейтингом должны получать больше конфет, чем их соседи с более низким рейтингом.
# 2. Нужно минимизировать общее количество конфет.

def candy(ratings: list[int]) -> int:
    """
    Функция вычисляет минимальное количество конфет, необходимых для раздачи детям согласно условиям.

    :param ratings: list[int] - список рейтингов детей.
    :return: int - минимальное количество конфет, необходимых для раздачи.
    """

    n: int = len(ratings)
    candies: list[int] = [1] * n  # Всем детям выдаем по одной конфете

    # Первый проход (слева направо): следим за возрастанием рейтинга
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:  # Если рейтинг текущего ребёнка выше предыдущего
            candies[i] = candies[i - 1] + 1  # Даем ему больше конфет, чем предыдущему

    # Второй проход (справа налево): следим за убыванием рейтинга
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:  # Если рейтинг текущего ребёнка выше следующего
            candies[i] = max(candies[i], candies[i + 1] + 1)  # Даем больше конфет, но с учетом предыдущего прохода

    return sum(candies)  # Возвращаем общее количество конфет


# Пример вызова функции
print(candy([1, 2, 2, 1, 4, 6, 2, 4]))  # Ожидаемый результат: 13

"""
Анализ сложности:
- Временная сложность: O(n), так как мы проходим массив дважды (слева направо и справа налево).
- Пространственная сложность: O(n), так как используем дополнительный массив candies для хранения количества конфет.
"""
